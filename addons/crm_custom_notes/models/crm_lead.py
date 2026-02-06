from odoo import models, fields, api
import urllib.parse

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    custom_notes = fields.Html(string='Notas de Negociação', help='Notas detalhadas sobre o cliente e a negociação.')
    
    custom_priority = fields.Selection([
        ('0', 'A conversar'),
        ('1', 'Interessado'),
        ('2', 'Urgente'),
        ('3', 'Processo em andamento'),
        ('4', 'Pendente')
    ], string='Prioridade Customizada', default='0')

    whatsapp_url = fields.Char(string='WhatsApp URL', compute='_compute_whatsapp_url')

    @api.depends('mobile', 'phone')
    def _compute_whatsapp_url(self):
        for lead in self:
            number = lead.mobile or lead.phone
            if number:
                # Limpar o número para deixar apenas dígitos
                clean_number = "".join(filter(str.isdigit, number))
                # Se não tiver o código do país, assume Brasil (55)
                if len(clean_number) <= 11:
                    clean_number = "55" + clean_number
                
                message = f"Olá {lead.contact_name or lead.name}, tudo bem?"
                encoded_message = urllib.parse.quote(message)
                lead.whatsapp_url = f"https://wa.me/{clean_number}?text={encoded_message}"
            else:
                lead.whatsapp_url = False
