// Copyright (c) 2024, Usama and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Therapy Plan Details"] = {
	"filters": [
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "Not Started\nIn Progress\nCompleted\nCancelled",
			"default": "In Progress",
		}

	],
	"formatter": function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (column.fieldname == "status" && data && data.status == "Not Started") {
			value = "<span style='color:red'>" + value + "</span>";
		}
		else if (column.fieldname == "status" && data && data.status == "Completed") {
			value = "<span style='color:green'>" + value + "</span>";
		}
		else if (column.fieldname == "status" && data && data.status == "In Progress") {
			value = "<span style='color:orange'>" + value + "</span>";
		}
		else if (column.fieldname == "status" && data && data.status == "Cancelled") {
			value = "<span style='color:orange'>" + value + "</span>";
		}

		if (column.fieldname == "total_sessions" && data){
			value = "<span style='padding-right: 48px'>" + value + "</span>";
		}

		if (column.fieldname == "total_sessions_completed" && data){
			value = "<span style='padding-right: 68px'>" + value + "</span>";
		}

		return value;
	},
};
