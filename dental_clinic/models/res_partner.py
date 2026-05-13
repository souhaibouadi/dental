# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_dental_patient = fields.Boolean(string='Is Dental Patient')
    dental_patient_id = fields.One2many('dental.patient', 'partner_id', string='Patient Record')
