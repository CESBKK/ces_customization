'''
Available variables for use in custom naming serie:

from ERPNext:
Base on current transactional date.
.YYYY.
.YY.
.MM.
.DD.
.WW.
.FY.
.{fieldname}.

from ERPNext Thailand:
Base on posting date or document date or transactional date.
.YYYY-DATE.
.YY-DATE.
.MM-DATE.
.DD-DATE.
.WW-DATE.

From CES Customization:
Base on posting date or document date or transactional date.
.CES-YY.
.CES-YYYY.
.CES-YY-BE.
.CES-YYYY-BE.
.CES-WW.
.CES-MM.
.CES-DD.
.CES-YYYYMM.
.CES-YYMM.
.CES-YYYYMM-BE.
.CES-YYMM-BE.
.CES-PMT-TYPE.  - Special for payment_type field or Payment Entry DocType.
.CES-JV-TYPE.   - Special for entry_type field or Journal Entry DocType.
.CES-COM-ABBR.  - Company's Abbreviate

'''


DOCTYPE_NAMING_SERIES = {
    "Asset": [
        {
            "default": "ACC-ASS-.YYYY.-",
            "ces_custom": "ACC-ASS-.CES-YYMM-BE.-",
        },
    ],
    "Asset Capitalization": [
        {
            "default": "ACC-ASC-.YYYY.-",
            "ces_custom": "ACC-ASC-.CES-YYMM-BE.-",
        },
    ],
    "Asset Depreciation Schedule": [
        {
            "default": "ACC-ADS-.YYYY.-",
            "ces_custom": "ACC-ADS-.CES-YYMM-BE.-",
        },
    ],
    "Asset Maintenance Log": [
        {
            "default": "ACC-AML-.YYYY.-",
            "ces_custom": "ACC-AML-.CES-YYYY-BE.-",
        },
    ],
    "Asset Repair": [
        {
            "default": "ACC-ASR-.YYYY.-",
            "ces_custom": "ACC-ASR-.CES-YYYY-BE.-",
        },
    ],
    "Blanket Order": [
        {
            "default": "MFG-BLR-.YYYY.-",
            "ces_custom": "MFG-BLR-.CES-YYMM-BE.-",
        },
    ],
    "Campaign": [
        {
            "default": "SAL-CAM-.YYYY.-",
            "ces_custom": "SAL-CAM-.CES-YYMM-BE.-",
        },
    ],
    "Customer": [
        {
            "default": "CUST-.YYYY.-",
            "ces_custom": "CUST-.CES-YYMM-BE.-",
        },
    ],
    "Delivery Note": [
        {
            "default": "MAT-DN-.YYYY.-\nMAT-DN-RET-.YYYY.-",
            "ces_custom": "MAT-DN-.CES-YYMM-BE.-\nMAT-DN-RET-.CES-YYMM-BE.-",
        },
    ],
    "Delivery Trip": [
        {
            "default": "MAT-DT-.YYYY.-",
            "ces_custom": "MAT-DT-.CES-YYMM-BE.-",
        },
    ],
    "Driver": [
        {
            "default": "HR-DRI-.YYYY.-",
            "ces_custom": "HR-DRI-.CES-YYMM-BE.-",
        },
    ],
    "Dunning": [
        {
            "default": "DUNN-.MM.-.YY.-",
            "ces_custom": "DUNN-.CES-YYMM-BE.-",
        },
    ],
    "Employee": [
        {
            "default": "HR-EMP-",
            "ces_custom": "HR-EMP-.CES-YY-BE.",
        },
    ],
    "Item": [
        {
            "default": "STO-ITEM-.YYYY.-",
            "ces_custom": "STO-ITEM-.CES-YY-BE.",
        },
    ],
    "Journal Entry": [
        {
            "default": "ACC-JV-.YYYY.-",
            "ces_custom": "ACC-JV-.CES-JV-TYPE.CES-YYMM-BE.-",
        },
    ],
    "POS Invoice": [
        {
            "default": "ACC-PSINV-.YYYY.-",
            "ces_custom": "ACC-PSINV-.CES-YYMM-BE.-",
        },
    ],
    "Packing Slip": [
        {
            "default": "MAT-PAC-.YYYY.-",
            "ces_custom": "MAT-PAC-.CES-YYMM-BE.-",
        },
    ],
    "Payment Entry": [
        {
            "default": "ACC-PAY-.YYYY.-",
            "ces_custom": "ACC-.CES-PMT-TYPE.-.CES-YYMM-BE.-",
        },
    ],
    "Payment Request": [
        {
            "default": "ACC-PRQ-.YYYY.-",
            "ces_custom": "ACC-PRQ-.CES-YYMM-BE.-",
        },
    ],
    "Pick List": [
        {
            "default": "STO-PICK-.YYYY.-",
            "ces_custom": "STO-PICK-.CES-YYMM-BE.-",
        },
    ],
    "Project Update": [
        {
            "default": "PROJ-UPD-.YYYY.-",
            "ces_custom": "PROJ-UPD-.CES-YYMM-BE.-",
        },
    ],
    "Purchase Invoice": [
        {
            "default": "ACC-PINV-.YYYY.-\nACC-PINV-RET-.YYYY.-",
            "ces_custom": "ACC-PINV-.CES-YYMM-BE.-\nACC-PINV-RET-.CES-YYMM-BE.-",
        },
    ],
    "Purchase Order": [
        {
            "default": "PUR-ORD-.YYYY.-",
            "ces_custom": ".CES-COM-ABBR.-PO-.CES-YYMM-BE.-",
        },
    ],
    "Purchase Receipt": [
        {
            "default": "MAT-PRE-.YYYY.-\nMAT-PR-RET-.YYYY.-",
            "ces_custom": "MAT-CES-YYMM-BE-.YYYY.-\nMAT-PRE-RET-.CES-YYMM-BE.-",
        },
    ],
    "Quality Inspection": [
        {
            "default": "MAT-QA-.YYYY.-",
            "ces_custom": "MAT-QA-.CES-YYMM-BE.-",
        },
    ],
    "Quotation": [
        {
            "default": "SAL-QTN-.YYYY.-",
            "ces_custom": ".CES-COM-ABBR.-QTN-.CES-YYMM-BE.-",
        },
    ],
    "Request for Quotation": [
        {
            "default": "PUR-RFQ-.YYYY.-",
            "ces_custom": ".CES-COM-ABBR.-RFQ-.CES-YYMM-BE.-",
        },
    ],
    "Sales Invoice": [
        {
            "default": "ACC-SINV-.YYYY.-\nACC-SINV-RET-.YYYY.-",
            "ces_custom": ".CES-COM-ABBR.-INV-.CES-YYMM-BE.-\n.CES-COM-ABBR.-INV-RET-.CES-YYMM-BE.-",
        },
    ],
    "Sales Order": [
        {
            "default": "SAL-ORD-.YYYY.-",
            "ces_custom": "SAL-ORD-.CES-YYMM-BE.-",
        },
    ],
    "Shareholder": [
        {
            "default": "ACC-SH-.YYYY.-",
            "ces_custom": ".CES-COM-ABBR.-SH-",
        },
    ],
    "Stock Entry": [
        {
            "default": "MAT-STE-.YYYY.-",
            "ces_custom": "MAT-STE-.CES-YYMM-BE.-",
        },
    ],
    "Stock Reconciliation": [
        {
            "default": "MAT-RECO-.YYYY.-",
            "ces_custom": "MAT-RECO-.CES-YYMM-BE.-",
        },
    ],
    "Subcontracting Order": [
        {
            "default": "SC-ORD-.YYYY.-",
            "ces_custom": "MAT-RECO-.CES-YYMM-BE.-",
        },
    ],
    "Subcontracting Receipt": [
        {
            "default": "MAT-SCR-.YYYY.-\nMAT-SCR-RET-.YYYY.-",
            "ces_custom": "MAT-SCR-.CES-YYMM-BE.-\nMAT-SCR-RET-.CES-YYMM-BE.-",
        },
    ],
    "Supplier": [
        {
            "default": "SUP-.YYYY.-",
            "ces_custom": "SUP-.CES-YYMM-BE.-",
        },
    ],
    "Supplier Quotation": [
        {
            "default": "SUP-.YYYY.-",
            "ces_custom": "SUP-.CES-YYMM-BE.-",
        },
    ],
    "Supplier Scorecard Period": [
        {
            "default": "PU-SSP-.YYYY.-",
            "ces_custom": "PUR-SSP-.CES-YY-BE.-",
        },
    ],
    "Timesheet": [
        {
            "default": "TS-.YYYY.-",
            "ces_custom": "TS-.CES-YYYY-BE.-",
        },
    ],
    "Warranty Claim": [
        {
            "default": "SER-WRN-.YYYY.-",
            "ces_custom": "SER-WRN-.CES-YYYY-BE.-",
        },
    ],
    "Work Order": [
        {
            "default": "MFG-WO-.YYYY.-",
            "ces_custom": "MFG-WO-.CES-YYMM-BE.-",
        },
    ],
}
