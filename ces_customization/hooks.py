app_name = "ces_customization"
app_title = "CES Customization"
app_publisher = "Cloud Engineering and Services Co.,Ltd."
app_description = "Customization for Thailand"
app_email = "cescoltdbkk@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []
required_apps = ["erpnext"]
# required_apps = ["erpnext", "erpnext_thailand"]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ces_customization",
# 		"logo": "/assets/ces_customization/logo.png",
# 		"title": "CES Customization",
# 		"route": "/ces_customization",
# 		"has_permission": "ces_customization.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ces_customization/css/ces_customization.css"
# app_include_js = "/assets/ces_customization/js/ces_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/ces_customization/css/ces_customization.css"
# web_include_js = "/assets/ces_customization/js/ces_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ces_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}
# webform_include_js = {"Journal Entry": "public/js/journal_entry.js"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Journal Entry": "public/js/journal_entry.js",
    "Payment Entry": "public/js/payment_entry.js",
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ces_customization/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ces_customization.utils.jinja_methods",
# 	"filters": "ces_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ces_customization.install.before_install"
# after_install = "ces_customization.install.after_install"
after_install = "ces_customization.setup.install.after_install"
after_app_install = "ces_customization.setup.install.after_app_install"

# Uninstallation
# ------------

# before_uninstall = "ces_customization.uninstall.before_uninstall"
# after_uninstall = "ces_customization.uninstall.after_uninstall"
before_uninstall = "ces_customization.setup.uninstall.before_uninstall"
before_app_uninstall = "ces_customization.setup.uninstall.before_app_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ces_customization.utils.before_app_install"
# after_app_install = "ces_customization.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ces_customization.utils.before_app_uninstall"
# after_app_uninstall = "ces_customization.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = ces_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

override_doctype_class = {
    "Journal Entry": "ces_customization.overrides.journal_entry.ces_JournalEntry",
    "Payment Entry": "ces_customization.overrides.payment_entry.ces_PaymentEntry",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "Quotation": {
        "on_trash": "ces_customization.custom.sales.on_trash",
    },
    "Sales Order": {
        "on_trash": "ces_customization.custom.sales.on_trash",
    },
    "Sales Invoice": {
        "on_trash": "ces_customization.custom.sales.on_trash",
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ces_customization.tasks.all"
# 	],
# 	"daily": [
# 		"ces_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"ces_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ces_customization.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ces_customization.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ces_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events":
# 		"ces_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ces_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ces_customization.utils.before_request"]
# after_request = ["ces_customization.utils.after_request"]

# Job Events
# ----------
# before_job = ["ces_customization.utils.before_job"]
# after_job = ["ces_customization.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ces_customization.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# function should expect the variable and doc as arguments
naming_series_variables = {
    "CES-YY": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-YYYY": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-YY-BE": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-YYYY-BE": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-WW": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-MM": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-DD": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-YYYYMM": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-YYMM": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-YYYYMM-BE": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-YYMM-BE": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-PMT-TYPE": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-JV-TYPE": "ces_customization.custom.naming.parse_naming_series_variable",
    "CES-COM-ABBR": "ces_customization.custom.naming.parse_naming_series_variable",
}

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["fieldname", "like", "ces%"]]
    },
    {
        "dt": "Bank"
    },
]
