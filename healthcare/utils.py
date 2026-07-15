import frappe
from frappe.utils.user import is_website_user


def check_app_permission():
	if frappe.session.user == "Administrator":
		return True

	if is_website_user():
		return False

	# Hide the app tile when its module is blocked for the user (e.g. via Module Profile)
	if "Healthcare" in frappe.get_cached_doc("User", frappe.session.user).get_blocked_modules():
		return False

	return True
