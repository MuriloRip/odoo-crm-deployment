# Guia de Uso: CRM e Calendário no Odoo para Araújo & França Advocacia

## 1. Introdução

Este guia foi elaborado para auxiliar na utilização do sistema Odoo, focando nos módulos de **CRM (Gestão de Relacionamento com o Cliente)** e **Calendário**. O objetivo é otimizar o processo de captação e acompanhamento de clientes, bem como a organização de tarefas e compromissos. Compreender cada campo e sua finalidade é crucial para maximizar a eficiência do sistema.

## 2. Visão Geral do CRM no Odoo

O CRM no Odoo é a ferramenta central para gerenciar todas as interações com potenciais clientes (leads) e clientes existentes. Ele permite registrar informações, acompanhar o progresso de cada caso e garantir que nenhuma oportunidade seja perdida. Para a Araújo & França Advocacia, ele foi customizado para refletir o fluxo jurídico.

## 3. Criando um Novo Contato/Lead

Ao iniciar um novo contato, seja ele um potencial cliente ou uma pessoa com quem o escritório tem alguma transação avulsa, você preencherá um formulário. Entender cada campo é fundamental:

### 3.1. Campos Essenciais (Informações Básicas)

| Campo | Para que Serve | Como Preencher | Exemplo |
| :--- | :--- | :--- | :--- |
| **Nome** | Identificação principal da pessoa ou empresa. | Nome completo da pessoa ou razão social da empresa. | `João da Silva` ou `Empresa XYZ Ltda.` |
| **Email** | Contato principal para comunicações eletrônicas. | Endereço de e-mail válido. | `joao.silva@email.com` |
| **Telefone** | Contato principal para comunicações telefônicas. | Número de telefone com DDD. | `(11) 98765-4321` |
| **Empresa** | Se o contato representa uma empresa. | Nome da empresa (se aplicável). | `Construtora ABC` |

### 3.2. Campos Específicos do CRM Jurídico (Oportunidade/Lead)

Estes campos são cruciais para qualificar e acompanhar um potencial caso jurídico:

| Campo | Para que Serve | Como Preencher | Exemplo | 
| :--- | :--- | :--- | :--- |
| **Assunto** | Breve descrição do caso ou interesse do contato. | Resumo do motivo do contato. | `Divórcio Litigioso`, `Revisão Contratual` |
| **Fase do Processo** | Estágio atual do lead no funil de vendas/processo jurídico. | Selecione a fase apropriada (ex: `Novo`, `Qualificação`, `Proposta`, `Ganho`). | `Qualificação` |
| **Valor Estimado da Causa** | Estimativa do valor financeiro envolvido no caso. | Valor monetário aproximado. | `R$ 50.000,00` |

### 3.3. Campos do Módulo de Gestão de Contatos Externos (Novo Módulo)

Estes campos são parte do novo módulo `odoo_non_client_management` e são específicos para pessoas que não são clientes de um processo jurídico formal, mas com quem o escritório tem transações avulsas.

| Campo | Para que Serve | Como Preencher | Exemplo | 
| :--- | :--- | :--- | :--- |
| **É Contato Externo** | Indica que este contato não é um lead/cliente de CRM tradicional. | Marque esta caixa se for um contato avulso (ex: venda de um bem). | `[X]` (marcado) |
| **Anotações Compartilhadas** | Campo de texto livre para observações importantes sobre o contato, visíveis para todos que acessarem este ID. | Informações contextuais relevantes. | `"Essa foi a pessoa que comprou o sofá aqui do escritório. Pagar em 3x." ` |

### 3.4. Gestão de Ganhos/Custos (Aba no Contato Externo)

Dentro do perfil de um contato marcado como "Contato Externo", você encontrará uma aba para registrar transações financeiras:

| Campo | Para que Serve | Como Preencher | Exemplo | 
| :--- | :--- | :--- | :--- |
| **Descrição** | Detalhe da transação financeira. | `Venda de Sofá`, `Custo de Entrega` |
| **Tipo** | Define se é um `Ganho` (entrada) ou `Custo` (saída). | Selecione `Ganho` ou `Custo`. | `Ganho` |
| **Valor** | O montante financeiro da transação. | Valor monetário. | `1.500,00` |
| **Data** | Data em que a transação ocorreu. | Data da transação. | `07/02/2026` |
| **Status** | Indica se a transação está `Pendente` ou `Liquidado/Pago`. | Selecione o status atual. | `Pendente` |

## 4. Integrando com o Calendário

O Calendário é essencial para organizar compromissos e atividades relacionadas aos seus contatos e casos.

### 4.1. Criando Atividades (Tarefas, Reuniões, Ligações)

No perfil de um lead/cliente (ou mesmo em um contato externo), você pode criar atividades diretamente. Isso vincula a atividade ao contato, facilitando o acompanhamento.

1.  **Acesse o Contato:** Abra o perfil do lead ou cliente.
2.  **Clique em "Agendar Atividade":** Geralmente, há um botão ou seção para isso.
3.  **Preencha os Detalhes:**
    *   **Tipo de Atividade:** `Ligação`, `Reunião`, `Tarefa`, `E-mail`.
    *   **Resumo:** Breve descrição da atividade (ex: `Ligar para João sobre proposta`).
    *   **Data Limite:** Quando a atividade deve ser concluída.
    *   **Atribuído a:** Quem é responsável pela atividade.

### 4.2. Visualizando no Calendário

Todas as atividades agendadas aparecerão no módulo de **Calendário** do Odoo. Isso permite uma visão clara de todos os compromissos do escritório, organizados por dia, semana ou mês. Você pode arrastar e soltar atividades para reagendá-las.

## 5. Fluxo de Trabalho: Do Lead ao Cliente

O processo geralmente segue estas etapas no CRM:

1.  **Novo Lead:** Um contato inicial é registrado com informações básicas e o `Assunto` do caso.
2.  **Qualificação:** A equipe avalia a viabilidade do caso, adicionando mais detalhes e agendando atividades (ligações, reuniões).
3.  **Proposta:** Uma proposta de honorários é enviada e registrada.
4.  **Ganho:** O cliente aceita a proposta, e o lead se torna um cliente ativo, movendo-se para a fase `Ganho`.

Para contatos externos, o fluxo é mais direto: registra-se o contato, marca-se como `É Contato Externo` e gerencia-se as transações financeiras e anotações na aba dedicada.

## 6. Dicas de Uso

*   **Seja Detalhado:** Quanto mais informações você registrar, mais útil o sistema será.
*   **Use as Anotações Compartilhadas:** Elas são a memória coletiva do escritório para aquele contato.
*   **Mantenha o Calendário Atualizado:** Garanta que todas as atividades e compromissos estejam registrados para evitar esquecimentos.
*   **Explore os Filtros:** O Odoo permite filtrar e agrupar informações para encontrar rapidamente o que você precisa.

---
