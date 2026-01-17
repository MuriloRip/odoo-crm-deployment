# Guia de Instalação: Odoo 17 CRM (Sem Docker)

Para servidores compartilhados ou ambientes onde Docker não é viável, este guia detalha a instalação do Odoo 17 diretamente no Ubuntu.

---

## 📋 Pré-requisitos

- **Sistema Operacional:** Ubuntu 20.04 LTS ou 22.04 LTS
- **Acesso:** SSH com privilégios sudo
- **Recursos Mínimos:**
  - 2 GB de RAM
  - 10 GB de espaço em disco
  - 1 vCPU (recomendado 2+)

---

## 🚀 Instalação Rápida (Automatizada)

### 1. Clonar o Repositório
```bash
git clone https://github.com/MuriloRip/odoo-crm-deployment.git
cd odoo-crm-deployment
```

### 2. Executar o Script de Instalação
```bash
sudo bash install.sh
```

O script fará automaticamente:
- ✅ Atualizar o sistema
- ✅ Instalar dependências (Python, PostgreSQL, Nginx)
- ✅ Criar usuário `odoo`
- ✅ Clonar o repositório oficial do Odoo 17
- ✅ Configurar PostgreSQL
- ✅ Instalar dependências Python
- ✅ Criar arquivo de configuração
- ✅ Iniciar o serviço via systemd

### 3. Acessar o Odoo
```
http://seu-servidor:8069
```

**Credenciais padrão:**
- Usuário: `admin`
- Senha: `admin`

---

## 🔧 Comandos Úteis

### Ver Status do Serviço
```bash
systemctl status odoo
```

### Reiniciar o Odoo
```bash
systemctl restart odoo
```

### Ver Logs em Tempo Real
```bash
tail -f /opt/odoo/logs/odoo.log
```

### Parar o Odoo
```bash
systemctl stop odoo
```

### Iniciar o Odoo
```bash
systemctl start odoo
```

---

## 🔐 Configuração de Segurança

### 1. Alterar Senha do Admin
Acesse `http://seu-servidor:8069/web/settings/users` e altere a senha padrão.

### 2. Alterar Senha do PostgreSQL
```bash
sudo -u postgres psql
ALTER USER odoo WITH PASSWORD 'nova_senha_segura';
\q
```

Depois, atualize `/etc/odoo/odoo.conf`:
```ini
db_password = nova_senha_segura
```

E reinicie:
```bash
systemctl restart odoo
```

### 3. Configurar Nginx como Proxy Reverso

Crie `/etc/nginx/sites-available/odoo`:
```nginx
upstream odoo {
    server 127.0.0.1:8069;
}

server {
    listen 80;
    server_name seu-dominio.com.br;

    client_max_body_size 200M;

    location / {
        proxy_pass http://odoo;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location ~* ^/web/static/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

Ativar o site:
```bash
sudo ln -s /etc/nginx/sites-available/odoo /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### 4. Configurar SSL/HTTPS com Let's Encrypt
```bash
sudo apt-get install certbot python3-certbot-nginx -y
sudo certbot certonly --nginx -d seu-dominio.com.br
```

Depois, atualize `/etc/nginx/sites-available/odoo` para usar HTTPS.

---

## 💾 Backup Automatizado

### 1. Tornar o Script Executável
```bash
chmod +x /opt/odoo/backup.sh
```

### 2. Agendar Backup Diário (Cron)
```bash
sudo crontab -e
```

Adicione a linha:
```cron
0 1 * * * /opt/odoo/backup.sh >> /opt/odoo/logs/backup.log 2>&1
```

Isso executará o backup todos os dias à 1:00 AM.

### 3. Verificar Backups
```bash
ls -lh /opt/odoo/backups/database/
ls -lh /opt/odoo/backups/filestore/
```

---

## 📊 Estrutura de Diretórios

```
/opt/odoo/
├── odoo/                 # Código-fonte do Odoo 17
├── venv/                 # Ambiente virtual Python
├── addons/               # Módulos personalizados
├── data/                 # Filestore (PDFs, imagens)
├── backups/              # Backups automáticos
│   ├── database/         # Backups do PostgreSQL
│   └── filestore/        # Backups de arquivos
├── logs/                 # Arquivos de log
└── backup.sh             # Script de backup

/etc/odoo/
└── odoo.conf             # Arquivo de configuração

/etc/systemd/system/
└── odoo.service          # Serviço systemd
```

---

## 🐛 Troubleshooting

### Erro: "Port 8069 already in use"
```bash
lsof -i :8069
kill -9 <PID>
systemctl restart odoo
```

### Erro: "PostgreSQL connection refused"
```bash
sudo systemctl status postgresql
sudo systemctl restart postgresql
```

### Erro: "Permission denied" ao criar banco de dados
```bash
sudo chown -R odoo:odoo /opt/odoo
sudo chmod 755 /opt/odoo
```

### Logs mostram "ModuleNotFoundError"
```bash
source /opt/odoo/venv/bin/activate
pip install -r /opt/odoo/odoo/requirements.txt
systemctl restart odoo
```

---

## 📈 Próximos Passos

1. **Instalar módulos recomendados:**
   - CRM
   - Calendar
   - Documents
   - Contacts
   - Project
   - Timesheet
   - L10n-Brazil (para conformidade fiscal)

2. **Integrar com o site:**
   - Seguir o guia em `SITE_INTEGRATION_GUIDE.md`

3. **Customizar fluxos jurídicos:**
   - Seguir o guia em `LEGAL_WORKFLOW_GUIDE.md`

---

## 🆘 Suporte

Para problemas ou dúvidas:
1. Verificar logs: `tail -f /opt/odoo/logs/odoo.log`
2. Consultar documentação oficial: https://www.odoo.com/documentation/17.0/
3. Comunidade Odoo: https://github.com/odoo/odoo/discussions

---

*Última atualização: Janeiro 2026*
