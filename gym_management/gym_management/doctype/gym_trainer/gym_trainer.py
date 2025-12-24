# Copyright (c) 2025, ekshitha and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class GymTrainer(Document):

    def validate(self):
        self.validate_phone_number()

    def validate_phone_number(self):
        if self.phone_number:
            phone = str(self.phone_number).strip()

            if not phone.isdigit():
                frappe.throw("Phone number must contain only digits")

            if len(phone) != 10:
                frappe.throw("Phone number must be exactly 10 digits")


    def validate_email(self):
        if self.email:
            if not validate_email_address(self.email, throw=False):
                frappe.throw("Invalid email format (example: name@gmail.com)")
