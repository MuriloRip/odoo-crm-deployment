# Análise de Requisitos: Módulo de Gestão de Contatos Externos no Odoo

## 1. Introdução

Este documento detalha os requisitos para o desenvolvimento de um novo módulo customizado no Odoo, focado na gestão de contatos que não se enquadram como clientes formais no fluxo de CRM tradicional. O objetivo principal é permitir o rastreamento de transações financeiras avulsas (ganhos e custos) e a manutenção de anotações compartilhadas, vinculadas a um identificador único de contato, sem modificar o código-fonte principal do Odoo.

## 2. Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer ao usuário.

### 2.1. Gestão de Contatos Não-Clientes
*   **RF001:** O sistema deve permitir a criação e o gerenciamento de contatos que são explicitamente marcados como "não-clientes" ou "contatos externos".
*   **RF002:** Deve haver uma seção ou menu dedicado no Odoo para acessar e gerenciar esses contatos, separada do módulo de CRM principal.
*   **RF003:** Cada contato externo deve ter um identificador único (ID), que no contexto do Odoo será o `res.partner` ID.

### 2.2. Rastreamento Financeiro
*   **RF004:** O sistema deve permitir o registro de transações financeiras (ganhos e custos) associadas a cada contato externo.
*   **RF005:** Para cada transação, deve ser possível registrar a descrição, o valor, o tipo (ganho/custo), a data e o status (pendente/liquidado).
*   **RF006:** O sistema deve calcular e exibir o total de ganhos, o total de custos e o saldo geral para cada contato externo.
*   **RF007:** As transações devem ser visualizadas de forma clara no perfil do contato externo, com indicação visual do tipo (ganho/custo) e status.

### 2.3. Anotações Compartilhadas
*   **RF008:** Deve existir um campo de texto para "anotações compartilhadas" no perfil de cada contato externo.
*   **RF009:** As anotações inseridas neste campo devem ser visíveis para todos os usuários que acessarem o mesmo contato, garantindo a sincronização da informação por ID.
*   **RF010:** O campo de anotações deve ser intuitivo e permitir texto livre para observações contextuais (ex: "Ah, essa foi a pessoa que comprou o sofá aqui do escritório").

### 2.4. Integração com o Menu Principal do Odoo
*   **RF011:** O novo módulo deve ser acessível através de uma nova entrada no menu principal do Odoo, com um nome claro como "Gestão de Contatos".

## 3. Requisitos Não-Funcionais

Os requisitos não-funcionais descrevem como o sistema deve funcionar.

### 3.1. Modulariedade
*   **RNF001:** O módulo deve ser desenvolvido como um plugin independente do Odoo, sem modificar o código-fonte principal, para garantir a facilidade de atualização do Odoo no futuro.

### 3.2. Usabilidade
*   **RNF002:** A interface do usuário para o gerenciamento de contatos externos e suas transações deve ser intuitiva e fácil de usar.

### 3.3. Integridade de Dados
*   **RNF003:** O sistema deve garantir a integridade dos dados financeiros e das anotações, associando-os corretamente ao ID único do contato.

### 3.4. Segurança
*   **RNF004:** O módulo deve seguir as práticas de segurança padrão do Odoo para controle de acesso aos modelos e dados.

### 3.5. Performance
*   **RNF005:** O desenvolvimento do módulo não deve impactar negativamente a performance geral do sistema Odoo.

## 4. Detalhamento da Regra de Negócio: ID Único e Anotações Sincronizadas

O conceito de "ID único" para o qual as anotações devem ser sincronizadas é fundamental. No Odoo, o modelo `res.partner` já serve como um identificador único para pessoas e organizações. Portanto, o campo `shared_notes` será adicionado diretamente ao modelo `res.partner`.

Quando um usuário acessar um registro `res.partner` (seja ele um cliente formal, um lead ou um "contato externo" marcado pelo novo módulo), o campo `shared_notes` estará presente e exibirá o mesmo conteúdo para todos os usuários que visualizarem aquele `res.partner` específico. Isso garante que a anotação "Ah, essa foi a pessoa que comprou o sofá aqui do escritório" estará sempre associada àquele indivíduo, independentemente de como ele é categorizado em outros módulos (CRM, Vendas, etc.).

## 5. Resumo

O módulo `odoo_non_client_management` visa preencher uma lacuna no gerenciamento de interações avulsas, fornecendo uma ferramenta dedicada para rastrear compromissos financeiros e informações contextuais importantes para contatos que ainda não justificam um processo completo de CRM. A abordagem modular garante a sustentabilidade e a compatibilidade com futuras atualizações do Odoo.
