{
    'name': 'CRM Custom Notes and WhatsApp',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Customizações para o CRM: Notas, Prioridades e WhatsApp',
    'description': """
        - Adiciona campo de notas flexíveis no CRM.
        - Adiciona botão de WhatsApp no card do lead.
        - Adiciona sistema de prioridades customizado.
    """,
    'author': 'Manus',
    'depends': ['crm', 'phone_validation'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
