# # Copyright (c) 2025, ekshitha and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today


class GymMembership(Document):
	pass


def auto_expire_memberships():

    memberships = frappe.get_all(
        "Gym Membership",
        filters={
            "expiry_date": ["<=", today()],
            "status": "Active"
        },
        fields=["name", "gym_member", "expiry_date"]   # FIXED
    )

    for m in memberships:

        frappe.db.set_value("Gym Membership", m.name, "status", "Expired")

        # Get Gym Member email
        email = frappe.get_value("Gym Member", m.gym_member, "email")

        if email:
            frappe.sendmail(
                recipients=[email],
                subject="Gym Membership Expired",
                message=f"Dear {m.gym_member}, your membership expired on {m.expiry_date}. Please renew to continue."
            )

        frappe.logger().info(
            f"Membership expired: {m.name} ({m.gym_member})"
        )

    frappe.db.commit()






import frappe

def after_insert(doc, method):
    """Send real-time alert to assigned trainer when a member subscribes"""
    if doc.trainer:  # Make sure a trainer is assigned
        message = f"New Subscription!\nMember: {doc.member_name}\nPlan: {doc.plan_name}\nStart Date: {doc.start_date}\nContact: {doc.member_contact}"

        frappe.publish_realtime(
            event='new_subscription_alert',
            message=message,
            user=doc.trainer,  # Only assigned trainer receives it
            doctype=doc.doctype,
            docname=doc.name
        )

