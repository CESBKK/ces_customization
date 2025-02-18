### CES Customization

Customization for Thailand

## Available variables for use in custom naming serie:

from ERPNext:
Base on current transactional date.
- .YYYY.
- .YY.
- .MM.
- .DD.
- .WW.
- .FY.
- .{fieldname}.

from ERPNext Thailand:
Base on posting date or document date or transactional date.
- .YYYY-DATE.
- .YY-DATE.
- .MM-DATE.
- .DD-DATE.
- .WW-DATE.

From CES Customization:
Base on posting date or document date or transactional date.
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


## Add UOMs from Thailand's GFMIS

add Thai UOM หน่วยนับที่ใช้สำหรับจัดทำใบสั่งซื้อ บส.01 ในระบบ GFMIS
Except:
- CUP, DAY, KG - existed in erpnext default.
- HR. - already had 'H' for 'ชั่วโมง'

Note: UOMs are imported only. No uninstallation when app uninstalled.


#### License

mit