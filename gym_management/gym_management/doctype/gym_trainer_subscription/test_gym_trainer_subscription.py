# Copyright (c) 2025, ekshitha and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymTrainerSubscription(FrappeTestCase):
	pass


import frappe
import unittest
from datetime import date

class TestGymMembership(unittest.TestCase):

    def test_beginner_membership(self):
        """Test inserting a Beginner Plan membership"""
        doc = frappe.get_doc({
            "doctype": "Gym Membership",
            "gym_member": "GM-01",
            "membership_plan": "Beginner Plan",
            "trainer": "GT-0002",
            "start_date": date.today(),
            "end_date": date(2025, 12, 31),
            "status": "Active"
        })
        doc.insert(ignore_permissions=True)

    def test_advanced_membership(self):
        """Test inserting an Advanced Plan membership"""
        doc = frappe.get_doc({
            "doctype": "Gym Membership",
            "gym_member": "GM-01",
            "membership_plan": "Advanced Plan",
            "trainer": "GT-0002",
            "start_date": date.today(),
            "end_date": date(2026, 1, 31),
            "status": "Active"
        })
        doc.insert(ignore_permissions=True)

