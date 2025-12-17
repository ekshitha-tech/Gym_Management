// Copyright (c) 2025, ekshitha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership Card", {
    refresh: function(frm) {
        // Override Print action
        frm.page.set_primary_action(__('Print'), function() {
            frappe.call({
                method: "gym_management.gym_management.doctype.gym_membership_card.gym_membership_card.check_print_permission",
                args: {
                    docname: frm.doc.name
                },
                callback: function(r) {
                    if(r.message) {
                        // Open the print preview if permission passes
                        frm.print_doc();
                    }
                }
            });
        });
    }
});
