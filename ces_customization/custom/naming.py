import frappe
import re
from frappe.utils import getdate
from ces_customization.custom.utils import populate_thai_date


def parse_naming_series_variable(doc, variable):
    date = getdate()
    date = doc.get('posting_date') or doc.get('transaction_date') or doc.get('date') or getdate()
    if isinstance(date, str):
        date = getdate(date)

    # Populate data base on date
    result_ad = populate_thai_date(date=date)
    result_be = populate_thai_date(date=date, year_type='BE')

    # return vairable result
    if variable == 'CES-YY' and doc:
        return result_ad['yy']

    if variable == 'CES-YYYY' and doc:
        return result_ad['yyyy']

    if variable == 'CES-YY-BE' and doc:
        return result_be['yy']

    if variable == 'CES-YYYY-BE' and doc:
        return result_be['yyyy']

    if variable == 'CES-WW' and doc:
        return result_ad['ww']

    if variable == 'CES-MM' and doc:
        return result_ad['mm']

    if variable == 'CES-DD' and doc:
        return result_ad['dd']

    if variable == 'CES-YYYYMM-BE' and doc:
        return f"{result_be['yyyy']}{result_be['mm']}"

    if variable == 'CES-YYMM-BE' and doc:
        return f"{result_be['yy']}{result_be['mm']}"

    if variable == 'CES-YYYYMM' and doc:
        return f"{result_ad['yyyy']}{result_ad['mm']}"

    if variable == 'CES-YYMM' and doc:
        return f"{result_ad['yy']}{result_ad['mm']}"

    if variable == 'CES-JV-TYPE' and doc:
        jv_type = doc.get('voucher_type')

        if jv_type == 'Inter Company Journal Entry':
            return 'IC-'
        elif jv_type == 'Bank Entry':
            return 'BNK-'
        elif jv_type == 'Cash Entry':
            return 'CSH-'
        elif jv_type == 'Credit Card Entry':
            return 'CRD-'
        elif jv_type == 'Debit Note':
            return 'DRN-'
        elif jv_type == 'Credit Note':
            return 'CRN-'
        elif jv_type == 'Contra Entry':
            return 'CNT-'
        elif jv_type == 'Excise Entry':
            return 'EXS-'
        elif jv_type == 'Write Off Entry':
            return 'WOF-'
        elif jv_type == 'Opening Entry':
            return 'OPN-'
        elif jv_type == 'Depreciation Entry':
            return 'DEP-'
        elif jv_type == 'Exchange Rate Revaluation':
            return 'EXR-'
        elif jv_type == 'Exchange Gain Or Loss':
            return 'EXGL'
        elif jv_type == 'Deferred Revenue':
            return 'DFR-'
        elif jv_type == 'Deferred Expense':
            return 'DFE-'
        else:
            return ''

    if variable == 'CES-PMT-TYPE' and doc:
        pmt_type = doc.get('payment_type')
        result = 'PV'
        result = 'RV' if pmt_type == 'Receive' else result
        result = 'ITV' if pmt_type == 'Internal Transfer' else result
        return result

    if variable == 'CES-COM-ABBR' and doc:
        # doc is current doc we are working on
        # company_info_doc is another doc that contain Company Information
        # in this case company_info_doc => Doctype Company which contain abbr field.
        company_info_doc = frappe.get_doc('Company', doc.get('company'))
        return company_info_doc.get('abbr')


def ces_format_autoname(autoname: str, doc):
    """
    Generate autoname by replacing all instances of CES braced params (fields, date params ('DD', 'MM', 'YY'), series)
    Independent of remaining string or separators.

    Example pattern: 'format:LOG-{MM}-{fieldname1}-{fieldname2}-{#####}'

    Base on frappe.model.naming._format_autoname()
    """

    # first_colon_index = autoname.find(":")
    # autoname_value = autoname[first_colon_index + 1 :]
    BRACED_PARAMS_PATTERN = re.compile(r'(\{CES[\w-]+\})')

    def get_param_value_for_match(match):
        param = match.group()
        output = ''
        for part in [param[1:-1]]:
            output += parse_naming_series_variable(doc=doc, variable=part)
        return output

    # Replace braced params with their parsed value
    name = BRACED_PARAMS_PATTERN.sub(get_param_value_for_match, autoname)

    return name