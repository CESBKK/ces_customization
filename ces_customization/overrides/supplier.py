import frappe
import frappe.defaults
from frappe.model.naming import set_name_by_naming_series, set_name_from_naming_options, _format_autoname
from ces_customization.custom.naming import ces_format_autoname
from frappe.model.document import Document


class ces_Supplier(Document):

    def autoname(self):
        # First part from ERPNext's default autoname located in
        # erpnext/buying/doctype/supplier/supplier.py/Class Supplier
        supp_master_name = frappe.defaults.get_global_default("supp_master_name")
        if supp_master_name == "Supplier Name":
            self.name = self.supplier_name
        elif supp_master_name == "Naming Series":
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
