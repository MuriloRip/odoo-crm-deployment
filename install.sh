#!/bin/bash

################################################################################
# Script de Instalação: Odoo 17 CRM para Araújo & França Advocacia
# Ambiente: Ubuntu 20.04 LTS / 22.04 LTS (sem Docker)
# Uso: sudo bash install.sh
################################################################################

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configurações
ODOO_USER="odoo"
ODOO_HOME="/opt/odoo"
ODOO_VERSION="17.0"
POSTGRES_USER="odoo"
POSTGRES_PASSWORD="odoo_password"
POSTGRES_DB="odoo"

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Instalação do Odoo 17 CRM${NC}"
echo -e "${GREEN}Araújo & França Advocacia${NC}"
echo -e "${GREEN}========================================${NC}"

# Verificar se é root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}Este script deve ser executado como root (use sudo)${NC}"
   exit 1
fi

# 1. Atualizar sistema
echo -e "\n${YELLOW}[1/8] Atualizando sistema...${NC}"
apt-get update
apt-get upgrade -y

# 2. Instalar dependências do sistema
echo -e "\n${YELLOW}[2/8] Instalando dependências do sistema...${NC}"
apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    postgresql \
    postgresql-contrib \
    postgresql-client \
    git \
    curl \
    wget \
    nginx \
    supervisor \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    python3-tk \
    libharfbuzz0b \
    libfribidi0 \
    libxcb1

# 3. Criar usuário Odoo
echo -e "\n${YELLOW}[3/8] Criando usuário Odoo...${NC}"
if id "$ODOO_USER" &>/dev/null; then
    echo "Usuário $ODOO_USER já existe"
else
    useradd -m -d $ODOO_HOME -s /bin/bash $ODOO_USER
    echo -e "${GREEN}Usuário $ODOO_USER criado${NC}"
fi

# 4. Configurar PostgreSQL
echo -e "\n${YELLOW}[4/8] Configurando PostgreSQL...${NC}"
sudo -u postgres psql <<EOF
CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';
ALTER ROLE $POSTGRES_USER SET client_encoding TO 'utf8';
ALTER ROLE $POSTGRES_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $POSTGRES_USER SET default_transaction_deferrable TO on;
ALTER ROLE $POSTGRES_USER SET default_transaction_level TO 'read committed';
ALTER ROLE $POSTGRES_USER CREATEDB;
EOF

echo -e "${GREEN}PostgreSQL configurado${NC}"

# 5. Clonar Odoo
echo -e "\n${YELLOW}[5/8] Clonando Odoo 17...${NC}"
if [ ! -d "$ODOO_HOME/odoo" ]; then
    sudo -u $ODOO_USER git clone --depth 1 --branch $ODOO_VERSION https://github.com/odoo/odoo.git $ODOO_HOME/odoo
    echo -e "${GREEN}Odoo clonado${NC}"
else
    echo "Odoo já existe em $ODOO_HOME/odoo"
fi

# 6. Criar ambiente virtual e instalar dependências Python
echo -e "\n${YELLOW}[6/8] Instalando dependências Python...${NC}"
sudo -u $ODOO_USER python3 -m venv $ODOO_HOME/venv
source $ODOO_HOME/venv/bin/activate

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Instalar requirements do Odoo
pip install -r $ODOO_HOME/odoo/requirements.txt

# Instalar dependências adicionais
pip install psycopg2-binary wkhtmltopdf

echo -e "${GREEN}Dependências Python instaladas${NC}"

# 7. Criar diretórios e configurar permissões
echo -e "\n${YELLOW}[7/8] Criando diretórios e configurando permissões...${NC}"
mkdir -p $ODOO_HOME/addons
mkdir -p $ODOO_HOME/backups
mkdir -p $ODOO_HOME/logs
mkdir -p /etc/odoo

chown -R $ODOO_USER:$ODOO_USER $ODOO_HOME
chown -R $ODOO_USER:$ODOO_USER /etc/odoo
chmod 755 $ODOO_HOME

# 8. Criar arquivo de configuração
echo -e "\n${YELLOW}[8/8] Criando arquivo de configuração...${NC}"
cat > /etc/odoo/odoo.conf <<EOF
[options]
addons_path = $ODOO_HOME/addons,$ODOO_HOME/odoo/addons
data_dir = $ODOO_HOME/data
admin_passwd = admin_password_change_me
db_host = localhost
db_port = 5432
db_user = $POSTGRES_USER
db_password = $POSTGRES_PASSWORD
db_name = $POSTGRES_DB
server_wide_modules = base,web,l10n_br_base
workers = 4
worker_type = wsgi
max_cron_threads = 2
limit_time_real = 3600
limit_time_cpu = 600
logfile = $ODOO_HOME/logs/odoo.log
log_level = info
EOF

chown $ODOO_USER:$ODOO_USER /etc/odoo/odoo.conf
chmod 640 /etc/odoo/odoo.conf

echo -e "${GREEN}Arquivo de configuração criado${NC}"

# Criar arquivo de serviço systemd
cat > /etc/systemd/system/odoo.service <<EOF
[Unit]
Description=Odoo 17 CRM - Araújo & França Advocacia
After=network.target postgresql.service

[Service]
Type=simple
User=$ODOO_USER
Group=$ODOO_USER
WorkingDirectory=$ODOO_HOME/odoo
Environment="PATH=$ODOO_HOME/venv/bin"
ExecStart=$ODOO_HOME/venv/bin/python $ODOO_HOME/odoo/odoo-bin -c /etc/odoo/odoo.conf
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable odoo
systemctl start odoo

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}✓ Instalação Concluída!${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "\n${YELLOW}Próximos passos:${NC}"
echo "1. Acessar: http://localhost:8069"
echo "2. Criar novo banco de dados"
echo "3. Usuário padrão: admin"
echo "4. Senha padrão: admin"
echo ""
echo -e "${YELLOW}Comandos úteis:${NC}"
echo "  Ver status: systemctl status odoo"
echo "  Reiniciar: systemctl restart odoo"
echo "  Ver logs: tail -f $ODOO_HOME/logs/odoo.log"
echo ""
echo -e "${YELLOW}Configurar Nginx (Proxy Reverso):${NC}"
echo "  Editar: /etc/nginx/sites-available/odoo"
echo "  Ativar: ln -s /etc/nginx/sites-available/odoo /etc/nginx/sites-enabled/"
echo "  Testar: nginx -t"
echo "  Recarregar: systemctl reload nginx"
echo ""
echo -e "${YELLOW}Pre-configurar Estágios Jurídicos:${NC}"
echo "  1. Instale o módulo CRM no Odoo"
echo "  2. Execute: python3 $ODOO_HOME/setup_stages.py"
echo "  3. Os 5 estágios jurídicos serão criados automaticamente"
echo ""
