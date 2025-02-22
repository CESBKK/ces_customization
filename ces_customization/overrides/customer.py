import frappe
import frappe.defaults
from frappe.model.naming import set_name_by_naming_series, set_name_from_naming_options, _format_autoname
from erpnext.selling.doctype.customer.customer import Customer
from ces_customization.custom.naming import ces_format_autoname


class ces_Customer(Customer):

    def autoname(self):
        print('ces_Customer is used...')
        cust_master_name = frappe.defaults.get_global_default("cust_master_name")
        if cust_master_name == "Customer Name":
            self.name = self.get_customer_name()
        elif cust_master_name == "Naming Series":
            set_name_by_naming_series(self)
        else:
            autoname = frappe.get_meta(self.doctype).autoname
            _autoname = autoname.lower()
            if not _autoname.startswith("format:"):
                set_name_from_naming_options(autoname, doc=self)
            else:
                # First pass, process CES variables
                autoname = ces_format_autoname(autoname, doc=self)
                # Second pass, run thru default erpnext's processor
                self.name = _format_autoname(autoname, self)
