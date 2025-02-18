# import frappe
import click
from ces_customization.setup.install import change_naming_series


def before_app_uninstall(app_name):
    if app_name == 'erpnext_thailand':
        click.secho('Restore Naming Series for DocTypes to default value in ERPNext Thailand...', fg='yellow')
        change_naming_series(action='uninstall', module=app_name)

    if app_name == 'hrms':
        click.secho('Restore Naming Series for DocTypes to default value in HRMS...', fg='yellow')
        change_naming_series(action='uninstall', module=app_name)


def before_uninstall():
    click.secho('Sad that You are gone!', fg='yellow')
    click.secho('Restore Naming Series for DocTypes to default value in ERPNext...', fg='yellow')
    change_naming_series(action='uninstall')


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
