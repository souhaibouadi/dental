# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class DentalPrescription(models.Model):
    _name = 'dental.prescription'
    _description = 'Dental Prescription'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc, id desc'

    name = fields.Char(required=True, readonly=True, copy=False, default=lambda s: _('New'), tracking=True)
    patient_id = fields.Many2one('dental.patient', required=True, tracking=True)
    practitioner_id = fields.Many2one('dental.practitioner', required=True, tracking=True)
    appointment_id = fields.Many2one('dental.appointment')
    date = fields.Date(default=fields.Date.context_today, required=True, tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled'),
    ], default='draft', tracking=True)
    line_ids = fields.One2many('dental.prescription.line', 'prescription_id', copy=True)
    diagnosis = fields.Text()
    advice = fields.Html(string='Advice / Posology')
    company_id = fields.Many2one('res.company', default=lambda s: s.env.company)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals.get('name') == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('dental.prescription') or _('New')
        return super().create(vals_list)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'cancel'

    def action_draft(self):
        self.state = 'draft'

    def action_print(self):
        return self.env.ref('dental_clinic.action_report_dental_prescription').report_action(self)
