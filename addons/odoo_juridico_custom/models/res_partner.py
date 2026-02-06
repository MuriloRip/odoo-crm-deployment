from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    transaction_ids = fields.One2many('finance.transaction', 'partner_id', string='Histórico Financeiro Jurídico')
    
    total_honorarios = fields.Float(string='Total Honorários Pendentes', compute='_compute_legal_finance')
    total_despesas = fields.Float(string='Total Despesas Pendentes', compute='_compute_legal_finance')

    def _compute_legal_finance(self):
        for partner in self:
            transactions = partner.transaction_ids.filtered(lambda t: t.status == 'pending')
            partner.total_honorarios = sum(transactions.filtered(lambda t: t.transaction_type == 'honorario').mapped('amount'))
            partner.total_despesas = sum(transactions.filtered(lambda t: t.transaction_type in ['despesa', 'custas']).mapped('amount'))
