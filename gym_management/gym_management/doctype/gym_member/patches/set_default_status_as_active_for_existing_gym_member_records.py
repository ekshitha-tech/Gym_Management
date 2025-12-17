
import frappe

def execute():
    """Set default status as Active for existing Gym Member records"""

    frappe.db.sql("""
        UPDATE `tabGym Member`
        SET status = 'Active'
        WHERE status IS NULL OR status = ''
    """)

    frappe.db.commit()
