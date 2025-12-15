# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class GymClassBooking(Document):
    pass

def weekly_class_booking_summary():
    """
    Send weekly summary of all Gym Class Bookings
    """
    from datetime import datetime, timedelta

    today = datetime.today().date()
    last_week = today - timedelta(days=7)

    bookings = frappe.get_all(
        "Gym Class Booking",
        filters={"schedule": ["between", [last_week, today]]},
        fields=["gym_member", "class_name", "schedule", "schedule_time", "gym_trainer", "status"]
    )

    print("Recipients:", ["ekshithaavilala@gmail.com"])  # print recipients here
    print("Number of bookings:", len(bookings))          # print number of bookings here

    if not bookings:
        summary = "<p>No classes held in the past week.</p>"
    else:
        summary = "<ul>"
        for b in bookings:
            summary += f"<li>Member: {b['gym_member']}, Class: {b['class_name']}, Schedule: {b['schedule']} {b['schedule_time']}, Trainer: {b['gym_trainer']}, Status: {b['status']}</li>"
        summary += "</ul>"

    subject = f"Weekly Gym Class Booking Summary ({last_week} to {today})"

    recipients = ["ekshithaavilala@gmail.com"]

    try:
        frappe.sendmail(recipients=recipients, subject=subject, message=f"<h3>Weekly Gym Class Summary</h3>{summary}")
        print("Email sent!")
    except Exception as e:
        frappe.log_error(message=str(e), title="Weekly Class Summary Email Failed")
        print("Email failed:", e)
