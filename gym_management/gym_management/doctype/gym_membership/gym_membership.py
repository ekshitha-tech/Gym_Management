# # Copyright (c) 2025, ekshitha and contributors
# # For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today


class GymMembership(Document):
	pass

@frappe.whitelist()
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







