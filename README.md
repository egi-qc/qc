EGI Quality Criteria
====================

This repository contains the EGI Quality Criteria used for verification
of products in the [EGI Software Provision](https://wiki.egi.eu/wiki/EGI_Software_Provisioning)
workflow.

Each YAML file contains a list of criteria with the following fields:
* id: a unique id
* name: short name of the criterion
* critical: whether the criterion can mark the product as rejected
* desc: longer description of the criterion
* passfail: what the verifier should check
* report: what should be included in the verification report
* related (optional): pointers to relevant information for the criterion
* testing (optional): pointers to tests the criterion
* revision (optional): internal QC management history

## Rendering

The render subdirectory contains a simple python script for generating a HTML version of the 
criteria (it requires [Jinja2](http://jinja.pocoo.org/docs/) and [Markdown](http://pythonhosted.org/Markdown/) packages)
