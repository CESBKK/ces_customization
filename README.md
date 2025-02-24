# CES Customization

Customization for Thailand

By installing ces_customization, it provides access to additional naming series variables and UOM from Thailand Goverment's standard and a couple of neat tweaks.  Here are a list of available fucntions:

1. [Custom Virtual DocField](#virtual)
2. [Additional Naming Series Variable](#naming_series_variable)
3. [Document Naming Series](#naming_series)
4. [Thailand's GFMIS Unit of Measurements](#gfmis_uoms)
5. [One-time Customers and One-time Vendors](#onetime)

### <a name="install"></a>Installation
---
In your ```bench``` directory:

```
bench get-app https://github.com/CESBKK/ces_customization
```
Before installation please customize your document naming seiries locate in:
```
cd ./apps/ces_customization/ces_customization/setup/data
```
The following files contain customization for each apps:
```
naming_series_data_erpnext.json
naming_series_data_hrms.json
naming_series_data_erpnext_thailand.json
```
**To install:**
```
bench --site <<site-name>> install-app ces_customization
```
**To uninstall:**
```
bench --site <<site-name>> uninstall-app ces_customization
```

<div style="text-align: right;">
<a href="#">Back to top</a>
</div>

### <a name="virtual"></a>Custom Virtual DocField
---
Mostly date related currently available for Payment Entry and Journal Entry DocType.

<div style="text-align: right;">
<a href="#">Back to top</a>
</div>

### <a name="naming_series_variable"></a>Naming Series Variables:
---
#### From CES Customization:

Base on posting date or document date or transactional date. Varibale with BE will return year in Bhudist Era or AD+543.  CES variables also can be used in naming expression for Auto Name by putting them in {-} e.g. format:CUST-{CES-YYMM-BE}{#####}
- ```.CES-YY.```
- ```.CES-YYYY.```
- ```.CES-YY-BE.```
- ```.CES-YYYY-BE.```
- ```.CES-WW.```
- ```.CES-MM.```
- ```.CES-DD.```
- ```.CES-YYYYMM.```
- ```.CES-YYMM.```
- ```.CES-YYYYMM-BE.```
- ```.CES-YYMM-BE.```
- ```.CES-PMT-TYPE.```  - Special for payment_type field or Payment Entry DocType.
- ```.CES-JV-TYPE.```   - Special for entry_type field or Journal Entry DocType.
- ```.CES-COM-ABBR.```  - Company's Abbreviated Name

#### From ERPNext:

Base on current transactional date.
- ```.YYYY.```
- ```.YY.```
- ```.MM.```
- ```.DD.```
- ```.WW.```
- ```.FY.```
- ```.{fieldname}.```

#### From [ERPNext Thailand](https://github.com/ecosoft-frappe/erpnext_thailand):

Base on posting date or document date or transactional date.
- ```.YYYY-DATE.```
- ```.YY-DATE.```
- ```.MM-DATE.```
- ```.DD-DATE.```
- ```.WW-DATE.```

### <a name="naming_series"></a>Document Naming Series
---
This app provide custom naming series for varioud DocType in the following app:
+ ERPNext
+ HRMS
+ ERPNext_Thailand

Before [installation](#install) you can edit ```ces_custom``` field in json data file for your liking.

<div style="text-align: right;">
<a href="#">Back to top</a>
</div>

### <a name="gfmis_uoms"></a>UOMs from Thailand's GFMIS
---
Add Thai UOMs based on goverment's standard หน่วยนับที่ใช้สำหรับจัดทำใบสั่งซื้อ บส.01 ในระบบ GFMIS

Note: UOMs are imported only. No uninstallation when app uninstalled.

<div style="text-align: right;">
<a href="#">Back to top</a>
</div>

### <a name="onetime"></a>One-time Customers and One-time Vendors
---
This app creates One dummy customer and One dummy supplier.
+ One-time Customer (CZZZ-999999999)

    A customer with whom a company only conducts a single business transaction, meaning they are not expected to make repeat purchases and therefore do not require a full, detailed customer master record in the system; their information is entered directly into the sales order when needed, usually using a designated "one-time customer"
    
    **Benefits:**

    Using one-time customer functionality helps streamline the sales process for occasional transactions while minimizing unnecessary data entry.

+ One-time Vendor (SZZZ-999999999)

    A supplier that a company only does business with once, meaning they will only purchase goods or services from that vendor on a single occasion and do not plan to make future purchases from them.

    **Usage Scenarios:**

    Expense claim from Vendor during travelling trip.  Procuring a very special goods or services once in the blue moon especially those without VAT related.

<div style="text-align: right;">
<a href="#">Back to top</a>
</div>

### License

mit

Copyright (c) 2025, Cloud Engineering and Services Company Limited
