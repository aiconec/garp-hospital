<div align="center">
  <img src="healthcare/public/images/healthcare.svg" height="128" alt="GARP Health Logo">
  <h2>GARP Health</h2>
  <p align="center">
    <p>Open source & easy-to-use hospital information system (HIS) for all healthcare organisations.</p>
  </p>
</div>

### Introduction

GARP Health enables the health domain in GARP ERP and has various features that will help healthcare practitioners, clinics and hospitals to leverage the power of the GARP platform. It is built on the GARP Framework, a full-stack, meta-data driven, web framework, and integrates seamlessly with GARP ERP. GARP Health helps to manage healthcare workflows efficiently and most of the design is based on HL7 FHIR (Fast Health Interoperability Resources).


### Key Features

Key feature sets include Patient management, Outpatient / Inpatient management, Clinical Procedures, Rehabilitation and Physiotherapy, Laboratory management etc. and supports configuring multiple Medical Code Standards. It allows mapping any healthcare facility as Service Units and specialities as Medical Departments.

By integrating with GARP ERP, features of the ERP can also be utilized to manage Pharmacy and supplies, Purchases, Human Resources, Accounts and Finance, Asset Management, Quality etc. Along with authentication and role based access permissions, RESTfullness, extensibility, responsiveness and other goodies, the framework also allows setting up Website, payment integration and Patient portal.


### Installation

Using bench, install the GARP Framework and GARP ERP first.

Once GARP ERP is installed, add the healthcare app to your bench by running

```sh
$ bench get-app https://github.com/aiconec/garp-hospital
```

After that, you can install the healthcare app on the required site by running

```sh
$ bench --site demo.com install-app healthcare
```


### License

GNU GPL V3. See [license.txt](license.txt) for more information.

Forked from [earthians/marley](https://github.com/earthians/marley).
