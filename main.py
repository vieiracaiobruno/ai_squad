"""
Main execution script for the IT Squad with CrewAI
"""

import os
from dotenv import load_dotenv
from crew import run_it_squad


def main():
    """
    Main function to run the IT squad.
    """
    # Load environment variables
    load_dotenv()
    
    # Check for required environment variables
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Erro: OPENAI_API_KEY não encontrada!")
        print("Por favor, configure sua chave API no arquivo .env")
        return
    
    if not os.getenv("GITHUB_TOKEN"):
        print("⚠️  Aviso: GITHUB_TOKEN não encontrado!")
        print("As ferramentas do GitHub podem não funcionar corretamente.")
        print("Por favor, configure seu token do GitHub no arquivo .env")
    
    # Project description - you can customize this
    project_description = """
    Desenvolver uma aplicação web de gerenciamento de tarefas (TODO app) com as seguintes características:
    
    - Backend em Python usando FastAPI
    - Banco de dados SQLite para persistência
    - API RESTful com endpoints para CRUD de tarefas
    - Autenticação básica de usuários
    - Frontend simples em HTML/CSS/JavaScript
    - Testes unitários e de integração
    - Documentação da API
    - README com instruções de instalação e uso
    
    O projeto deve seguir boas práticas de desenvolvimento, incluindo:
    - Código limpo e bem documentado
    - Arquitetura modular
    - Tratamento de erros adequado
    - Validação de dados
    - Segurança básica
    """
    
    # Run the IT squad
    result = run_it_squad(project_description)
    
    # Print the final result
    print("\n📊 Resultado Final:")
    print("="*80)
    print(result)
    print("="*80)


if __name__ == "__main__":
    main()
