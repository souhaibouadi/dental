# -*- coding: utf-8 -*-
from odoo import fields, models


class DentalRoom(models.Model):
    _name = 'dental.room'
    _description = 'Dental Room / Chair'
    _order = 'sequence, name'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    code = fields.Char()
    description = fields.Text()
    equipment = fields.Text(help='Equipment available in this room/chair.')
    active = fields.Boolean(default=True)
    color = fields.Integer()
