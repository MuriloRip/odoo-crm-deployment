from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    transaction_ids = fields.One2many('finance.transaction', 'partner_id', string='Transações Financeiras')
    
    total_to_receive = fields.Float(string='Total a Receber', compute='_compute_finance_totals')
    total_to_pay = fields.Float(string='Total a Pagar', compute='_compute_finance_totals')

    def _compute_finance_totals(self):
        for partner in self:
            transactions = partner.transaction_ids.filtered(lambda t: t.status == 'pending')
            partner.total_to_receive = sum(transactions.filtered(lambda t: t.transaction_type == 'income').mapped('amount'))
            partner.total_to_pay = sum(transactions.filtered(lambda t: t.transaction_type == 'expense').mapped('amount'))
