# Comandos Rápidos de Terminal

Para gerenciar seu servidor Odoo, você pode utilizar os seguintes comandos diretamente no terminal:

## 1. Editar Arquivos com Nano
Se precisar ajustar alguma configuração manualmente:
```bash
nano addons/odoo_non_client_management/__manifest__.py
```
*   **Para Salvar:** `Ctrl + O` e depois `Enter`.
*   **Para Sair:** `Ctrl + X`.

## 2. Permissões de Execução
Para garantir que os scripts funcionem corretamente:
```bash
chmod +x update_odoo.sh
```

## 3. Executar Atualização
Para baixar as novas alterações e reiniciar o sistema:
```bash
./update_odoo.sh
```

## 4. Verificar Logs (Docker)
Se algo não estiver funcionando, verifique os erros com:
```bash
docker-compose logs -f web
```
