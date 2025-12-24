# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt



import frappe
from frappe.website.website_generator import WebsiteGenerator


class GymWorkoutPlan(WebsiteGenerator):

    def get_context(self, context):
        context.no_cache = 1
        return context

  
 