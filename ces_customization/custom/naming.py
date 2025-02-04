from frappe.model.naming import determine_consecutive_week_number
from frappe.utils import (
    getdate,
    # get_datetime
)


def parse_naming_series_variable(doc, variable):
    date = getdate()
    date = doc.get("posting_date") or doc.get("transaction_date") or doc.get("date") or getdate()
    if isinstance(date, str):
        date = getdate(date)

    # Populate data base on date
    r_ad = populate_serie(date=date)
    r_be = populate_serie(date=date, year_type='BE')

    # return vairable result
    if variable == 'CES-YY' and doc:
        return r_ad['yy']

    if variable == 'CES-YYYY' and doc:
        return r_ad['yyyy']

    if variable == 'CES-YY-BE' and doc:
        return r_be['yy']

    if variable == 'CES-YYYY-BE' and doc:
        return r_be['yyyy']

    if variable == 'CES-WW' and doc:
        return r_ad['ww']

    if variable == 'CES-MM' and doc:
        return r_ad['mm']

    if variable == 'CES-DD' and doc:
        return r_ad['dd']

    if variable == 'CES-YYYYMM-BE' and doc:
        return f"{r_be['yyyy']}{r_be['mm']}"

    if variable == 'CES-YYMM-BE' and doc:
        return f"{r_be['yy']}{r_be['mm']}"

    if variable == 'CES-YYYYMM' and doc:
        return f"{r_ad['yyyy']}{r_ad['mm']}"

    if variable == 'CES-YYMM' and doc:
        return f"{r_ad['yy']}{r_ad['mm']}"

    if variable == 'CES-PMT-TYPE' and doc:
        pmt_type = doc.get('payment_type')
        result = 'PV'
        result = 'RV' if pmt_type == 'Receive' else result
        result = 'ITV' if pmt_type == 'Internal Transfer' else result
        return result


def populate_serie(date, year_type='AD'):
    # make sure that the supply posting date is in datetime type
    # sometimes Frappe just return datetime as str
    target_date = getdate(date)
    result = {}
    if year_type == 'AD':
        result['yyyy'] = str(target_date.year)
        result['yy'] = result['yyyy'][-2:]
    else:
        result['yyyy'] = str(int(target_date.year)+543)
        result['yy'] = result['yyyy'][-2:]

    result['ww'] = str(determine_consecutive_week_number(target_date)).zfill(2)

    result['mm'] = str(target_date.month).zfill(2)

    result['dd'] = str(target_date.day).zfill(2)
    return result
