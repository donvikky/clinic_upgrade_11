##############################################################################
#    Copyright (C) 2018 eHealth Africa. All Rights Reserved
#    EHA Clinic Extensions to Payroll Module


{
    'name': 'EHA Clinic Payroll Extension',
    'version': '1.0',
    'author': "Ehealth Africa",
    'category': 'Generic Modules/Medical',
    'summary': 'Ehealth Africa extensions to Odoo 11 Payroll module',
    'depends': ['base', 'hr_payroll'],
    
    'description': "EHA Clinic extensions to the Odoo 11 Payroll Module",
    "website": "https://www.eha.ng",
    "data": [
        'data/payroll_rule.xml',
        'views/hr_payslip.xml'
    ],
    "images": [],
    "demo": [

    ],
    'test':[
    ],
    'css': [],
    'js': [

    ],
    'qweb': [

    ],
    
}