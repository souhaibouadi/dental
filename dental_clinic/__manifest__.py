# -*- coding: utf-8 -*-
{
    'name': 'Dental Clinic Management',
    'version': '17.0.1.0.0',
    'category': 'Healthcare',
    'summary': 'Complete dental clinic management: patients, appointments, treatments, odontogram, prescriptions, billing.',
    'description': """
Dental Clinic Management for Odoo 17
=====================================
Features:
  * Patient files with medical history and allergies
  * Practitioners and rooms / dental chairs
  * Appointment scheduling (calendar / gantt-like)
  * Treatment catalog (services) and treatment plans
  * Interactive odontogram (32 teeth) with tooth conditions
  * Prescriptions with printable PDF
  * Native integration with Odoo Invoicing (no insurance)
  * Security groups (Receptionist / User / Manager)
  * Demo data ready to test
""",
    'author': 'souhaibouadi',
    'website': 'https://github.com/souhaibouadi/dental',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
        'contacts',
        'product',
        'account',
        'calendar',
    ],
    'data': [
        # security
        'security/dental_security.xml',
        'security/ir.model.access.csv',
        # data
        'data/ir_sequence_data.xml',
        'data/dental_tooth_data.xml',
        'data/mail_template_data.xml',
        # reports
        'report/report_paperformat.xml',
        'report/dental_reports.xml',
        'report/dental_prescription_template.xml',
        'report/dental_treatment_plan_template.xml',
        'report/dental_patient_card_template.xml',
        # views
        'views/dental_menus.xml',
        'views/res_partner_views.xml',
        'views/dental_patient_views.xml',
        'views/dental_practitioner_views.xml',
        'views/dental_room_views.xml',
        'views/dental_treatment_views.xml',
        'views/dental_appointment_views.xml',
        'views/dental_treatment_plan_views.xml',
        'views/dental_tooth_views.xml',
        'views/dental_prescription_views.xml',
        # wizards
        'wizards/dental_invoice_wizard_views.xml',
    ],
    'demo': [
        'demo/dental_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dental_clinic/static/src/css/odontogram.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
