// Copyright (c) 2025, ekshitha and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Gym Membership", {
// 	refresh(frm) {

// 	},
// });
frappe.realtime.on('new_subscription_alert', (data) => {
    frappe.show_alert({
        message: `<a href="/app/gym-membership/${data.docname}" target="_blank">${data.message}</a>`,
        indicator: 'green'
    });
});
