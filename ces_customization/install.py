import click
import frappe
# from frappe.custom.doctype.custom_field.custom_field import \
#     create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import \
    make_property_setter

from ces_customization.constants import (
    DOCTYPE_NAMING_SERIES,
    ERPNEXT_THAILAND_DOCTYPE_NAMING_SERIES
)


def after_install():
    try:
        print("Setting up CES Customization...")
        # make_custom_fields()
        make_property_setters()
        click.secho("Thank you for installing CES Customization!", fg="green")
    except Exception as e:
        BUG_REPORT_URL = "https://github.com/CESBKK/ces_customization/issues/new"
        click.secho(
            "Installation for CES Customization app failed due to an error."
            " Please try re-installing the app or"
            f" report the issue on {BUG_REPORT_URL} if not resolved.",
            fg="bright_red",
        )
        raise e


# def make_custom_fields():
#     print("Setup custom fields for erpnext...")
#     create_custom_fields(ERP_CUSTOM_FIELDS, ignore_validate=True)
#     create_custom_fields(BILLING_CUSTOM_FIELDS, ignore_validate=True)
#     if "hrms" in frappe.get_installed_apps():
#         print("Setup custom fields for hrms...")
#         create_custom_fields(HRMS_CUSTOM_FIELDS, ignore_validate=True)


def make_property_setters(action: str = 'install', input_dict: dict = DOCTYPE_NAMING_SERIES):
    if action == 'install':
        target = 'ces_custom'
        print("Update Naming Series for DocTypes in ERPNext...")
    else:
        target = 'default'
        print("Restore Naming Series for DocTypes to default value in ERPNext...")

    # special treatment last until database definition change
    # bank_transaction_serie_setter(action=action)

    for doctypes, serie_values in input_dict.items():
        if isinstance(doctypes, str):
            doctypes = (doctypes,)
        for doctype in doctypes:
            serie_name = serie_values[0][target].split('\n')[0]
            naming_series_property_setter(doctype, "default", "")
            naming_series_property_setter(doctype, "options", serie_values[0][target])
            naming_series_property_setter(doctype, "default", serie_name)
            frappe.clear_cache(doctype=doctype)


def naming_series_property_setter(doctype, property, value):
    make_property_setter(doctype, "naming_series", property, value, "Text")


# def bank_transaction_serie_setter(action):
#     '''
#     Special treatment for Bank Transaction DocType
#     as serie name was part of default value of database field.
#     Need DDL to make change to database field directly

#     This doctype is used when do bank reconcile by importing bank statement
#     into system.
#     '''
#     if action == 'install':
#         target_value = 'ACC-BTN-.CES-YYMM-BE.-'
#     else:
#         target_value = 'ACC-BTN-.YYYY.-'

#     sql = (
#         'ALTER TABLE `tabBank Transaction` '
#         'CHANGE `naming_series` '
#         '`naming_series` varchar(140) '
#         'CHARACTER SET utf8mb4 '
#         'COLLATE utf8mb4_unicode_ci '
#         f"DEFAULT '{target_value}';"
#     )

#     frappe.db.sql(sql)
#     frappe.clear_cache(doctype='Bank Transaction')


def after_app_install(app_name):
    if app_name == "erpnext_thailand":
        make_property_setters(action='install', input_dict=ERPNEXT_THAILAND_DOCTYPE_NAMING_SERIES)
        # create_custom_fields(HRMS_CUSTOM_FIELDS, ignore_validate=True)
