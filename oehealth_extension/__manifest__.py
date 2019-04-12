##############################################################################
#    Copyright (C) 2018 oeHealth. All Rights Reserved
#    EHA Clinic Extensions to oeHealth, Hospital Management Solutions


{
    'name': 'oeHealth Extension',
    'version': '1.4',
    'author': "Ehealth Africa / Braincrew Apps(Migrated to Odoo 12)",
    'category': 'Generic Modules/Medical',
    'summary': 'Ehealth Africa extensions to Odoo 12 Hospital Management Solutions',
    'depends': ['base', 'sale', 'purchase', 'account', 'product','document','hr','web', 'account','oehealth', 'mail', 'helpdesk'],
    
    'description': "EHA Clinic extensions to the oehealth Module",
    "website": "https://erp.eha.ng",
    "data": [

        'security/oeh_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.xml',        

        #'sequence/oeh_sequence.xml',
        'oeh_navigation.xml',

        #'oeha_calllog/views/oeh_medical_calllog_view.xml',
        'oeha_insurance/views/oeha_insurance.xml',
        'oeha_symptom/views/oeha_medical_symptom.xml',
        #'oeha_imaging/views/report_patient_imagingtest.xml',
        #'oeha_imaging/reports/oeh_medical_imaging_report.xml',
        #'oeha_imaging/views/oeh_medical_imaging_view.xml',
        'oeha_lab/views/oeha_medical_lab_view.xml',
        'oeha_lab/reports/oeha_medical_label_report_view.xml',
        'oeha_patient/views/oeha_patient_view.xml',
        'oeha_evaluation/views/oeha_medical_evaluation_view.xml',
        'oeha_helpdesk/data/helpdesk_groups.xml',
        'oeha_helpdesk/views/oeha_helpdesk_view.xml',
        'oeha_appointment/views/oeha_appointment_view.xml',
        'oeha_accounting/views/oeha_invoice.xml',

    ],
    "images": ['images/main_screenshot.png'],
    "demo": [

    ],
    'test':[
    ],
    'css': [],
    'js': [

    ],
    'qweb': [

    ],
    "active": False
}