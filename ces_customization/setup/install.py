import click
import json
import frappe
from frappe import _
# from frappe.custom.doctype.custom_field.custom_field import \
#     create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import \
    make_property_setter

from ces_customization.setup.constants import (
    DOCTYPE_NAMING_SERIES,
    ERPNEXT_THAILAND_DOCTYPE_NAMING_SERIES,
    HRMS_DOCTYPE_NAMING_SERIES
)


def after_install():
    try:
        # make_custom_fields()
        click.secho("Update Naming Series for DocTypes in ERPNext...", fg="yellow")
        make_property_setters()
        click.secho("Add GFMIS UOMs...", fg="yellow")
        add_uom_data()
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


def make_property_setters(action: str = "install", input_dict: dict = DOCTYPE_NAMING_SERIES):
    if action == "install":
        target = "ces_custom"
    else:
        target = "default"

    for doctypes, serie_values in input_dict.items():
        if isinstance(doctypes, str):
            doctypes = (doctypes,)
        for doctype in doctypes:
            serie_name = serie_values[0][target].split('\n')[0]
            if doctype == "Bank Transaction":
                '''
                Bank Transaction is a bit special, as default naming serie
                is a part of database field default value.
                We will need to ignore all validation to change its
                property setter.
                '''
                naming_series_property_setter(doctype, "default", "", False)
                naming_series_property_setter(doctype, "options", serie_values[0][target], False)
                naming_series_property_setter(doctype, "default", serie_name, False)
            else:
                naming_series_property_setter(doctype, "default", "")
                naming_series_property_setter(doctype, "options", serie_values[0][target])
                naming_series_property_setter(doctype, "default", serie_name)
            frappe.clear_cache(doctype=doctype)


def naming_series_property_setter(doctype,
                                  property,
                                  value,
                                  validate_fields=True):
    make_property_setter(doctype,
                         "naming_series",
                         property,
                         value,
                         "Text",
                         validate_fields_for_doctype=validate_fields)


def after_app_install(app_name):
    if app_name == "erpnext_thailand":
        click.secho("Update Naming Series for DocTypes in ERPNext Thailand...", fg="yellow")
        make_property_setters(action="install", input_dict=ERPNEXT_THAILAND_DOCTYPE_NAMING_SERIES)
        # create_custom_fields(HRMS_CUSTOM_FIELDS, ignore_validate=True)
    if app_name == "hrms":
        click.secho("Update Naming Series for DocTypes in HRMS...", fg="yellow")
        make_property_setters(action="install", input_dict=HRMS_DOCTYPE_NAMING_SERIES)


def add_uom_data():
    '''
    Based on erpnext/setup/setup_wizard/operations/install_fixtures.py
    add Thai UOM หน่วยนับที่ใช้สำหรับจัดทำใบสั่งซื้อ บส.01 ในระบบ GFMIS
    Except:
    - CUP, DAY, KG - exist in erpnext default.
    - HR. - already had "H" for "ชั่วโมง"
    '''
    uoms = json.loads(
        open(frappe.get_app_path("ces_customization", "setup", "data", "gfmis_uom_data.json")).read()
    )
    for d in uoms:
        if not frappe.db.exists("UOM", _(d.get("uom_name"))):
            frappe.get_doc(
                {
                    "doctype": "UOM",
                    "uom_name": _(d.get("uom_name")),
                    "name": _(d.get("uom")),
                    "must_be_whole_number": d.get("must_be_whole_number"),
                    "enabled": 1,
                }
            ).db_insert()
