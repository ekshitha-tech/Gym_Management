// Copyright (c) 2025, ekshitha and contributors
// For license information, please see license.txt

frappe.query_reports["Fitness JOurney"] = {
    "filters": [
        {
            "fieldname": "gym_member",
            "label": "Gym Member",
            "fieldtype": "Link",
            "options": "Gym Member",
            "reqd": 0  // optional
        },
        {
            "fieldname": "workout_date",
            "label": "Workout Date",
            "fieldtype": "Date",
            "reqd": 0  // optional
        }
    ]
}
