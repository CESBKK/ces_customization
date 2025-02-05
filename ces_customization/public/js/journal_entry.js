// Copyright (c) 2025, Cloud Engineering and Services Co., Ltd. and contributors.
// For license information, please see license.txt

frappe.ui.form.on("Journal Entry", {
    refresh(frm){
        frm.trigger('update_ces_fields');
    },
    posting_date(frm) {
        //Trigger update CES feilds whenever posting_date changed!
        frm.trigger('update_ces_fields');
    },
    update_ces_fields(frm) {
        //Populate CES field
        const th_month_l = new Array('x', 'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม');
        const th_month_s = new Array('x', 'ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.')
        const pd_date = new Date(frm.doc.posting_date);
        const pd_month = pd_date.getUTCMonth()+1;
        const pd_day = pd_date.getUTCDate();
        const pd_year = pd_date.getUTCFullYear();
        const pd_year_be = pd_year+543;
        
        // Populate posting date with BE year
        const be_date = `${pd_year_be}-${pd_month.toString().padStart(2,'0')}-${pd_day.toString().padStart(2,'0')}`;

        // Set value to each Virtual DocField
        frm.set_value('ces_thai_month_abbr', th_month_s[pd_month]);
        frm.set_value('ces_thai_month', th_month_l[pd_month]);
        frm.set_value('ces_posting_date_be', be_date);
        frm.set_value('ces_pd_yyyy_be', `${pd_year_be}`);
        frm.set_value('ces_pd_yy_be', `${pd_year_be%100}`);
        frm.set_value('ces_pd_yyyy', `${pd_year}`);
        frm.set_value('ces_pd_yy', `${pd_year%100}`);
        frm.set_value('ces_pd_mm', `${pd_month.toString().padStart(2,'0')}`);
        frm.set_value('ces_pd_dd', `${pd_day.toString().padStart(2,'0')}`);
        frm.set_value('ces_pd_d', `${pd_day}`);
    },
});