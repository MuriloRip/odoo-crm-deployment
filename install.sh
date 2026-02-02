#!/bin/bash

################################################################################
# Script de Instalação Automatizado: Odoo 17 CRM para Araújo & França Advocacia
# Ambiente: Ubuntu 22.04 LTS (sem Docker)
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
echo -e "${GREEN}Instalação Automatizada do Odoo 17 CRM${NC}"
echo -e "${GREEN}Araújo & França Advocacia${NC}"
echo -e "${GREEN}========================================${NC}"

# Verificar se é root
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}Este script deve ser executado como root (use sudo)${NC}"
   exit 1
fi

# 1. Atualizar sistema
echo -e "\n${YELLOW}[1/9] Atualizando sistema...${NC}"
apt-get update
apt-get upgrade -y

# 2. Instalar dependências do sistema (incluindo correções para Odoo 17)
echo -e "\n${YELLOW}[2/9] Instalando dependências do sistema...${NC}"
apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    python3.11-dev \
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
    libxcb1 \
    libldap2-dev \
    libsasl2-dev \
    net-tools

# Iniciar PostgreSQL se não estiver rodando
service postgresql start

# 3. Criar usuário Odoo
echo -e "\n${YELLOW}[3/9] Criando usuário Odoo...${NC}"
if id "$ODOO_USER" &>/dev/null; then
    echo "Usuário $ODOO_USER já existe"
else
    useradd -m -d $ODOO_HOME -s /bin/bash $ODOO_USER
    echo -e "${GREEN}Usuário $ODOO_USER criado${NC}"
fi

# 4. Configurar PostgreSQL
echo -e "\n${YELLOW}[4/9] Configurando PostgreSQL...${NC}"
sudo -u postgres psql <<EOF
DO \$$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = '$POSTGRES_USER') THEN
        CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';
    END IF;
END
\$$;
ALTER USER $POSTGRES_USER WITH SUPERUSER;
ALTER ROLE $POSTGRES_USER SET client_encoding TO 'utf8';
ALTER ROLE $POSTGRES_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $POSTGRES_USER SET default_transaction_deferrable TO on;
EOF

# Criar banco de dados se não existir
sudo -u postgres psql -tc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRES_DB'" | grep -q 1 || sudo -u postgres psql -c "CREATE DATABASE $POSTGRES_DB OWNER $POSTGRES_USER"

echo -e "${GREEN}PostgreSQL configurado e Banco de Dados criado${NC}"

# 5. Clonar Odoo
echo -e "\n${YELLOW}[5/9] Clonando Odoo 17...${NC}"
if [ ! -d "$ODOO_HOME/odoo" ]; then
    sudo -u $ODOO_USER git clone --depth 1 --branch $ODOO_VERSION https://github.com/odoo/odoo.git $ODOO_HOME/odoo
    echo -e "${GREEN}Odoo clonado${NC}"
else
    echo "Odoo já existe em $ODOO_HOME/odoo"
fi

# 6. Criar ambiente virtual e instalar dependências Python
echo -e "\n${YELLOW}[6/9] Instalando dependências Python...${NC}"
if [ ! -d "$ODOO_HOME/venv" ]; then
    sudo -u $ODOO_USER python3 -m venv $ODOO_HOME/venv
fi
source $ODOO_HOME/venv/bin/activate

# Upgrade pip
sudo -u $ODOO_USER $ODOO_HOME/venv/bin/pip install --upgrade pip setuptools wheel

# Instalar requirements do Odoo
sudo -u $ODOO_USER $ODOO_HOME/venv/bin/pip install -r $ODOO_HOME/odoo/requirements.txt

# Instalar dependências adicionais
sudo -u $ODOO_USER $ODOO_HOME/venv/bin/pip install psycopg2-binary wkhtmltopdf

echo -e "${GREEN}Dependências Python instaladas${NC}"

# 7. Criar diretórios e configurar permissões
echo -e "\n${YELLOW}[7/9] Criando diretórios e configurando permissões...${NC}"
mkdir -p $ODOO_HOME/addons
mkdir -p $ODOO_HOME/backups
mkdir -p $ODOO_HOME/logs
mkdir -p $ODOO_HOME/data
mkdir -p /etc/odoo

chown -R $ODOO_USER:$ODOO_USER $ODOO_HOME
chown -R $ODOO_USER:$ODOO_USER /etc/odoo
chmod 755 $ODOO_HOME

# 8. Criar arquivo de configuração
echo -e "\n${YELLOW}[8/9] Criando arquivo de configuração...${NC}"
cat > /etc/odoo/odoo.conf <<EOF
[options]
addons_path = $ODOO_HOME/addons,$ODOO_HOME/odoo/addons
data_dir = $ODOO_HOME/data
admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = $POSTGRES_USER
db_password = $POSTGRES_PASSWORD
db_name = $POSTGRES_DB
server_wide_modules = base,web
workers = 0
max_cron_threads = 1
limit_time_real = 3600
limit_time_cpu = 600
logfile = $ODOO_HOME/logs/odoo.log
log_level = info
EOF

chown $ODOO_USER:$ODOO_USER /etc/odoo/odoo.conf
chmod 640 /etc/odoo/odoo.conf

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
systemctl restart odoo

echo -e "${GREEN}Serviço Odoo configurado e iniciado${NC}"

# 9. Inicializar Banco de Dados e Configurar Estágios
echo -e "\n${YELLOW}[9/9] Inicializando CRM e Estágios Jurídicos...${NC}"
echo "Aguardando o servidor iniciar (10s)..."
sleep 10

# Inicializar módulos base e crm
sudo -u $ODOO_USER $ODOO_HOME/venv/bin/python $ODOO_HOME/odoo/odoo-bin -c /etc/odoo/odoo.conf -i base,crm --stop-after-init

# Copiar e executar script de estágios
cp setup_stages.py $ODOO_HOME/
chown $ODOO_USER:$ODOO_USER $ODOO_HOME/setup_stages.py
sudo -u $ODOO_USER $ODOO_HOME/venv/bin/python $ODOO_HOME/setup_stages.py

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}✓ Instalação e Configuração Concluídas!${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "\n${YELLOW}Acesso ao Sistema:${NC}"
echo "  URL: http://localhost:8069"
echo "  Usuário: admin"
echo "  Senha: admin"
echo ""
echo -e "${YELLOW}Status do Serviço:${NC}"
echo "  systemctl status odoo"
echo ""
echo -e "${GREEN}O CRM já está com os estágios jurídicos configurados!${NC}"
