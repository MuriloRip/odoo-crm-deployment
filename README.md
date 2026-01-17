# Odoo CRM Jurídico - Araújo & França Advocacia ⚖️

Este repositório contém a infraestrutura completa e independente para a implantação do **Odoo CRM Community Edition**, customizado para as necessidades da **Araújo & França Advocacia**. O sistema foi projetado para centralizar a gestão de clientes, processos e documentos, integrando-se ao site oficial do escritório.

---

## 🚀 Guia de Início Rápido (Servidor de Testes)

Para rodar o sistema no notebook de testes, siga os passos abaixo:

### 1. Pré-requisitos
*   Sistema Operacional: Recomendamos **Ubuntu Server 22.04 LTS**.
*   Ferramentas: **Docker** e **Docker Compose** instalados.

### 2. Instalação
Clone este repositório no servidor:
```bash
git clone https://github.com/MuriloRip/odoo-crm-deployment.git
cd odoo-crm-deployment
```

Suba o sistema com um único comando:
```bash
docker-compose up -d
```

O sistema estará disponível em: `http://localhost:8069` (ou o IP do notebook na rede).

---

## 🏗️ Estrutura do Projeto

*   `docker-compose.yml`: Configuração da orquestração entre o Odoo (Web) e o PostgreSQL (Banco de Dados).
*   `/config`: Contém o arquivo `odoo.conf` para ajustes finos do sistema.
*   `/addons`: Pasta destinada a módulos personalizados ou da comunidade (OCA).
*   `LICENSE_ANALYSIS.md`: Documento detalhado sobre as licenças LGPLv3 vs AGPLv3.
*   `SITE_INTEGRATION_GUIDE.md`: Guia técnico para conectar o site [araujoefranca.com.br](https://araujoefranca.com.br/) ao CRM.

---

## 🛡️ Segurança e Licenciamento (LGPLv3)

Conforme analisado, o uso do **Odoo Community (LGPLv3)** garante que:
1.  **Privacidade do Código:** Módulos personalizados criados para o escritório **não** precisam ser compartilhados publicamente.
2.  **Soberania de Dados:** O banco de dados PostgreSQL é independente e os dados pertencem exclusivamente ao escritório.
3.  **Independência:** O projeto não possui vínculos com plataformas proprietárias, podendo ser movido para qualquer provedor de nuvem (AWS, DigitalOcean, Google Cloud) no futuro.

---

## 📈 Próximos Passos
- [ ] Configuração de Backup Automático do PostgreSQL.
- [ ] Implementação de SSL (HTTPS) via Nginx Reverse Proxy.
- [ ] Customização dos módulos de CRM e Faturamento para o fluxo do escritório.

---
*Desenvolvido para o projeto de modernização do escritório.*
