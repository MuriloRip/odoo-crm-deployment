from odoo import models, fields, api

class NonClientTransaction(models.Model):
    _name = 'non.client.transaction'
    _description = 'Transação de Contato Externo'
    _order = 'date desc, id desc'

    name = fields.Char(string='Descrição/Referência', required=True, help="Ex: Venda de Sofá, Pagamento de Consultoria")
    transaction_type = fields.Selection([
        ('gain', 'Ganho/Entrada'),
        ('cost', 'Custo/Saída')
    ], string='Tipo de Lançamento', required=True, default='gain')
    
    amount = fields.Monetary(string='Valor', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Moeda', default=lambda self: self.env.company.currency_id)
    
    date = fields.Date(string='Data da Transação', default=fields.Date.context_today, required=True)
    partner_id = fields.Many2one('res.partner', string='Contato Relacionado', required=True, ondelete='cascade', domain=[('is_non_client', '=', True)])
    
    status = fields.Selection([
        ('pending', 'Pendente/Aberto'),
        ('paid', 'Liquidado/Pago')
    ], string='Situação', default='pending', required=True)

    notes = fields.Html(string='Observações Detalhadas')
