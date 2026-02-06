# Guia de Instalação: Módulo de Gestão de Contatos Externos

Este guia explica como ativar o novo módulo `odoo_non_client_management` no seu ambiente Odoo.

## Passos para Instalação

1.  **Atualizar o Código:**
    Certifique-se de que a pasta `addons/odoo_non_client_management` está no seu servidor.

2.  **Reiniciar o Odoo:**
    *   Se estiver usando **Docker**:
        ```bash
        docker-compose restart web
        ```
    *   Se estiver usando **Instalação Direta**:
        ```bash
        sudo systemctl restart odoo
        ```

3.  **Ativar o Modo Desenvolvedor:**
    *   No Odoo, vá em **Definições**.
    *   Role até o final e clique em **Ativar o modo de desenvolvedor**.

4.  **Atualizar Lista de Apps:**
    *   Vá no menu superior **Aplicações**.
    *   Clique em **Atualizar Lista de Aplicações** no menu horizontal superior.
    *   Clique em **Atualizar** na janela que abrir.

5.  **Instalar o Módulo:**
    *   Remova o filtro "Aplicações" da barra de busca.
    *   Digite `Gestão de Contatos Não-Clientes`.
    *   Clique em **Instalar**.

## Como Usar

### Criando um Contato Externo
1.  Acesse o novo menu **Gestão de Contatos** no topo da tela.
2.  Clique em **Criar**.
3.  O campo **É Contato Externo** virá marcado automaticamente.
4.  Preencha o nome e outras informações.

### Registrando Transações (Ganhos/Custos)
1.  Dentro do formulário do contato, vá na aba **Gestão de Ganhos/Custos**.
2.  Adicione linhas na tabela de transações.
3.  Defina se é um **Ganho** (venda, entrada) ou **Custo** (pagamento, despesa).
4.  O saldo será calculado automaticamente no topo da aba.

### Anotações Compartilhadas
1.  Use o campo **Anotações do ID (Compartilhadas)** para escrever observações que todos os usuários devem ver para aquele contato específico.
2.  Exemplo: "Pessoa que comprou o sofá do escritório".

---
*Nota: Este módulo foi desenvolvido como um plugin e não altera o código base do Odoo, facilitando atualizações futuras.*
