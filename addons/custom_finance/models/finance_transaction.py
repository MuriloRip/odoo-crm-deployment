from odoo import models, fields, api

class FinanceTransaction(models.Model):
    _name = 'finance.transaction'
    _description = 'Transação Financeira'
    _order = 'date desc'

    name = fields.Char(string='Descrição', required=True)
    transaction_type = fields.Selection([
        ('income', 'Ganho (A Receber)'),
        ('expense', 'Gasto (A Pagar)')
    ], string='Tipo', required=True, default='income')
    
    amount = fields.Float(string='Valor', required=True)
    date = fields.Date(string='Data', default=fields.Date.context_today)
    partner_id = fields.Many2one('res.partner', string='Pessoa/Contato', required=True)
    
    status = fields.Selection([
        ('pending', 'Pendente'),
        ('paid', 'Concluído/Pago')
    ], string='Status', default='pending')

    notes = fields.Text(string='Observações')
