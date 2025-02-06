# import frappe
import click
from ces_customization.install import make_property_setters
from ces_customization.constants import (
    DOCTYPE_NAMING_SERIES,
    ERPNEXT_THAILAND_DOCTYPE_NAMING_SERIES,
    HRMS_DOCTYPE_NAMING_SERIES
)


def before_app_uninstall(app_name):
    if app_name == "erpnext_thailand":
        click.secho("Restore Naming Series for DocTypes to default value in ERPNext Thailand...", fg="yellow")
        make_property_setters(action='uninstall', input_dict=ERPNEXT_THAILAND_DOCTYPE_NAMING_SERIES)
    # 	delete_custom_fields(HRMS_CUSTOM_FIELDS)
    if app_name == "hrms":
        click.secho("Restore Naming Series for DocTypes to default value in HRMS...", fg="yellow")
        make_property_setters(action='uninstall', input_dict=HRMS_DOCTYPE_NAMING_SERIES)


def before_uninstall():
    click.secho("Sad that You are gone!", fg="yellow")
    click.secho("Restore Naming Series for DocTypes to default value in ERPNext...", fg="yellow")
    make_property_setters(action='uninstall', input_dict=DOCTYPE_NAMING_SERIES)


# def delete_custom_fields(custom_fields):
#     """Helper function to delete custom fields"""
#     for doctypes, fields in custom_fields.items():
#         if isinstance(fields, dict):
#             fields = [fields]
#         if isinstance(doctypes, str):
#             doctypes = (doctypes,)
#         for doctype in doctypes:
#             frappe.db.delete(
#                 "Custom Field",
#                 {
#                     "fieldname": ("in", [field["fieldname"] for field in fields]),
#                     "dt": doctype,
#                 },
#             )
#             frappe.clear_cache(doctype=doctype)
