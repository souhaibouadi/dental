# -*- coding: utf-8 -*-
from odoo import fields, models


class DentalMedicalHistory(models.Model):
    _name = 'dental.medical.history'
    _description = 'Patient Medical History Entry'
    _order = 'date desc, id desc'

    patient_id = fields.Many2one('dental.patient', required=True, ondelete='cascade')
    date = fields.Date(default=fields.Date.context_today, required=True)
    title = fields.Char(required=True)
    description = fields.Text()
    practitioner_id = fields.Many2one('dental.practitioner', string='Practitioner')
    kind = fields.Selection([
        ('disease', 'Disease'),
        ('surgery', 'Surgery'),
        ('allergy', 'Allergy'),
        ('medication', 'Medication'),
        ('other', 'Other'),
    ], default='disease', required=True)
