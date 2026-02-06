{
    'name': 'Odoo Jurídico Customizado',
    'version': '1.1',
    'category': 'Legal',
    'summary': 'Plugin modular para CRM Jurídico: Notas, WhatsApp, Processos e Financeiro',
    'description': """
        Este módulo funciona como um plugin independente para o Odoo:
        - Customiza o CRM para o fluxo jurídico.
        - Adiciona campos de Processo e Tribunal.
        - Integra WhatsApp direto nos cards.
        - Simplifica a interface removendo funções de varejo.
        - Controle financeiro de honorários e despesas.
    """,
    'author': 'Manus',
    'depends': ['crm', 'contacts', 'phone_validation'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/res_partner_views.xml',
        'views/finance_views.xml',
        'views/menu_simplification.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
