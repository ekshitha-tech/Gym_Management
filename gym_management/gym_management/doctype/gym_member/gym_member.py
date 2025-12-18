# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import validate_email_address

class GymMember(WebsiteGenerator):

    def get_context(self, context):
        member_name = self.name
        doc = frappe.get_doc("Gym Member", member_name)

    def validate(self):
        self.validate_phone()
        self.validate_email()
    def validate_phone(self):
        if self.phone:
            phone = str(self.phone).strip()

            if not phone.isdigit():
                frappe.throw("Phone number must contain only digits")

            if len(phone) != 10:
                frappe.throw("Phone number must be exactly 10 digits")
    def validate_email(self):
        if self.email:
            # checks ONLY format
            if not validate_email_address(self.email, throw=False):
                frappe.throw("Invalid email format. Example: name@gmail.com")