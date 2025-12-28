"""
IT Squad Tasks Definition
This module defines the tasks for the IT squad workflow.
"""

from crewai import Task
from agents import (
    create_project_manager,
    create_tech_lead,
    create_developer,
    create_tester
)


def create_planning_task(project_description: str) -> Task:
    """
    Creates the project planning task for the Project Manager.
    """
    return Task(
        description=f"""
        Analise os requisitos do projeto e crie um plano de ação detalhado.
        
        Descrição do Projeto: {project_description}
        
        Sua tarefa é:
        1. Analisar os requisitos do projeto
        2. Definir o escopo e objetivos claros
        3. Identificar os principais entregáveis
        4. Criar uma lista de tarefas priorizadas
        5. Definir marcos e prazos estimados
        6. Identificar possíveis riscos e dependências
        
        Use as ferramentas do GitHub para verificar repositórios existentes,
        issues, pull requests e qualquer contexto relevante.
        """,
        agent=create_project_manager(),
        expected_output="Um plano de projeto detalhado com escopo, objetivos, tarefas priorizadas, "
                       "marcos, prazos e análise de riscos"
    )


def create_architecture_task(planning_context: str = "") -> Task:
    """
    Creates the technical architecture task for the Tech Lead.
    """
    return Task(
        description=f"""
        Com base no plano do projeto, defina a arquitetura técnica e decisões de design.
        
        Sua tarefa é:
        1. Definir a arquitetura geral do sistema
        2. Escolher tecnologias e frameworks apropriados
        3. Definir padrões de código e convenções
        4. Criar estrutura de diretórios e organização do projeto
        5. Definir estratégia de branching e CI/CD
        6. Documentar decisões técnicas importantes
        
        Use as ferramentas do GitHub para analisar o repositório,
        criar branches se necessário, e documentar a arquitetura.
        
        {planning_context}
        """,
        agent=create_tech_lead(),
        expected_output="Documento de arquitetura técnica com decisões de design, estrutura do projeto, "
                       "tecnologias escolhidas e padrões de desenvolvimento"
    )


def create_implementation_task(architecture_context: str = "") -> Task:
    """
    Creates the implementation task for the Developer.
    """
    return Task(
        description=f"""
        Implemente as funcionalidades definidas seguindo a arquitetura e padrões estabelecidos.
        
        Sua tarefa é:
        1. Implementar as funcionalidades conforme especificado
        2. Seguir os padrões de código e arquitetura definidos
        3. Escrever código limpo, legível e bem documentado
        4. Criar commits atômicos com mensagens descritivas
        5. Abrir pull requests quando necessário
        6. Responder a comentários de code review
        
        Use as ferramentas do GitHub para criar branches, fazer commits,
        abrir pull requests e colaborar com a equipe.
        
        {architecture_context}
        """,
        agent=create_developer(),
        expected_output="Código implementado de alta qualidade com commits bem documentados "
                       "e pull requests criados conforme necessário"
    )


def create_testing_task(implementation_context: str = "") -> Task:
    """
    Creates the testing and quality assurance task for the Tester.
    """
    return Task(
        description=f"""
        Realize testes abrangentes e garanta a qualidade do código implementado.
        
        Sua tarefa é:
        1. Revisar o código implementado
        2. Criar e executar casos de teste
        3. Identificar bugs e problemas de qualidade
        4. Validar que todos os requisitos foram atendidos
        5. Verificar edge cases e cenários de erro
        6. Criar issues para bugs encontrados
        7. Validar correções de bugs
        
        Use as ferramentas do GitHub para revisar pull requests,
        criar issues para bugs, e documentar resultados dos testes.
        
        {implementation_context}
        """,
        agent=create_tester(),
        expected_output="Relatório de testes com casos de teste executados, bugs identificados "
                       "e validação de que todos os requisitos foram atendidos corretamente"
    )


def create_all_tasks(project_description: str) -> list[Task]:
    """
    Creates all tasks for the IT squad workflow.
    """
    return [
        create_planning_task(project_description),
        create_architecture_task(),
        create_implementation_task(),
        create_testing_task()
    ]
