#!/bin/bash

################################################################################
# Script de Backup: Odoo 17 CRM + PostgreSQL + Filestore
# Ambiente: Ubuntu 20.04 LTS / 22.04 LTS (sem Docker)
# Uso: bash backup.sh
# Agendamento: crontab -e
# Exemplo: 0 1 * * * /opt/odoo/backup.sh >> /opt/odoo/logs/backup.log 2>&1
################################################################################

set -e

# Configurações
ODOO_HOME="/opt/odoo"
BACKUP_DIR="$ODOO_HOME/backups"
POSTGRES_USER="odoo"
POSTGRES_DB="odoo"
BACKUP_RETENTION_DAYS=7
BACKUP_RETENTION_WEEKS=4
BACKUP_RETENTION_MONTHS=6

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DATE=$(date +%Y%m%d)
WEEK=$(date +%Y_W%V)
MONTH=$(date +%Y%m)

# Criar diretório de backup se não existir
mkdir -p $BACKUP_DIR
mkdir -p $BACKUP_DIR/database
mkdir -p $BACKUP_DIR/filestore
mkdir -p $BACKUP_DIR/logs

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Iniciando Backup - $TIMESTAMP${NC}"
echo -e "${GREEN}========================================${NC}"

# 1. Backup do Banco de Dados PostgreSQL
echo -e "\n${YELLOW}[1/3] Fazendo backup do banco de dados...${NC}"
BACKUP_DB_FILE="$BACKUP_DIR/database/odoo_${TIMESTAMP}.sql.gz"

pg_dump -U $POSTGRES_USER -d $POSTGRES_DB | gzip > $BACKUP_DB_FILE

if [ -f "$BACKUP_DB_FILE" ]; then
    SIZE=$(du -h $BACKUP_DB_FILE | cut -f1)
    echo -e "${GREEN}✓ Backup do BD concluído: $SIZE${NC}"
else
    echo -e "${RED}✗ Erro ao fazer backup do BD${NC}"
    exit 1
fi

# 2. Backup do Filestore (PDFs e Documentos)
echo -e "\n${YELLOW}[2/3] Fazendo backup do filestore (PDFs)...${NC}"
BACKUP_FILESTORE_FILE="$BACKUP_DIR/filestore/filestore_${TIMESTAMP}.tar.gz"

if [ -d "$ODOO_HOME/data" ]; then
    tar -czf $BACKUP_FILESTORE_FILE -C $ODOO_HOME data/ 2>/dev/null || true
    
    if [ -f "$BACKUP_FILESTORE_FILE" ]; then
        SIZE=$(du -h $BACKUP_FILESTORE_FILE | cut -f1)
        echo -e "${GREEN}✓ Backup do filestore concluído: $SIZE${NC}"
    else
        echo -e "${YELLOW}⚠ Aviso: Filestore vazio ou erro ao compactar${NC}"
    fi
else
    echo -e "${YELLOW}⚠ Diretório de dados não encontrado${NC}"
fi

# 3. Limpeza de backups antigos
echo -e "\n${YELLOW}[3/3] Limpando backups antigos...${NC}"

# Manter últimos 7 dias
find $BACKUP_DIR/database -name "odoo_*.sql.gz" -mtime +$BACKUP_RETENTION_DAYS -delete
find $BACKUP_DIR/filestore -name "filestore_*.tar.gz" -mtime +$BACKUP_RETENTION_DAYS -delete

echo -e "${GREEN}✓ Limpeza concluída${NC}"

# Relatório final
echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}Backup Concluído com Sucesso!${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "\n${YELLOW}Resumo:${NC}"
echo "  Banco de Dados: $BACKUP_DB_FILE"
echo "  Filestore: $BACKUP_FILESTORE_FILE"
echo "  Diretório: $BACKUP_DIR"
echo ""
echo -e "${YELLOW}Próximo backup: $(date -d '+1 day' '+%d/%m/%Y às %H:%M')${NC}"
echo ""
