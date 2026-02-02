# Guia Completo: Instalar Odoo CRM em Notebook com Linux
## Passo-a-Passo para Sexta-Feira

**Data:** Janeiro 2026  
**Objetivo:** Formatar notebook, instalar Linux e rodar Odoo CRM  
**Tempo Estimado:** 2-3 horas  
**Dificuldade:** Média

---

## 📋 O que Você Vai Fazer

1. **Formatar o notebook** (apagar tudo)
2. **Instalar Ubuntu Linux** (sistema operacional grátis)
3. **Instalar Odoo CRM** (usando script automatizado)
4. **Configurar estágios jurídicos** (pré-configurados)
5. **Testar o sistema** (garantir que funciona)

---

## 🛠️ Pré-requisitos

### Hardware Necessário
- ✅ Notebook com pelo menos 4GB de RAM (ideal 8GB+)
- ✅ 50GB de espaço em disco disponível
- ✅ Conexão com internet
- ✅ Pen drive com 8GB (para instalar Ubuntu)

### Softwares Necessários
- ✅ Rufus (para criar pen drive bootável) - grátis
- ✅ Ubuntu 22.04 LTS ISO (grátis)
- ✅ Git (já vem no Linux)

---

## 📥 Passo 1: Preparar o Pen Drive Bootável

### 1.1 Baixar Rufus
Acesse: https://rufus.ie/  
Clique em "Download" e baixe a versão mais recente.

### 1.2 Baixar Ubuntu 22.04 LTS
Acesse: https://ubuntu.com/download/desktop  
Clique em "Download" (arquivo .iso ~3.5GB).

### 1.3 Criar Pen Drive Bootável
1. Conecte o pen drive ao computador
2. Abra o Rufus
3. Selecione o pen drive em "Device"
4. Clique em "SELECT" e escolha o arquivo Ubuntu .iso
5. Deixe as configurações padrão
6. Clique em "START"
7. Aguarde até terminar (~10 minutos)

**Pronto! Pen drive está pronto para instalar Linux.**

---

## 💻 Passo 2: Formatar Notebook e Instalar Ubuntu

### 2.1 Iniciar Instalação do Ubuntu
1. Desligar o notebook completamente
2. Conectar o pen drive
3. Ligar o notebook e apertar **F12** (ou F2, DEL, ESC - depende do modelo)
4. Selecionar "Boot from USB"
5. Aguardar carregar Ubuntu

### 2.2 Instalar Ubuntu
Quando a tela do Ubuntu aparecer:

1. Clique em **"Install Ubuntu"**
2. Selecione idioma: **Português (Brasil)**
3. Clique em **"Continue"**
4. Selecione layout de teclado: **Portuguese (Brazil)**
5. Clique em **"Continue"**
6. Selecione **"Erase disk and install Ubuntu"** (vai formatar tudo!)
7. Clique em **"Install Now"**
8. Confirme que vai apagar tudo (clique "Continue")
9. Selecione timezone: **America/Sao_Paulo**
10. Crie usuário:
    - **Nome:** seu nome
    - **Nome do computador:** odoo-escritorio
    - **Usuário:** seu_nome
    - **Senha:** escolha uma senha forte
11. Clique em **"Continue"**
12. Aguarde instalação (~30-45 minutos)
13. Clique em **"Restart Now"**
14. Remova o pen drive quando pedir

**Pronto! Ubuntu está instalado!**

---

## 🚀 Passo 3: Instalar Odoo CRM

### 3.1 Abrir Terminal
Clique no ícone de terminal (ou pressione **Ctrl + Alt + T**)

### 3.2 Clonar o Repositório
Digite os comandos abaixo (um por vez, pressione Enter depois de cada um):

```bash
cd ~
git clone https://github.com/MuriloRip/odoo-crm-deployment.git
cd odoo-crm-deployment
```

### 3.3 Executar Script de Instalação
Digite:

```bash
sudo bash install.sh
```

**Vai pedir sua senha. Digite a senha que você criou no Ubuntu.**

**O script vai:**
- ✅ Atualizar o sistema
- ✅ Instalar Python, PostgreSQL, Nginx
- ✅ Clonar Odoo 17
- ✅ Configurar tudo automaticamente

**Tempo:** ~20-30 minutos (depende da internet)

### 3.4 Aguardar Conclusão
Quando terminar, você verá:

```
========================================
✓ Instalação Concluída!
========================================
```

**Pronto! Odoo está instalado!**

---

## 🎯 Passo 4: Acessar o Odoo

### 4.1 Abrir Navegador
Clique no ícone do Firefox (ou Chrome)

### 4.2 Acessar Odoo
Digite na barra de endereço:

```
http://localhost:8069
```

Pressione Enter.

### 4.3 Criar Banco de Dados
Você verá uma tela para criar um novo banco de dados:

