# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


<<<<<<< Updated upstream
class GymWorkoutPlan(Document):
	pass
=======
import frappe
from frappe.website.website_generator import WebsiteGenerator


class GymWorkoutPlan(WebsiteGenerator):
    pass

    # def get_context(self, context):
    #     context.no_cache = 1
    #     return context

  
 
>>>>>>> Stashed changes
