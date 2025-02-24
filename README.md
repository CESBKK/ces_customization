# CES Customization

Customization for Thailand

By installing ces_customization, it provides access to additional naming series variables and UOM from Thailand Goverment's standard and a couple of neat tweaks.  Here are a list of available fucntions:
1. [Additional Naming Series Variable](#naming_series)
2. [Thailand's GFMIS Unit of Measurements](#gfmis_uoms)
3. [One-time Customers and One-time Vendors](#onetime)

### <a name="naming_series"></a>Naming Series Variables:
---
#### From CES Customization:

Base on posting date or document date or transactional date. Varibale with BE will return year in Bhudist Era or AD+543.  CES variables also can be used in naming expression for Auto Name by putting them in {-} e.g. format:CUST-{CES-YYMM-BE}{#####}
- .CES-YY.
- .CES-YYYY.
- .CES-YY-BE.
- .CES-YYYY-BE.
- .CES-WW.
- .CES-MM.
- .CES-DD.
- .CES-YYYYMM.
- .CES-YYMM.
- .CES-YYYYMM-BE.
- .CES-YYMM-BE.
- .CES-PMT-TYPE.  - Special for payment_type field or Payment Entry DocType.
- .CES-JV-TYPE.   - Special for entry_type field or Journal Entry DocType.
- .CES-COM-ABBR.  - Company's Abbreviated Name

#### From ERPNext:

Base on current transactional date.
- .YYYY.
- .YY.
- .MM.
- .DD.
- .WW.
- .FY.
- .{fieldname}.

#### From [ERPNext Thailand](https://github.com/ecosoft-frappe/erpnext_thailand):

Base on posting date or document date or transactional date.
- .YYYY-DATE.
- .YY-DATE.
- .MM-DATE.
- .DD-DATE.
- .WW-DATE.

### <a name="gfmis_uoms"></a>UOMs from Thailand's GFMIS
---
Add Thai UOMs based on goverment's standard หน่วยนับที่ใช้สำหรับจัดทำใบสั่งซื้อ บส.01 ในระบบ GFMIS

Note: UOMs are imported only. No uninstallation when app uninstalled.


### <a name="onetime"></a>One-time Customers and One-time Vendors
---
+ One-time Customers (CZZZ-999999999)

    
    Benefits:
    Using one-time customer functionality helps streamline the sales process for occasional transactions while minimizing unnecessary data entry.
+ 

### License

mit

Copyright (c) 2025-present, Cloud Engineering and Services Company Limited
