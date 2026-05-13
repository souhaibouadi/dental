# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class DentalInvoiceWizard(models.TransientModel):
    _name = 'dental.invoice.wizard'
    _description = 'Create Invoice from Treatment Plan'

    plan_id = fields.Many2one('dental.treatment.plan', required=True)
    patient_id = fields.Many2one('dental.patient', required=True)
    line_ids = fields.Many2many('dental.treatment.plan.line', string='Lines to Invoice')
    journal_id = fields.Many2one(
        'account.journal', required=True,
        domain=[('type', '=', 'sale')],
        default=lambda s: s.env['account.journal'].search([('type','=','sale'), ('company_id','=', s.env.company.id)], limit=1),
    )
    invoice_date = fields.Date(default=fields.Date.context_today, required=True)

    @api.onchange('plan_id')
    def _onchange_plan(self):
        if self.plan_id:
            self.line_ids = self.plan_id.line_ids.filtered(lambda l: not l.invoiced and l.state != 'cancel')

    def action_create_invoice(self):
        self.ensure_one()
        if not self.line_ids:
            raise UserError(_('No lines selected to invoice.'))
        if not self.patient_id.partner_id:
            raise UserError(_('Patient has no related contact.'))
        invoice_lines = []
        for line in self.line_ids:
            product = line.treatment_id.product_id
            if not product:
                raise UserError(_('Treatment "%s" has no linked product.') % line.treatment_id.name)
            invoice_lines.append((0, 0, {
                'product_id': product.id,
                'name': line.description or line.treatment_id.name,
                'quantity': line.quantity,
                'price_unit': line.price_unit,
                'discount': line.discount,
            }))
        move = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.patient_id.partner_id.id,
            'invoice_date': self.invoice_date,
            'journal_id': self.journal_id.id,
            'dental_patient_id': self.patient_id.id,
            'dental_plan_id': self.plan_id.id,
            'invoice_line_ids': invoice_lines,
        })
        self.line_ids.write({'invoiced': True})
        self.plan_id.invoice_ids = [(4, move.id)]
        return {
            'type': 'ir.actions.act_window',
            'name': _('Invoice'),
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': move.id,
        }
