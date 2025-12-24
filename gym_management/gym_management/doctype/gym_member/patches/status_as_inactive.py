import frappe

def execute():
    """Set default status as Inactive for existing Gym Member records"""

    frappe.db.sql("""
        UPDATE `tabGym Member`
        SET status = 'Inactive'
        WHERE status IS NULL OR status = ''
    """)

    frappe.db.commit()
