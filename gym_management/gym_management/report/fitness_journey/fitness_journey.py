# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):
    filters = filters or {}

    # -----------------------
    # Columns
    # -----------------------
    columns = [
        {"label": "Workout Plan", "fieldname": "plan_name", "fieldtype": "Data", "width": 160},
        {"label": "Gym Member", "fieldname": "gym_member", "fieldtype": "Link", "options": "Gym Member", "width": 150},
        {"label": "Workout Date", "fieldname": "workout_date", "fieldtype": "Date", "width": 120},
        {"label": "Weight (kg)", "fieldname": "weight", "fieldtype": "Float", "width": 100},
        {"label": "Calories Burned", "fieldname": "calories", "fieldtype": "Float", "width": 120}
    ]

    data = []
    chart = {}

    # -----------------------
    # Build Filters
    # -----------------------
    query_filters = {}
    if filters.get("gym_member"):
        query_filters["gym_member"] = filters.get("gym_member")
    
    if filters.get("workout_date"):
        date = filters.get("workout_date")
        query_filters["workout_date"] = date  # dynamic date filter

    # -----------------------
    # Fetch Records
    # -----------------------
    records = frappe.get_all(
        "Gym Workout Plan",
        filters=query_filters,
        fields=["name", "plan_name", "gym_member", "workout_date", "weight", "calories"],
        order_by="workout_date asc"
    )

    # -----------------------
    # Table Data
    # -----------------------
    for r in records:
        data.append({
            "plan_name": r.plan_name or r.name,
            "gym_member": r.gym_member,
            "workout_date": r.workout_date,
            "weight": r.weight,
            "calories": r.calories
        })

    # -----------------------
    # Pie Chart Data (Calories per Plan)
    # -----------------------
    if data:
        calories_per_plan = {}
        for r in data:
            plan = r["plan_name"]
            calories_per_plan[plan] = calories_per_plan.get(plan, 0) + flt(r["calories"])

        chart = {
            "data": {
                "labels": list(calories_per_plan.keys()),
                "datasets": [
                    {
                        "name": "Calories Burned",
                        "values": list(calories_per_plan.values())
                    }
                ]
            },
            "type": "pie",
            "height": 300
        }

    return columns, data, [], chart
