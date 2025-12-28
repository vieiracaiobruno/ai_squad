"""
Example script showing how to use the IT Squad with different project types.
"""

from crew import run_it_squad


def example_web_app():
    """Example: Building a web application"""
    project_description = """
    Criar uma aplicação web de blog pessoal com:
    - Sistema de posts com título, conteúdo e tags
    - Comentários em posts
    - Sistema de busca
    - Interface responsiva
    - Painel administrativo
    """
    
    print("\n🌐 Exemplo: Aplicação Web de Blog")
    return run_it_squad(project_description)


def example_api_service():
    """Example: Building an API service"""
    project_description = """
    Desenvolver uma API RESTful para gerenciamento de usuários:
    - CRUD completo de usuários
    - Autenticação JWT
    - Níveis de permissão (admin, user)
    - Rate limiting
    - Documentação OpenAPI/Swagger
    - Logs estruturados
    """
    
    print("\n🔌 Exemplo: API RESTful")
    return run_it_squad(project_description)


def example_data_pipeline():
    """Example: Building a data pipeline"""
    project_description = """
    Construir um pipeline de dados para análise:
    - Ingestão de dados de múltiplas fontes
    - Limpeza e transformação de dados
    - Armazenamento em data warehouse
    - Criação de dashboards
    - Agendamento automatizado
    - Alertas e monitoramento
    """
    
    print("\n📊 Exemplo: Pipeline de Dados")
    return run_it_squad(project_description)


def example_automation_tool():
    """Example: Building an automation tool"""
    project_description = """
    Desenvolver ferramenta de automação DevOps:
    - Scripts de deploy automatizado
    - Monitoramento de serviços
    - Backup automatizado
    - Gerenciamento de configurações
    - Interface CLI
    - Notificações de status
    """
    
    print("\n🤖 Exemplo: Ferramenta de Automação")
    return run_it_squad(project_description)


if __name__ == "__main__":
    # Escolha qual exemplo executar descomentando a linha correspondente
    
    # example_web_app()
    # example_api_service()
    # example_data_pipeline()
    # example_automation_tool()
    
    print("\n💡 Descomente uma das funções acima para executar um exemplo!")
    print("Ou modifique main.py com seu próprio projeto.")
