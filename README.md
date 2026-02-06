# Odoo CRM Jurídico - Araújo & França Advocacia ⚖️

Este repositório contém a infraestrutura completa e independente para a implantação do **Odoo CRM Community Edition**, customizado para as necessidades da **Araújo & França Advocacia**. O sistema foi projetado para centralizar a gestão de clientes, processos e documentos, integrando-se ao site oficial do escritório.

---

## 🚀 Guia de Início Rápido

Escolha a opção que melhor se adequa ao seu ambiente:

### Opção 1: Com Docker (Recomendado para VPS dedicados)

**Pré-requisitos:**
*   Sistema Operacional: **Ubuntu Server 22.04 LTS**
*   Ferramentas: **Docker** e **Docker Compose** instalados

**Instalação:**
```bash
git clone https://github.com/MuriloRip/odoo-crm-deployment.git
cd odoo-crm-deployment
docker-compose up -d
```

Acesse em: `http://localhost:8069` (ou o IP do servidor na rede)

---

### Opção 2: Sem Docker (Recomendado para servidores compartilhados)

**Pré-requisitos:**
*   Sistema Operacional: **Ubuntu Server 20.04 LTS ou 22.04 LTS**
*   Acesso SSH com privilégios sudo

**Instalação:**
```bash
git clone https://github.com/MuriloRip/odoo-crm-deployment.git
cd odoo-crm-deployment
sudo bash install.sh
```

Acesse em: `http://seu-servidor:8069`

**Para detalhes completos, consulte:** [INSTALL_NO_DOCKER.md](INSTALL_NO_DOCKER.md)

---

## 🏗️ Estrutura do Projeto

*   `docker-compose.yml`: Configuração da orquestração entre o Odoo (Web) e o PostgreSQL (Banco de Dados).
*   `install.sh`: Script de instalação automatizado para Ubuntu (sem Docker).
*   `backup.sh`: Script de backup automatizado para banco de dados e filestore.
*   `/config`: Contém o arquivo `odoo.conf` para ajustes finos do sistema.
*   `/addons`: Pasta destinada a módulos personalizados.
    *   `odoo_juridico_custom`: Módulo principal de CRM jurídico.
    *   `odoo_non_client_management`: Novo módulo para gestão de contatos externos e transações avulsas.
*   `LICENSE_ANALYSIS.md`: Documento detalhado sobre as licenças LGPLv3 vs AGPLv3.
*   `SITE_INTEGRATION_GUIDE.md`: Guia técnico para conectar o site [araujoefranca.com.br](https://araujoefranca.com.br/) ao CRM.
*   `LEGAL_WORKFLOW_GUIDE.md`: Guia de customização de fluxos jurídicos, faturamento e segurança.
*   `INSTALL_NO_DOCKER.md`: Guia completo de instalação sem Docker para servidores compartilhados.

---

## 🛡️ Segurança e Licenciamento (LGPLv3)

Conforme analisado, o uso do **Odoo Community (LGPLv3)** garante que:
1.  **Privacidade do Código:** Módulos personalizados criados para o escritório **não** precisam ser compartilhados publicamente.
2.  **Soberania de Dados:** O banco de dados PostgreSQL é independente e os dados pertencem exclusivamente ao escritório.
3.  **Independência:** O projeto não possui vínculos com plataformas proprietárias, podendo ser movido para qualquer provedor de nuvem (AWS, DigitalOcean, Google Cloud) no futuro.

---

## 📈 Próximos Passos
- [x] Configuração de Backup Automático do PostgreSQL (Implementado via container dedicado ou script).
- [x] Backup Automático do Filestore/PDFs (Implementado).
- [x] Implementação de SSL (HTTPS) via Nginx Reverse Proxy (Configuração pronta em `./nginx`).
- [x] Instalação sem Docker para servidores compartilhados (Script automatizado).
- [x] Customização dos módulos de CRM e Faturamento para o fluxo do escritório (Guia em `LEGAL_WORKFLOW_GUIDE.md`).
- [x] Suporte a Localização Brasileira (L10n-Brazil) para conformidade fiscal.

---

## 🧩 Como Adicionar Novos Módulos (Custom Addons)

O Odoo é modular e você pode adicionar novas funcionalidades (como módulos específicos para advocacia da OCA) seguindo estes passos:

1.  **Baixe o Módulo:** Obtenha a pasta do módulo desejado (geralmente um arquivo .zip que você deve extrair).
2.  **Mova para a Pasta Addons:** Coloque a pasta do módulo dentro do diretório `/addons` deste projeto.
3.  **Reinicie o Sistema:** 
    - **Com Docker:** `docker-compose restart web`
    - **Sem Docker:** `systemctl restart odoo`
4.  **Ative no Painel:** 
    *   Acesse o Odoo como Administrador.
    *   Vá em **Configurações** e ative o **Modo Desenvolvedor**.
    *   Vá no menu **Aplicativos** e clique em **Atualizar Lista de Aplicativos**.
    *   Procure o novo módulo e clique em **Instalar**.

---

*Desenvolvido para o projeto de modernização do escritório.*
