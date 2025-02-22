from datetime import datetime
from ces_customization.custom.utils import populate_thai_date
from frappe.model.document import Document


class ces_JournalEntry(Document):
    '''This class populate Virtual DocField Data which we added to Journal Entry DocType'''
    @property
    def ces_posting_date_be(self):
        result = populate_thai_date(self.posting_date, year_type='BE')
        return datetime(int(result['yyyy']), int(result['mm']), int(result['dd']))

    @property
    def ces_pd_yyyy_be(self):
        result = populate_thai_date(self.posting_date, year_type='BE')
        return result['yyyy']

    @property
    def ces_pd_yy_be(self):
        result = populate_thai_date(self.posting_date, year_type='BE')
        return result['yy']

    @property
    def ces_pd_yyyy(self):
        result = populate_thai_date(self.posting_date)
        return result['yyyy']

    @property
    def ces_pd_yy(self):
        result = populate_thai_date(self.posting_date)
        return result['yy']

    @property
    def ces_pd_mm(self):
        result = populate_thai_date(self.posting_date)
        return result['mm']

    @property
    def ces_pd_dd(self):
        result = populate_thai_date(self.posting_date)
        return result['dd']

    @property
    def ces_pd_d(self):
        result = populate_thai_date(self.posting_date)
        return result['d']

    @property
    def ces_thai_month_abbr(self):
        result = populate_thai_date(self.posting_date)
        return result['th_mm']

    @property
    def ces_thai_month(self):
        result = populate_thai_date(self.posting_date)
        return result['th_mmmm']
