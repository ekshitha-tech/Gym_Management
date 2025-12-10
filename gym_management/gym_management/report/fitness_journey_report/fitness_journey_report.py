# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe.utils import getdate, flt

def execute(filters=None):
    """
    Script Report: Fitness Journey with Chart (Weight & Calories)
    """

    filters = filters or {}
    gym_member = filters.get("gym_member")

    # Fetch workout journey records, optionally filtered by gym member
    conditions = {}
    if gym_member:
        conditions['gym_member'] = gym_member

    records = frappe.get_all(
        'WorkoutJourney',
        filters=conditions,
        fields=['gym_member', 'weight', 'calories', 'date'],
        order_by='date asc'  # for chart to be chronological
    )

    # Prepare table data
    data = []
    for r in records:
        data.append({
            'gym_member': r['gym_member'],
            'weight': r['weight'],
            'calories': r['calories'],
            'date': r['date']
        })

    # Define report columns
    columns = [
        {"label": "Gym Member", "fieldname": "gym_member", "fieldtype": "Link", "options": "Gym Member", "width": 150},
        {"label": "Weight (kg)", "fieldname": "weight", "fieldtype": "Float", "width": 100},
        {"label": "Calories Burned", "fieldname": "calories", "fieldtype": "Float", "width": 120},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 100}
    ]

    # Prepare chart data
    chart = {
        "data": {
            "labels": [r['date'].strftime("%Y-%m-%d") if hasattr(r['date'], "strftime") else str(r['date']) for r in records],
            "datasets": [
                {
                    "name": "Weight (kg)",
                    "values": [flt(r['weight']) for r in records]
                },
                {
                    "name": "Calories Burned",
                    "values": [flt(r['calories']) for r in records]
                }
            ]
        },
        "type": "line",  # line chart
        "height": 300
    }

    return columns, data, None, chart  # chart is returned as 4th element

