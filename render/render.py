
from jinja2 import Environment, FileSystemLoader
from markdown import markdown
import os.path
import yaml


def markdown_filter(text, *args, **kwargs):
    return markdown(text, *args, **kwargs)

env = Environment(loader=FileSystemLoader('templates'))
env.filters['markdown'] = markdown_filter


release_id = '6'
intro_text = ("This page describes the 6th release of the EGI Quality "
              "Criteria (QC), that is used for verification of software "
              "products. These QC drive the Software Verification in "
              "[EGI Software Provision](https://wiki.egi.eu/wiki/"
              "EGI_Software_Provisioning) workflow.")
generic = [
    {
        'name': 'Documentation',
        'file': 'doc.yaml',
        'id': 'DOCUMENTATION',
    },
    {
        'name': 'Installation',
        'file': 'installation.yaml',
        'id': 'INSTALLATION',
    },
    {
        'name': 'Security',
        'file': 'security.yaml',
        'id': 'SECURITY',
    },
    {
        'name': 'Information Model',
        'file': 'info.yaml',
        'id': 'INFO_MODEL',
    },
    {
        'name': 'Operations',
        'file': 'operations.yaml',
        'id': 'OPERATIONS',
    },
    {
        'name': 'Support',
        'file': 'support.yaml',
        'id': 'SUPPORT',
    },
]

specific = [
    {
        'name': 'Specific QC',
        'file': 'specific.yaml',
        'id': 'SPECIFIC',
    },
]
QC_DIR = '../'


def load_criteria(d):
    for s in d:
        s_file = os.path.join(QC_DIR, s['file'])
        s['criteria'] = yaml.load(open(s_file).read())
    return d


template = env.get_template('base.html')
print template.render(generic=load_criteria(generic),
                      specific=load_criteria(specific),
                      release_id=release_id,
                      intro_text=intro_text)
