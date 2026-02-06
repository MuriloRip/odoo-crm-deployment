from odoo import models, fields, api

class NonClientTransaction(models.Model):
    _name = 'non.client.transaction'
    _description = 'Transação de Contato Externo'
    _order = 'date desc'

    name = fields.Char(string='Descrição', required=True)
    transaction_type = fields.Selection([
        ('gain', 'Ganho'),
        ('cost', 'Custo')
    ], string='Tipo', required=True, default='gain')
    
    amount = fields.Float(string='Valor', required=True)
    date = fields.Date(string='Data', default=fields.Date.context_today)
    partner_id = fields.Many2one('res.partner', string='Contato', required=True, ondelete='cascade')
    
    status = fields.Selection([
        ('pending', 'Pendente'),
        ('paid', 'Liquidado/Pago')
    ], string='Status', default='pending')

    notes = fields.Text(string='Observações da Transação')
