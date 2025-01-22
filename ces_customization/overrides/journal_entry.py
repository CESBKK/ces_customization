from datetime import datetime
from erpnext.accounts.doctype.journal_entry.journal_entry import JournalEntry



class ces_JournalEntry(JournalEntry):
    '''This class populate VIrtual DocField Data which we added to Journal Entry DocType'''
    @property
    def ces_pd_serie(self):
        r = self.populate_pd_serie()
        return f'{r['yy']}{r['mm']}-{r['dd']}'


    @property
    def ces_pd_serie_th(self):
        r = self.populate_pd_serie(year_type='BE')
        return f'{r['yy']}{r['mm']}-{r['dd']}'


    @property
    def ces_be_date(self):
        r = self.populate_pd_serie(year_type='BE')
        return datetime(int(r['yyyy']), int(r['mm']), int(r['dd']))


    @property
    def ces_th_mm(self):
        r = self.populate_pd_serie()
        return r['th_mm']


    @property
    def ces_be_yy(self):
        r = self.populate_pd_serie(year_type='BE')
        return r['yy']


    @property
    def ces_be_yyyy(self):
        r = self.populate_pd_serie(year_type='BE')
        return r['yyyy']


    @property
    def ces_th_mmmm(self):
        r = self.populate_pd_serie()
        return r['th_mmmm']


    def populate_pd_serie(self, year_type='AD'):
        result = {}
        if year_type == 'AD':
            result['yyyy']  = str(self.posting_date.year)
            result['yy']    = result['yyyy'][-2:]
        else:
            result['yyyy']  = str(int(self.posting_date.year)+543)
            result['yy']    = result['yyyy'][-2:]

        result['mm'] = str(self.posting_date.month).zfill(2)
        
        month_l = ['x', 'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
        month_s = ['x', 'ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.']
        result['th_mm']     = month_s[self.posting_date.month]
        result['th_mmmm']   = month_l[self.posting_date.month]

        result['dd'] = str(self.posting_date.day).zfill(2)
        return result


    # def before_naming(self):
    #     if self.ces_pd_serie is None:
    #         self.ces_pd_serie
        
    #     if self.ces_pd_serie_th is None:
    #         self.ces_pd_serie_th