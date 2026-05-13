# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    dental_patient_id = fields.Many2one('dental.patient', string='Dental Patient', index=True)
    dental_plan_id = fields.Many2one('dental.treatment.plan', string='Treatment Plan', index=True)
