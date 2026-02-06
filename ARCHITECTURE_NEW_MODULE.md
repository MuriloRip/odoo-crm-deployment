# Arquitetura do Módulo: Gestão de Contatos e Transações (Não-Clientes)

## Objetivo
Criar uma seção no Odoo para gerenciar pessoas que não são necessariamente clientes (ex: compradores de móveis de escritório), permitindo o rastreamento de débitos/créditos e anotações compartilhadas baseadas em um ID único (Partner).

## Componentes

### 1. Modelos (Models)
*   **res.partner (Herança):**
    *   Adicionar um campo `is_non_client` (Boolean) para filtrar esses contatos.
    *   Adicionar um campo `shared_notes` (Text) que será sincronizado/visível em todas as instâncias do mesmo contato.
*   **non_client.transaction (Novo Modelo):**
    *   `partner_id`: Many2one para `res.partner`.
    *   `description`: Char (ex: "Venda de Sofá").
    *   `amount`: Float (Valor).
    *   `type`: Selection (Ganho, Custo).
    *   `status`: Selection (Pago, Pendente).
    *   `date`: Date.

### 2. Interface (Views)
*   **Menu Principal:** Nova entrada no menu superior chamada "Gestão de Contatos".
*   **Lista/Kanban:** Visualização dos contatos não-clientes.
*   **Formulário:**
    *   Dados básicos do contato.
    *   Aba "Transações" para registrar ganhos e custos.
    *   Aba "Anotações Compartilhadas" com o campo de texto grande.

### 3. Lógica de Sincronização
Como o usuário mencionou "mesmo ID", no Odoo o `res.partner` já é o ID único. Se múltiplos usuários acessarem o mesmo registro de Partner, eles verão as mesmas `shared_notes`. Se o usuário se referia a "contatos diferentes com o mesmo nome/documento", a lógica de negócio deve garantir que eles apontem para o mesmo registro ou que as notas sejam copiadas, mas a melhor prática no Odoo é centralizar no `res.partner`.

## Estrutura de Arquivos (Plugin)
O novo módulo será chamado `odoo_non_client_management`.
- `models/res_partner.py`
- `models/non_client_transaction.py`
- `views/res_partner_views.xml`
- `views/transaction_views.xml`
- `views/menus.xml`
- `security/ir.model.access.csv`
- `__manifest__.py`
