"""
Example: Testing GitHub Tools Integration
This script demonstrates how the Developer agent can use GitHub tools
to research, analyze, and learn from existing projects.
"""

import os
from dotenv import load_dotenv
from crew import run_it_squad


def example_github_research():
    """
    Example: Using GitHub tools to research a project.
    
    This example shows how the squad can use GitHub integration to:
    - Search for similar projects
    - Analyze code structure
    - Learn from existing implementations
    - Find best practices
    """
    
    # Check if GitHub is configured
    load_dotenv()
    if not os.getenv("GITHUB_TOKEN") and not os.getenv("GITHUB_APP_ID"):
        print("⚠️  GitHub credentials not configured!")
        print("Please add GITHUB_TOKEN to your .env file to run this example.")
        print("See README.md for instructions on how to get a GitHub token.")
        return
    
    project_description = """
    Desenvolver uma API REST de autenticação com JWT em Python usando FastAPI.
    
    Antes de começar a implementação, o Developer deve:
    
    1. PESQUISAR projetos similares no GitHub:
       - Buscar exemplos de "fastapi jwt authentication"
       - Analisar repositórios populares com autenticação JWT
       - Identificar as melhores práticas e padrões comuns
    
    2. ANALISAR estruturas de projeto:
       - Examinar como projetos similares organizam seus arquivos
       - Verificar estruturas de diretórios recomendadas
       - Entender padrões de arquitetura usados
    
    3. ESTUDAR implementações específicas:
       - Ler código de funções de autenticação
       - Entender como tokens são gerados e validados
       - Ver exemplos de middleware de autenticação
    
    4. DOCUMENTAR achados:
       - Listar bibliotecas mais usadas
       - Documentar padrões de segurança encontrados
       - Compilar exemplos de código úteis
    
    Requisitos técnicos:
    - FastAPI como framework web
    - JWT para autenticação
    - Bcrypt para hash de senhas
    - SQLAlchemy para banco de dados
    - Pydantic para validação
    - Documentação completa com Swagger/OpenAPI
    
    O squad deve usar as ferramentas do GitHub para pesquisar e aprender
    com projetos existentes antes de propor a implementação.
    """
    
    print("="*80)
    print("🔍 Exemplo: Pesquisa e Análise com GitHub Tools")
    print("="*80)
    print("\nEste exemplo demonstra como o Developer agent usa GitHub tools para:")
    print("  • Buscar projetos similares")
    print("  • Analisar estruturas de código")
    print("  • Aprender com implementações existentes")
    print("  • Identificar melhores práticas")
    print("\n" + "="*80 + "\n")
    
    result = run_it_squad(project_description)
    
    print("\n" + "="*80)
    print("✅ Exemplo concluído!")
    print("="*80)
    print("\nO squad usou GitHub tools para pesquisar e analisar projetos existentes")
    print("antes de criar a arquitetura e plano de implementação.")
    print("\nConfira os resultados acima para ver como o Developer agent")
    print("utilizou as ferramentas do GitHub para pesquisar e aprender!")
    
    return result


def example_code_search():
    """
    Simple example: Search for code examples on GitHub.
    
    This is a simpler example that just asks the agent to search for
    specific code patterns on GitHub.
    """
    
    # Check if GitHub is configured
    load_dotenv()
    if not os.getenv("GITHUB_TOKEN") and not os.getenv("GITHUB_APP_ID"):
        print("⚠️  GitHub credentials not configured!")
        print("Please add GITHUB_TOKEN to your .env file to run this example.")
        return
    
    project_description = """
    Tarefa simples: Pesquisar exemplos de código no GitHub.
    
    O Developer deve usar as ferramentas do GitHub para:
    
    1. Buscar repositórios Python com autenticação JWT
    2. Encontrar 3-5 repositórios mais populares
    3. Para cada repositório encontrado:
       - Obter informações básicas (estrelas, descrição, linguagem)
       - Listar os arquivos principais
       - Se possível, ler um arquivo de exemplo (como README.md ou main.py)
    
    4. Criar um resumo com:
       - Lista de repositórios encontrados
       - Principais características de cada um
       - Recomendações de qual examinar mais a fundo
    
    NÃO é necessário implementar nada, apenas pesquisar e documentar.
    """
    
    print("="*80)
    print("🔎 Exemplo: Busca Simples de Código no GitHub")
    print("="*80)
    print("\nO Developer agent vai usar GitHub tools para pesquisar e analisar")
    print("repositórios de exemplo relacionados a autenticação JWT em Python.")
    print("\n" + "="*80 + "\n")
    
    result = run_it_squad(project_description)
    
    print("\n" + "="*80)
    print("✅ Pesquisa concluída!")
    print("="*80)
    
    return result


if __name__ == "__main__":
    print("\n💡 GitHub Integration Examples\n")
    print("Choose which example to run:\n")
    print("1. example_github_research() - Full project with GitHub research")
    print("2. example_code_search() - Simple code search example")
    print("\nUncomment one of the lines below to run an example:\n")
    
    # Uncomment one of these to run:
    # example_github_research()
    # example_code_search()
    
    print("Tip: Make sure you have GITHUB_TOKEN configured in your .env file!")
