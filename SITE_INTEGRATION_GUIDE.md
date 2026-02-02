# Guia de Integração: Site Araújo & França + Odoo CRM

Este guia detalha como conectar o site atual ([araujoefranca.com.br](https://araujoefranca.com.br/)) ao novo sistema Odoo CRM para automatizar a captura de clientes.

## 1. Cenário Atual
O site utiliza principalmente botões de **WhatsApp** para conversão. Embora eficientes, esses contatos não geram dados estruturados automaticamente no CRM.

## 2. Estratégia de Integração

### A. Formulário de Contato (Recomendado)
Para profissionalizar o atendimento, sugerimos adicionar um formulário de "Consulta Inicial" no site.
*   **Campos:** Nome, E-mail, Telefone, Área de Interesse (Societário, Tributário, etc.) e Mensagem.
*   **Conexão:** O Odoo possui uma API nativa (XML-RPC) que permite que qualquer formulário web envie dados diretamente para o módulo `crm.lead`.

### B. Integração via Webhook (WhatsApp)
Se o escritório preferir manter o WhatsApp como foco principal, pode-se usar ferramentas como **Zapier** ou **n8n** para:
1.  Capturar o início da conversa.
2.  Criar automaticamente um "Lead" no Odoo com o número do telefone do cliente.

## 3. Exemplo de Código para o Desenvolvedor do Site (PHP)
Se o site for em PHP, o desenvolvedor pode usar este snippet para enviar dados ao Odoo:

```php
// Exemplo simplificado de conexão via XML-RPC
$url = "http://ip-do-servidor:8069";
$db = "nome_do_banco";
$username = "admin";
$password = "senha";

// 1. Autenticação
// 2. Criação do Lead no Odoo
$client = new Ripcord\Client("$url/xmlrpc/2/object");
$id = $client->execute($db, $uid, $password, 'crm.lead', 'create', [[
    'name' => 'Novo Lead via Site: ' . $nome_cliente,
    'contact_name' => $nome_cliente,
    'email_from' => $email_cliente,
    'phone' => $telefone_cliente,
    'description' => $mensagem_cliente,
    'team_id' => 1 // Equipe de Vendas/Jurídico
]]);
```

## 4. Benefícios para o Escritório
*   **Histórico Centralizado:** Todo contato vira um registro com data e hora.
*   **Distribuição de Casos:** O Odoo pode encaminhar o lead automaticamente para o advogado especialista (ex: Dr. Willian para Previdenciário).
*   **Follow-up:** Lembretes automáticos para não deixar nenhum cliente sem resposta.
