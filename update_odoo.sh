#!/bin/bash

# Script para atualizar o repositório e reiniciar o Odoo
echo "Atualizando repositório Git..."
git pull origin main

echo "Ajustando permissões dos addons..."
chmod -R 755 addons/

echo "Reiniciando o serviço do Odoo..."
if [ -f "docker-compose.yml" ]; then
    docker-compose restart web
    echo "Docker restart executado."
else
    sudo systemctl restart odoo
    echo "Systemd restart executado."
fi

echo "Processo concluído! Lembre-se de atualizar a lista de apps no Odoo."
