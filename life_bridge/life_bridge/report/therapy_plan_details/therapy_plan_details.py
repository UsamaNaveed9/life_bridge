# Copyright (c) 2024, Usama and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):

	columns = get_columns()

	data = get_data(filters)

	return columns, data


def get_columns():
	return [
		{
			"label": _("Therapy Plan"),
			"fieldtype": "Link",
			"fieldname": "name",
			"options": "Therapy Plan",
			"width": 200,
		},
		{
			"label": _("Patient"),
			"fieldtype": "Link",
			"fieldname": "patient",
			"options": "Patient",
			"width": 200,
		},
		{"label": _("Patient Name"), "fieldtype": "data", "fieldname": "patient_name", "width": 200},
		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "status",
			"width": 100,
		},
		{
			"label": _("Start Date"),
			"fieldtype": "Date",
			"fieldname": "start_date",
			"width": 100,
		},
		{
			"label": _("Total Sessions"),
			"fieldtype": "Data",
			"fieldname": "total_sessions",
			"width": 120,
		},
		{
			"label": _("Completed Sessions"),
			"fieldtype": "Data",
			"fieldname": "total_sessions_completed",
			"width": 160,
		},
	]


def get_data(filters):
	if filters.status:
		therapy_plans = frappe.get_all(
			"Therapy Plan",
			filters=[["status","=",filters.status]],
			fields=["name", "patient", "patient_name", "status","start_date",
					"total_sessions","total_sessions_completed"]  
		)

	return therapy_plans