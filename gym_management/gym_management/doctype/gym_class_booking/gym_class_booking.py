# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class GymClassBooking(Document):
    pass
@frappe.whitelist()
def weekly_class_booking_summary():
    """
    Send weekly summary of all Gym Class Bookings
    """
    today = datetime.today().date()
    last_week = today - timedelta(days=7)

    bookings = frappe.get_all(
        "Gym Class Booking",
        filters={"schedule": ["between", [last_week, today]]},
        fields=["gym_member", "class_name", "schedule", "schedule_time", "gym_trainer", "status"]
    )

    if not bookings:
        summary = "<p>No classes held in the past week.</p>"
    else:
        summary = "<ul>"
        for b in bookings:
            summary += f"<li>Member: {b['gym_member']}, Class: {b['class_name']}, Schedule: {b['schedule']} {b['schedule_time']}, Trainer: {b['gym_trainer']}, Status: {b['status']}</li>"
        summary += "</ul>"

    # Get unique trainer names from bookings
    trainer_names = list({b['gym_trainer'] for b in bookings if b['gym_trainer']})

    # Fetch trainer emails dynamically
    trainers = frappe.get_all(
        "Gym Trainer",
        filters={"name": ["in", trainer_names]},
        fields=["email"]  # replace 'email' with your actual email field name if different
    )
    recipients = [t["email"] for t in trainers if t.get("email")]

    if not recipients:
        print("No trainer emails found. Email not sent.")
        return

    subject = f"Weekly Gym Class Booking Summary ({last_week} to {today})"

    try:
        frappe.sendmail(recipients=recipients, subject=subject, message=f"<h3>Weekly Gym Class Summary</h3>{summary}")
        print("Email sent to:", recipients)
    except Exception as e:
        frappe.log_error(message=str(e), title="Weekly Class Summary Email Failed")
        print("Email failed:", e)
