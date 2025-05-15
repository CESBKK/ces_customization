import frappe
import re
from frappe.utils import getdate
from frappe.model.naming import getseries
from ces_customization.custom.utils import populate_thai_date


def parse_naming_series_variable(doc, variable):
    if doc is None:
        doc = frappe.get_doc('Customer', 'CZZZ-999999999')

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
        abbr = frappe.db.get_value(
            doctype='Company',
            filters={'company': doc.get('company')},
            fieldname='abbr')
        return abbr


def ces_format_autoname(autoname: str, doc):
    """
    Generate autoname by replacing all instances of CES braced params (fields, date params e.g.
    'CES-YY-BE', 'CES-MM', 'CES-YY' etc., series) Independent of remaining string or separators.

    Example pattern: 'format:LOG-{MM}-{fieldname1}-{fieldname2}-{#####}'

    Base on frappe.model.naming._format_autoname()
    """

    BRACED_PARAMS_PATTERN = re.compile(r'(\{[\w\- | #]+\})')

    def get_param_value_for_match(match):
        param: str = match.group()
        for part in [param[1:-1]]:
            if part.startswith('CES'):
                output = parse_naming_series_variable(doc=doc, variable=part)
            elif part.startswith('#'):
                # Technically this should be passed to frappe's default processor
                # but there is a bug as serie_name is blank and yield unexpected result.
                # if it is fixed later on, we can remove this branch.
                serie_name = f'CES-{doc.get("doctype")}'
                digits = len(part)
                output = getseries(serie_name, digits)
            else:
                # left over which are frappe's default i.e. {MM} {DD} {YY}
                # We will pass this to _format_autoname.
                output = '{' + part + '}'
        return output

    # Replace braced params with their parsed value
    name = BRACED_PARAMS_PATTERN.sub(get_param_value_for_match, autoname)

    return name
