import frappe


def execute():
	get_all_bundles = frappe.get_all("Product Bundle", filters={"docstatus": 0}, fields=["name"])
	if get_all_bundles:
		for bundle in get_all_bundles:
			try:
				bundle_doc = frappe.get_doc("Product Bundle", bundle.name)
				bundle_doc.submit()
			except Exception as e:
				frappe.log_error(f"Failed to submit Product Bundle {bundle.name}", f"Patch Error: {e}")