1. **Database name:** odoo
2. **Email:** seu@email.com
3. **Password:** admin
4. **Confirm Password:** admin
5. Deixe as outras opções padrão
6. Clique em **"Create database"**

**Aguarde ~2-3 minutos enquanto o banco é criado.**

### 4.4 Login
Quando terminar, você verá tela de login:

- **Email:** admin@example.com
- **Senha:** admin

Clique em **"Log in"**

**Pronto! Você está dentro do Odoo!**

---

## ⚙️ Passo 5: Configurar Estágios Jurídicos

### 5.1 Instalar Módulo CRM
1. Clique em **"Aplicativos"** (no menu)
2. Procure por **"CRM"**
3. Clique em **"Instalar"**
4. Aguarde instalação (~1 minuto)

### 5.2 Executar Script de Estágios
Abra terminal novamente (Ctrl + Alt + T) e digite:

```bash
cd ~/odoo-crm-deployment
python3 setup_stages.py
```

**O script vai criar os 5 estágios jurídicos automaticamente.**

### 5.3 Verificar Estágios
1. Volte ao navegador (Odoo)
2. Clique em **"CRM"** (no menu)
3. Clique em **"Funil de Vendas"**
4. Você verá as 5 colunas:
   - Novo Contato
   - Consulta Inicial
   - Análise de Viabilidade
   - Proposta de Honorários
   - Contrato Assinado

**Pronto! Estágios configurados!**

---

## 📝 Passo 6: Testar o Sistema

### 6.1 Criar um Lead de Teste
1. Clique em **"CRM"** → **"Leads"**
2. Clique em **"Novo"**
3. Preencha:
   - **Nome:** João Silva (teste)
   - **Email:** joao@teste.com
   - **Telefone:** 11999999999
4. Clique em **"Salvar"**

### 6.2 Mover para Próximo Estágio
1. Clique em **"CRM"** → **"Funil de Vendas"**
2. Arraste o card "João Silva" de "Novo Contato" para "Consulta Inicial"
3. Veja se funciona!

### 6.3 Adicionar Documento
1. Clique no lead "João Silva"
2. Vá até a seção **"Documentos"**
3. Clique em **"Anexar"** e escolha um arquivo PDF
4. Veja se o documento foi anexado

**Pronto! Sistema testado e funcionando!**

---

## 🔧 Comandos Úteis (Para Depois)

### Ver Status do Odoo
```bash
systemctl status odoo
```

### Reiniciar Odoo
```bash
sudo systemctl restart odoo
```

### Ver Logs (para resolver problemas)
```bash
tail -f /opt/odoo/logs/odoo.log
```

### Fazer Backup
```bash
bash /opt/odoo/backup.sh
```

---

## ⚠️ Possíveis Problemas e Soluções

### Problema: "Conexão recusada" ao acessar http://localhost:8069

**Solução:**
1. Abra terminal
2. Digite: `systemctl status odoo`
3. Se disser "inactive", execute: `sudo systemctl start odoo`
4. Aguarde 30 segundos
5. Tente acessar novamente

### Problema: Senha do admin não funciona

**Solução:**
1. Abra terminal
2. Digite: `sudo -u postgres psql`
3. Digite: `ALTER USER odoo WITH PASSWORD 'nova_senha';`
4. Digite: `\q`
5. Edite `/etc/odoo/odoo.conf` e altere `db_password`
6. Reinicie: `sudo systemctl restart odoo`

### Problema: Notebook fica muito lento

**Solução:**
1. Feche outros programas
2. Aumente a RAM do Odoo em `/etc/odoo/odoo.conf`
3. Ou use um notebook com mais RAM

---

## 📋 Checklist Final

Antes de terminar sexta-feira, verifique:

- [ ] Ubuntu instalado e funcionando
- [ ] Odoo instalado e acessível em http://localhost:8069
- [ ] Banco de dados "odoo" criado
- [ ] Login funcionando (admin/admin)
- [ ] Módulo CRM instalado
- [ ] 5 estágios jurídicos criados
- [ ] Lead de teste criado
- [ ] Lead movido entre estágios
- [ ] Documento anexado com sucesso
- [ ] Backup testado

---

## 🎯 Próximos Passos (Depois de Sexta)

1. **Integrar com o site:** Conectar araujoefranca.com.br ao CRM
2. **Treinar equipe:** Ensinar como usar o sistema
3. **Customizar:** Adicionar campos específicos do escritório
4. **Backup automático:** Agendar backups diários

---

## 📞 Dúvidas Durante a Instalação?

Se algo der errado:

1. **Anote a mensagem de erro**
2. **Procure no Google:** "Odoo [mensagem de erro]"
3. **Consulte os logs:** `tail -f /opt/odoo/logs/odoo.log`
4. **Reinicie o serviço:** `sudo systemctl restart odoo`

---

**Boa sorte na sexta-feira! 🚀**

*Guia preparado por: Manus AI*  
*Data: Janeiro 2026*
