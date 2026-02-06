from odoo import models, fields, api

class FinanceTransaction(models.Model):
    _name = 'finance.transaction'
    _description = 'Transação Financeira Jurídica'
    _order = 'date desc'

    name = fields.Char(string='Descrição/Serviço', required=True)
    transaction_type = fields.Selection([
        ('honorario', 'Honorários (A Receber)'),
        ('despesa', 'Despesa de Processo (A Pagar)'),
        ('custas', 'Custas Judiciais (A Pagar)')
    ], string='Tipo de Lançamento', required=True, default='honorario')
    
    amount = fields.Float(string='Valor', required=True)
    date = fields.Date(string='Data', default=fields.Date.context_today)
    partner_id = fields.Many2one('res.partner', string='Cliente/Parte', required=True)
    
    status = fields.Selection([
        ('pending', 'Pendente'),
        ('paid', 'Liquidado/Pago')
    ], string='Status', default='pending')

    notes = fields.Text(string='Observações do Caso')
