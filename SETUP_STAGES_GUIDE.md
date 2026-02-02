# Guia: Pré-configuração de Estágios Jurídicos

Este script automatiza a criação dos estágios jurídicos no Odoo CRM, economizando tempo de configuração manual.

---

## 📋 O que o Script Faz

1. ✅ Conecta ao Odoo via XML-RPC
2. ✅ Verifica se o módulo CRM está instalado
3. ✅ Obtém ou cria a equipe padrão
4. ✅ Deleta os estágios padrão do Odoo
5. ✅ Cria 5 estágios jurídicos pré-configurados

---

## 🚀 Como Usar

### Pré-requisitos

- Odoo 17 já instalado e rodando
- Módulo CRM já instalado
- Python 3 com xmlrpc disponível

### Execução

```bash
# Opção 1: Direto
python3 /opt/odoo/setup_stages.py

# Opção 2: Com permissões
chmod +x /opt/odoo/setup_stages.py
/opt/odoo/setup_stages.py
```

### Resultado

O script criará estes estágios:

| Ordem | Nome | Probabilidade | Descrição |
|-------|------|---------------|-----------|
| 1 | Novo Contato | 10% | Leads vindos do site ou WhatsApp |
| 2 | Consulta Inicial | 30% | Reunião agendada |
| 3 | Análise de Viabilidade | 50% | Estudo jurídico do caso |
| 4 | Proposta de Honorários | 75% | Contrato enviado |
| 5 | Contrato Assinado | 100% | Pronto para ajuizar |

---

## ⚙️ Configuração

Se precisar alterar as credenciais padrão, edite o arquivo:

```python
# setup_stages.py - Linhas 10-12
ODOO_URL = "http://localhost:8069"
ODOO_DB = "odoo"
ODOO_USER = "admin"
ODOO_PASSWORD = "admin"
```

---

## 🔧 Customização

### Adicionar Novos Estágios

Edite a lista `LEGAL_STAGES` no script:

```python
LEGAL_STAGES = [
    {
        "name": "Seu Estágio",
        "sequence": 6,
        "probability": 50,
        "description": "Descrição do estágio",
    },
    # ... mais estágios
]
```

### Modificar Estágios Existentes

1. Acesse: **CRM → Configuração → Estágios**
2. Clique no estágio desejado
3. Edite nome, sequência, probabilidade
4. Salve

---

## ❌ Desfazer

Se precisar remover os estágios criados:

1. Acesse: **CRM → Configuração → Estágios**
2. Selecione todos os estágios
3. Clique em "Deletar"
4. Execute o script novamente

---

## 🐛 Troubleshooting

### Erro: "Conexão recusada"
```
❌ Erro ao conectar ao Odoo
```
**Solução:** Verifique se o Odoo está rodando:
```bash
systemctl status odoo
```

### Erro: "Autenticação falhou"
```
❌ Erro: Autenticação falhou
```
**Solução:** Verifique as credenciais em `setup_stages.py`

### Erro: "Módulo CRM não está instalado"
```
❌ Erro: Módulo CRM não está instalado
```
**Solução:** Instale o módulo CRM:
1. Acesse Odoo → Aplicativos
2. Procure por "CRM"
3. Clique em "Instalar"
4. Execute o script novamente

---

## 📝 Notas

- O script é **idempotente** - pode ser executado múltiplas vezes sem problemas
- Os estágios padrão do Odoo serão **deletados** automaticamente
- A equipe "Equipe Jurídica" será criada se não existir
- Todos os estágios são criados com `fold=False` (visíveis por padrão)

---

*Última atualização: Janeiro 2026*
