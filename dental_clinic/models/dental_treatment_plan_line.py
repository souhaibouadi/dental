# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DentalTreatmentPlanLine(models.Model):
    _name = 'dental.treatment.plan.line'
    _description = 'Treatment Plan Line'
    _order = 'sequence, id'

    sequence = fields.Integer(default=10)
    plan_id = fields.Many2one('dental.treatment.plan', required=True, ondelete='cascade')
    patient_id = fields.Many2one(related='plan_id.patient_id', store=True)
    practitioner_id = fields.Many2one('dental.practitioner')
    treatment_id = fields.Many2one('dental.treatment', required=True)
    tooth_id = fields.Many2one('dental.tooth', domain="[('patient_id', '=', patient_id)]")
    description = fields.Char()
    quantity = fields.Float(default=1.0)
    price_unit = fields.Float()
    discount = fields.Float(string='Disc. %', default=0.0)
    subtotal = fields.Float(compute='_compute_subtotal', store=True)
    state = fields.Selection([
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='planned')
    scheduled_date = fields.Date()
    invoiced = fields.Boolean(default=False, copy=False)
    note = fields.Text()
    currency_id = fields.Many2one(related='plan_id.currency_id', readonly=True)

    @api.onchange('treatment_id')
    def _onchange_treatment(self):
        if self.treatment_id:
            self.price_unit = self.treatment_id.price
            self.description = self.treatment_id.name

    @api.depends('quantity', 'price_unit', 'discount')
    def _compute_subtotal(self):
        for rec in self:
            price = rec.price_unit * (1 - (rec.discount or 0.0) / 100.0)
            rec.subtotal = rec.quantity * price
