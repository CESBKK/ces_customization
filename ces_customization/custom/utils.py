from frappe.model.naming import determine_consecutive_week_number
from frappe.utils import getdate


def populate_thai_date(date, year_type='AD'):
    # make sure that the supply posting date is in datetime type
    # sometimes Frappe just return datetime as str
    target_date = getdate(date)
    month_l = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'
    month_s = 'x ม.ค. ก.พ. มี.ค. เม.ย. พ.ค. มิ.ย. ก.ค. ก.ย. ต.ค. พ.ย. ธ.ค.'
    result = {}

    if year_type == 'AD':
        result['yyyy'] = str(target_date.year)
        result['yy'] = result['yyyy'][-2:]
    else:
        result['yyyy'] = str(int(target_date.year)+543)
        result['yy'] = result['yyyy'][-2:]

    result['ww'] = str(determine_consecutive_week_number(target_date)).zfill(2)

    result['mm'] = str(target_date.month).zfill(2)
    result['th_mm'] = month_s.split()[target_date.month]
    result['th_mmmm'] = month_l.split()[target_date.month]

    result['dd'] = str(target_date.day).zfill(2)
    result['d'] = str(target_date.day)
    return result
