# Guia de Customização de Fluxos Jurídicos - Araújo & França

Este documento orienta como configurar o Odoo para o fluxo específico de advocacia após a primeira instalação.

## 1. Estágios do CRM (Funil de Vendas Jurídico)
No módulo CRM, altere os estágios padrão para:
1.  **Novo Contato:** Leads vindos do site ou WhatsApp.
2.  **Consulta Inicial:** Reunião agendada para entender o caso.
3.  **Análise de Viabilidade:** Estudo jurídico do caso e provas.
4.  **Proposta de Honorários:** Envio do contrato de prestação de serviços.
5.  **Contrato Assinado:** Cliente fechado, pronto para virar processo.

## 2. Gestão de Faturamento (Honorários)
Configure o módulo de Faturamento para os tipos de cobrança comuns:
*   **Honorários Iniciais (Pró-labore):** Fatura única no início do caso.
*   **Honorários Mensais (Retainer):** Para clientes fixos (empresas).
*   **Honorários de Êxito (Ad exitum):** Fatura gerada ao final do processo com base no ganho do cliente.

## 3. Automação de Backups (Banco de Dados e Documentos)
O sistema possui uma estratégia de backup redundante para garantir a segurança total dos dados:

### A. Banco de Dados (PostgreSQL)
Gerenciado pelo container `db_backup`:
*   **Frequência:** Diária (meia-noite).
*   **Retenção:** Mantém os últimos 7 dias, 4 semanas e 6 meses.
*   **Local:** Arquivos `.sql.gz` em `/backups`.

### B. Arquivos Físicos (Filestore/PDFs)
Gerenciado pelo container `filestore_backup`:
*   **Frequência:** Diária (01:00 AM).
*   **Função:** Compacta toda a pasta `/var/lib/odoo` (onde ficam os PDFs de processos e documentos).
*   **Local:** Arquivos `.tar.gz` em `/backups/filestore`.

## 4. Localização Brasileira (L10n-Brazil)
Para conformidade com o sistema fiscal brasileiro (emissão de notas e boletos):
1.  **Módulos OCA:** É necessário baixar os módulos do repositório [OCA/l10n-brazil](https://github.com/OCA/l10n-brazil) e colocá-los na pasta `/addons`.
2.  **Configuração:** O arquivo `odoo.conf` já está pré-configurado para carregar o módulo base da localização brasileira (`l10n_br_base`).

## 5. Segurança SSL (HTTPS)
O Nginx está configurado. Para ativar o HTTPS real:
1.  Coloque seus arquivos `fullchain.pem` e `privkey.pem` na pasta `./nginx/certs`.
2.  Descomente as linhas de SSL no arquivo `./nginx/conf.d/odoo.conf`.
3.  Reinicie os containers: `docker-compose restart nginx`.
