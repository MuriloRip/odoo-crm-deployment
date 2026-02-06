{
    'name': 'Gestão de Contatos Não-Clientes',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Gerenciamento de contatos externos, transações e anotações compartilhadas',
    'description': """
        Este módulo permite gerenciar pessoas que não são necessariamente clientes:
        - Rastreamento de pagamentos (Ganhos e Custos).
        - Anotações compartilhadas vinculadas ao contato.
        - Interface simplificada e separada do CRM principal.
    """,
    'author': 'Manus',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/transaction_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
