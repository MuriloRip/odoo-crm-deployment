{
    'name': 'Gestão de Contatos e Transações Externas',
    'version': '1.2',
    'category': 'Sales/CRM',
    'summary': 'Gerenciamento de contatos, transações financeiras e anotações compartilhadas por ID',
    'description': """
        Módulo customizado para Araújo & França Advocacia:
        - Gestão de contatos que não são clientes formais.
        - Rastreamento de Ganhos e Custos avulsos.
        - Anotações ricas (HTML) sincronizadas pelo ID do contato.
        - Integração visual com CRM e Calendário.
    """,
    'author': 'Manus AI',
    'depends': ['base', 'contacts', 'crm', 'calendar'],
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
