# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt

import frappe
# from frappe.model.document import Document

# class GymWorkoutPlan(Document):
#     pass
# gym_management/gym_management/doctype/gym_workout_plan/gym_workout_plan.py

from frappe.model.document import Document

class GymWorkoutPlan(Document):
    def get_page_info(self):
        return {
            "title": self.plan_name,
            "name": self.name,
            "description": self.description,
            "children": [
                {
                    "exercise": row.exercise_name,
                    "reps": row.reps,
                    "sets": row.sets
                }
                for row in self.gym_workout_plan  # Replace `exercises` with your child table fieldname
            ]
        }
