#!/usr/bin/env python3

################################################################################
# Script de Configuração: Pré-configura Estágios Jurídicos no Odoo CRM
# Uso: python3 setup_stages.py
# Pré-requisitos: Odoo já instalado e rodando, módulo CRM ativado
################################################################################

import xmlrpc.client
import sys
import time

# Configurações
ODOO_URL = "http://localhost:8069"
ODOO_DB = "odoo"
ODOO_USER = "admin"
ODOO_PASSWORD = "admin"

# Estágios jurídicos pré-configurados
LEGAL_STAGES = [
    {
        "name": "Novo Contato",
        "sequence": 1,
        "probability": 10,
        "description": "Leads vindos do site ou WhatsApp",
    },
    {
        "name": "Consulta Inicial",
        "sequence": 2,
        "probability": 30,
        "description": "Reunião agendada para entender o caso",
    },
    {
        "name": "Análise de Viabilidade",
        "sequence": 3,
        "probability": 50,
        "description": "Estudo jurídico do caso e análise de provas",
    },
    {
        "name": "Proposta de Honorários",
        "sequence": 4,
        "probability": 75,
        "description": "Contrato de prestação de serviços enviado",
    },
    {
        "name": "Contrato Assinado",
        "sequence": 5,
        "probability": 100,
        "description": "Cliente fechado, pronto para ajuizar processo",
    },
]

def connect_odoo():
    """Conecta ao Odoo via XML-RPC"""
    try:
        common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
        uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})
        
        if not uid:
            print("❌ Erro: Autenticação falhou. Verifique credenciais.")
            sys.exit(1)
        
        models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")
        return models, uid
    except Exception as e:
        print(f"❌ Erro ao conectar ao Odoo: {e}")
        print("   Certifique-se de que o Odoo está rodando em http://localhost:8069")
        sys.exit(1)

def check_crm_module(models, uid):
    """Verifica se o módulo CRM está instalado"""
    try:
        modules = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            "ir.module.module", "search",
            [["name", "=", "crm"], ["state", "=", "installed"]]
        )
        return len(modules) > 0
    except Exception as e:
        print(f"❌ Erro ao verificar módulo CRM: {e}")
        return False

def get_default_team(models, uid):
    """Obtém a equipe padrão de vendas"""
    try:
        teams = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            "crm.team", "search",
            [["name", "=", "Sales"]],
            {"limit": 1}
        )
        
        if teams:
            return teams[0]
        
        # Se não existir, cria uma equipe padrão
        team_id = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            "crm.team", "create",
            [{
                "name": "Equipe Jurídica",
                "sequence": 1,
            }]
        )
        return team_id
    except Exception as e:
        print(f"⚠️  Aviso: Não foi possível obter equipe padrão: {e}")
        return None

def delete_default_stages(models, uid, team_id):
    """Deleta os estágios padrão do Odoo"""
    try:
        stages = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            "crm.stage", "search",
            [["team_id", "=", team_id]]
        )
        
        if stages:
            models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                "crm.stage", "unlink",
                [stages]
            )
            print(f"✓ {len(stages)} estágios padrão deletados")
    except Exception as e:
        print(f"⚠️  Aviso ao deletar estágios padrão: {e}")

def create_stages(models, uid, team_id):
    """Cria os estágios jurídicos pré-configurados"""
    created = 0
    
    for stage in LEGAL_STAGES:
        try:
            stage_data = {
                "name": stage["name"],
                "sequence": stage["sequence"],
                "probability": stage["probability"],
                "description": stage["description"],
                "team_id": team_id,
                "fold": False,
            }
            
            stage_id = models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                "crm.stage", "create",
                [stage_data]
            )
            
            print(f"✓ Estágio criado: {stage['name']} (ID: {stage_id})")
            created += 1
            
        except Exception as e:
            print(f"❌ Erro ao criar estágio '{stage['name']}': {e}")
    
    return created

def main():
    print("=" * 60)
    print("Configuração de Estágios Jurídicos - Odoo CRM")
    print("=" * 60)
    print()
    
    # Conectar ao Odoo
    print("🔌 Conectando ao Odoo...")
    models, uid = connect_odoo()
    print("✓ Conectado com sucesso")
    print()
    
    # Verificar módulo CRM
    print("📦 Verificando módulo CRM...")
    if not check_crm_module(models, uid):
        print("❌ Erro: Módulo CRM não está instalado")
        print("   Instale o módulo CRM antes de executar este script")
        sys.exit(1)
    print("✓ Módulo CRM está instalado")
    print()
    
    # Obter equipe padrão
    print("👥 Obtendo equipe padrão...")
    team_id = get_default_team(models, uid)
    if not team_id:
        print("❌ Erro: Não foi possível obter ou criar equipe")
        sys.exit(1)
    print(f"✓ Equipe ID: {team_id}")
    print()
    
    # Deletar estágios padrão
    print("🗑️  Deletando estágios padrão...")
    delete_default_stages(models, uid, team_id)
    print()
    
    # Criar estágios jurídicos
    print("✨ Criando estágios jurídicos...")
    created = create_stages(models, uid, team_id)
    print()
    
    # Resumo
    print("=" * 60)
    print(f"✓ Configuração Concluída!")
    print(f"  {created} estágios jurídicos criados com sucesso")
    print()
    print("📋 Estágios criados:")
    for i, stage in enumerate(LEGAL_STAGES, 1):
        print(f"  {i}. {stage['name']}")
    print()
    print("🚀 Próximos passos:")
    print("  1. Acesse http://localhost:8069")
    print("  2. Vá em CRM → Funil de Vendas")
    print("  3. Veja os estágios jurídicos pré-configurados")
    print("  4. Customize conforme necessário")
    print("=" * 60)

if __name__ == "__main__":
    main()
