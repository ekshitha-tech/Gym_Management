import frappe
from frappe.utils import getdate, flt

def execute(filters=None):
    """
    Script Report: Monthly Revenue Summary from Income Entry
    """

    # Fetch all Income Entry records with Amount > 0
    entries = frappe.get_all(
        'Income Entry',
        filters={'amount': ['>', 0]},
        fields=['date', 'amount']
    )

    # Aggregate revenue by month
    monthly_revenue = {}
    for e in entries:
        month = getdate(e['date']).strftime("%Y-%m")
        monthly_revenue[month] = monthly_revenue.get(month, 0) + flt(e['amount'])

    # Prepare data for the report
    data = []
    for month, total in sorted(monthly_revenue.items()):
        data.append({
            'month': month,
            'total_revenue': total
        })

    # Define report columns
    columns = [
        {"label": "Month", "fieldname": "month", "fieldtype": "Data", "width": 120},
        {"label": "Total Revenue", "fieldname": "total_revenue", "fieldtype": "Currency", "width": 150}
    ]

    return columns, data
