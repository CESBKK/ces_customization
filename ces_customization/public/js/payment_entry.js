// Copyright (c) 2025, Cloud Engineering and Services Co., Ltd. and contributors.
// For license information, please see license.txt

frappe.require('/assets/ces_customization/js/utils.js');

frappe.ui.form.on("Payment Entry", {
    refresh(frm){
        update_ces_fields(frm);
    },
    posting_date(frm) {
        //Trigger update CES feilds whenever posting_date changed!
        update_ces_fields(frm);
    },
});