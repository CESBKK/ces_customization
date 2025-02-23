import frappe
import frappe.defaults
from frappe.model.naming import set_name_by_naming_series, set_name_from_naming_options, _format_autoname
from ces_customization.custom.naming import ces_format_autoname
from frappe.model.document import Document


class ces_Customer(Document):

    def autoname(self):
        # First part from ERPNext's default autoname located in
        # erpnext/selling/doctype/customer/customer.py/Class Customer
        cust_master_name = frappe.defaults.get_global_default("cust_master_name")
        if cust_master_name == "Customer Name":
            self.name = self.get_customer_name()
        elif cust_master_name == "Naming Series":
            set_name_by_naming_series(self)
        else:
            # second part is customization if ERPNext version change need to recheck the code
            autoname = frappe.get_meta(self.doctype).autoname
            _autoname = autoname.lower()
            if not _autoname.startswith("format:"):
                set_name_from_naming_options(autoname, doc=self)
            else:
                # First pass, process CES variables and serie's sequence #####
                autoname = ces_format_autoname(autoname, doc=self)

                # Second pass, run thru default erpnext's processor to process {DD} {MM} {YY}
                self.name = _format_autoname(autoname, self)
