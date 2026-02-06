{
    'name': 'Controle Financeiro Customizado',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Controle simples de ganhos e gastos vinculado a contatos',
    'description': """
        - Registro de Ganhos (a receber) e Gastos (a pagar).
        - Vínculo direto com contatos (res.partner).
        - Visão unificada no cadastro da pessoa.
    """,
    'author': 'Manus',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/finance_transaction_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
