# Guia de Customizações - Odoo CRM

Este documento descreve as novas funcionalidades implementadas no ambiente `odoo_dev` para atender aos requisitos de negociação e controle financeiro.

## 1. CRM e Negociação

### Notas de Negociação
- **Onde encontrar:** Dentro de qualquer Lead ou Oportunidade, há uma nova aba chamada **"Notas de Negociação"**.
- **Uso:** Espaço livre para anotar detalhes pessoais do cliente (ex: "tem um fusca", "filho vai casar") que ajudam na abordagem comercial.

### Botão de WhatsApp
- **Onde encontrar:** No card do Lead (visão Kanban) e dentro do formulário ao lado do telefone.
- **Uso:** Clique no ícone verde do WhatsApp para abrir uma conversa direta com o cliente. O sistema já limpa o número e adiciona uma mensagem de saudação automática.

### Prioridades Customizadas
- **Onde encontrar:** No formulário do Lead.
- **Opções:** 
  - A conversar
  - Interessado
  - Urgente
  - Processo em andamento
  - Pendente

## 2. Controle Financeiro (Ganhos e Gastos)

### Novo Módulo "Financeiro"
- **Onde encontrar:** No menu principal do Odoo, agora existe o ícone **"Financeiro"**.
- **Uso:** Permite cadastrar transações de "Ganho (A Receber)" ou "Gasto (A Pagar)", vinculando-as a um contato.

### Visão Unificada no Contato
- **Onde encontrar:** Ao abrir o cadastro de qualquer pessoa (Contatos), há uma nova aba **"Financeiro (Ganhos/Gastos)"**.
- **Uso:** Mostra o resumo de quanto aquela pessoa deve ou tem a receber, além da lista de todas as transações ligadas a ela.

## 3. Agenda e Follow-up

### Tipos de Atividade
Foram criados dois novos tipos de atividade para facilitar o agendamento:
1. **Re-ligar (Follow-up):** Para lembrar de ligar e verificar se o cliente quer continuar.
2. **Reunião Agendada:** Para compromissos formais.

### Estágios do Funil
O funil de vendas foi ajustado para refletir o processo solicitado:
- Antes de ser Lead -> Lead -> Oportunidade -> Cliente

---

## Como Ativar as Mudanças no Odoo

Como os arquivos foram enviados para o servidor, você precisa:
1. Ir em **Configurações** -> **Ativar Modo de Desenvolvedor**.
2. Ir no menu **Apps**.
3. Clicar em **Atualizar Lista de Apps**.
4. Procurar por "CRM Custom Notes" e "Controle Financeiro Customizado" e clicar em **Instalar** ou **Atualizar**.
