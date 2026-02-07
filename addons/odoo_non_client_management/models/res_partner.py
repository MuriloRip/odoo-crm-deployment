from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_non_client = fields.Boolean(string='É Contato Externo', default=False)
    shared_notes = fields.Html(string='Anotações Compartilhadas (ID Único)', help='Anotações ricas que aparecem para todos os usuários que acessarem este contato.')
    last_interaction_date = fields.Date(string='Última Interação', compute='_compute_last_interaction', store=True)

    @api.depends('non_client_transaction_ids.date')
    def _compute_last_interaction(self):
        for partner in self:
            if partner.non_client_transaction_ids:
                partner.last_interaction_date = max(partner.non_client_transaction_ids.mapped('date'))
            else:
                partner.last_interaction_date = False
    
    non_client_transaction_ids = fields.One2many('non.client.transaction', 'partner_id', string='Transações de Contato Externo')
    
    total_gains = fields.Float(string='Total Ganhos', compute='_compute_transactions_totals')
    total_costs = fields.Float(string='Total Custos', compute='_compute_transactions_totals')
    balance = fields.Float(string='Saldo', compute='_compute_transactions_totals')

    def _compute_transactions_totals(self):
        for partner in self:
            transactions = partner.non_client_transaction_ids
            gains = sum(transactions.filtered(lambda t: t.transaction_type == 'gain').mapped('amount'))
            costs = sum(transactions.filtered(lambda t: t.transaction_type == 'cost').mapped('amount'))
            partner.total_gains = gains
            partner.total_costs = costs
            partner.balance = gains - costs
