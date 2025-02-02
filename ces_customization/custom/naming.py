from frappe.model.naming import determine_consecutive_week_number
from frappe.utils import (
    get_datetime
)


def parse_naming_series_variable(doc, variable):
    if variable == 'CES-PD-YY' and doc:
        date = doc.get('posting_date')
        r = populate_serie(date=date)
        return r['yy']

    if variable == 'CES-PD-YYYY' and doc:
        date = doc.get('posting_date')
        r = populate_serie(date=date)
        return r['yyyy']

    if variable == 'CES-PD-YYBE' and doc:
        date = doc.get('posting_date')
        r = populate_serie(date=date, year_type='BE')
        return r['yy']

    if variable == 'CES-PD-YYYYBE' and doc:
        date = doc.get('posting_date')
        r = populate_serie(date=date, year_type='BE')
        return r['yyyy']

    if variable == 'CES-PD-WW' and doc:
        date = doc.get('posting_date')
        r = populate_serie(date=date)
        return r['ww']

    if variable == 'CES-PD-MM' and doc:
        date = doc.get('posting_date')
        r = populate_serie(date=date)
        return r['mm']

    if variable == 'CES-PD-DD' and doc:
        date = doc.get('posting_date')
        r = populate_serie(date=date)
        return r['dd']

    if variable == 'CES-TD-YY' and doc:
        date = doc.get('transaction_date')
        r = populate_serie(date=date)
        return r['yy']

    if variable == 'CES-TD-YYYY' and doc:
        date = doc.get('transaction_date')
        r = populate_serie(date=date)
        return r['yyyy']

    if variable == 'CES-TD-YYBE' and doc:
        date = doc.get('transaction_date')
        r = populate_serie(date=date, year_type='BE')
        return r['yy']

    if variable == 'CES-TD-YYYYBE' and doc:
        date = doc.get('transaction_date')
        r = populate_serie(date=date, year_type='BE')
        return r['yyyy']

    if variable == 'CES-TD-WW' and doc:
        date = doc.get('transaction_date')
        r = populate_serie(date=date)
        return r['ww']

    if variable == 'CES-TD-MM' and doc:
        date = doc.get('transaction_date')
        r = populate_serie(date=date)
        return r['mm']

    if variable == 'CES-TD-DD' and doc:
        date = doc.get('transaction_date')
        r = populate_serie(date=date)
        return r['dd']

    if variable == 'CES-PMT-TYPE' and doc:
        pmt_type = doc.get('payment_type')
        result = 'PV'
        result = 'RV' if pmt_type == 'Receive' else result
        result = 'ITV' if pmt_type == 'Internal Transfer' else result
        return result


def populate_serie(date, year_type='AD'):
    # make sure that the supply posting date is in datetime type
    # sometimes Frappe just return datetime as str
    target_date = get_datetime(date)
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
