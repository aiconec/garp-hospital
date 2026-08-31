import click

import frappe

import healthcare


def before_install():
	def major_version(v: str) -> str:
		return v.split(".")[0]

	frappe_version = major_version(frappe.__version__)
	healthcare_version = major_version(healthcare.__version__)

	if frappe_version == healthcare_version:
		return

	click.secho(
		f"You're attempting to install GARP Health develop branch on GARP ERP version {frappe_version}."
		"This is not supported and will result in broken install. Switch to correct branch before installing.",
		fg="red",
	)

	raise SystemExit(1)
