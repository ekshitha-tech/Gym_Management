# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymWorkoutPlan(Document):
    pass
import frappe

def get_context(context):
    plan_route = frappe.form_dict.get("plan")

    if plan_route:
        context.plan = frappe.get_doc(
            "Gym Workout Plan",
            {"route": plan_route, "publish": 1}
        )

    context.plans = frappe.get_all(
        "Gym Workout Plan",
        filters={"publish": 1},
        fields=["plan_name", "level", "description", "route"]
    )

