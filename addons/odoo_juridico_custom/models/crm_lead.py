from odoo import models, fields, api
import urllib.parse

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Campos de Negociação (Notas)
    custom_notes = fields.Html(string='Notas de Negociação', help='Notas detalhadas sobre o cliente e a negociação.')
    
    # Campos Jurídicos Avançados
    process_number = fields.Char(string='Número do Processo')
    court_name = fields.Char(string='Tribunal/Vara')
    legal_area = fields.Selection([
        ('civil', 'Civil'),
        ('trabalhista', 'Trabalhista'),
        ('penal', 'Penal'),
        ('familia', 'Família'),
        ('tributario', 'Tributário'),
        ('outro', 'Outro')
    ], string='Área Jurídica')

    # Prioridades Customizadas
    custom_priority = fields.Selection([
        ('0', 'A conversar'),
        ('1', 'Interessado'),
        ('2', 'Urgente'),
        ('3', 'Processo em andamento'),
        ('4', 'Pendente')
    ], string='Prioridade Jurídica', default='0')

    # Integração WhatsApp
    whatsapp_url = fields.Char(string='WhatsApp URL', compute='_compute_whatsapp_url')

    @api.depends('mobile', 'phone')
    def _compute_whatsapp_url(self):
        for lead in self:
            number = lead.mobile or lead.phone
            if number:
                clean_number = "".join(filter(str.isdigit, number))
                if len(clean_number) <= 11:
                    clean_number = "55" + clean_number
                
                # Mensagem personalizada com contexto jurídico
                msg = f"Olá {lead.contact_name or lead.name}, aqui é do escritório de advocacia. Gostaria de falar sobre o seu caso."
                if lead.process_number:
                    msg += f" (Ref. Processo: {lead.process_number})"
                
                encoded_message = urllib.parse.quote(msg)
                lead.whatsapp_url = f"https://wa.me/{clean_number}?text={encoded_message}"
            else:
                lead.whatsapp_url = False
