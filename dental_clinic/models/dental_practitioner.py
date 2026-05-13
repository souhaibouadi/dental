# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DentalPractitioner(models.Model):
    _name = 'dental.practitioner'
    _description = 'Dental Practitioner / Dentist'
    _inherit = ['mail.thread']
    _order = 'name'

    name = fields.Char(required=True, tracking=True)
    user_id = fields.Many2one('res.users', string='Related User', tracking=True)
    image_1920 = fields.Image()
    speciality = fields.Selection([
        ('general', 'General Dentistry'),
        ('orthodontics', 'Orthodontics'),
        ('endodontics', 'Endodontics'),
        ('periodontics', 'Periodontics'),
        ('prosthodontics', 'Prosthodontics'),
        ('pedodontics', 'Pediatric Dentistry'),
        ('surgery', 'Oral Surgery'),
        ('implantology', 'Implantology'),
        ('hygienist', 'Dental Hygienist'),
    ], default='general', required=True, tracking=True)
    license_number = fields.Char(tracking=True)
    phone = fields.Char()
    email = fields.Char()
    color = fields.Integer(string='Calendar Color')
    notes = fields.Text()
    active = fields.Boolean(default=True)

    appointment_ids = fields.One2many('dental.appointment', 'practitioner_id')
    appointment_count = fields.Integer(compute='_compute_count')

    def _compute_count(self):
        for rec in self:
            rec.appointment_count = len(rec.appointment_ids)
