from datetime import datetime
from erpnext.accounts.doctype.journal_entry.journal_entry import JournalEntry
from frappe.utils import getdate


class ces_JournalEntry(JournalEntry):
    '''This class populate Virtual DocField Data which we added to Journal Entry DocType'''
    @property
    def ces_posting_date_be(self):
        r = self.populate_pd_serie(year_type='BE')
        return datetime(int(r['yyyy']), int(r['mm']), int(r['dd']))

    @property
    def ces_pd_yyyy_be(self):
        r = self.populate_pd_serie(year_type='BE')
        return r['yyyy']

    @property
    def ces_pd_yy_be(self):
        r = self.populate_pd_serie(year_type='BE')
        return r['yy']

    @property
    def ces_pd_yyyy(self):
        r = self.populate_pd_serie()
        return r['yyyy']

    @property
    def ces_pd_yy(self):
        r = self.populate_pd_serie()
        return r['yy']

    @property
    def ces_pd_mm(self):
        r = self.populate_pd_serie()
        return r['mm']

    @property
    def ces_pd_dd(self):
        r = self.populate_pd_serie()
        return r['dd']

    @property
    def ces_pd_d(self):
        r = self.populate_pd_serie()
        return r['d']

    @property
    def ces_thai_month_abbr(self):
        r = self.populate_pd_serie()
        return r['th_mm']

    @property
    def ces_thai_month(self):
        r = self.populate_pd_serie()
        return r['th_mmmm']

    def populate_pd_serie(self, year_type='AD'):
        # make sure that the supply posting date is in datetime type
        # sometimes Frappe just return datetime as str
        posting_date = getdate(self.posting_date)
        result = {}
        if year_type == 'AD':
            result['yyyy'] = str(posting_date.year)
            result['yy'] = result['yyyy'][-2:]
        else:
            result['yyyy'] = str(int(posting_date.year)+543)
            result['yy'] = result['yyyy'][-2:]

        result['mm'] = str(posting_date.month).zfill(2)

        month_l = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'
        month_s = 'x ม.ค. ก.พ. มี.ค. เม.ย. พ.ค. มิ.ย. ก.ค. ก.ย. ต.ค. พ.ย. ธ.ค.'
        result['th_mm'] = month_s.split()[posting_date.month]
        result['th_mmmm'] = month_l.split()[posting_date.month]

        result['dd'] = str(posting_date.day).zfill(2)
        result['d'] = str(posting_date.day)
        return result
