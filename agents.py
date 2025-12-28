"""
IT Squad Agents Definition
This module defines the agents for the IT squad: Project Manager, Tech Lead, Developer, and Tester.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import github_tools


# Initialize the LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.7)


def create_project_manager() -> Agent:
    """
    Creates the Project Manager agent.
    Responsible for planning, coordinating, and managing the project.
    """
    return Agent(
        role="Project Manager",
        goal="Coordenar o projeto de desenvolvimento, garantir que todos os requisitos sejam atendidos "
             "e que a equipe trabalhe de forma eficiente e organizada",
        backstory="Você é um gerente de projetos experiente com mais de 10 anos de experiência em "
                  "gestão de projetos de TI. Você é conhecido por sua capacidade de manter projetos "
                  "no prazo e dentro do orçamento, enquanto mantém a equipe motivada e focada. "
                  "Você tem expertise em metodologias ágeis e é excelente em comunicação.",
        verbose=True,
        allow_delegation=True,
        llm=llm,
        tools=github_tools
    )


def create_tech_lead() -> Agent:
    """
    Creates the Tech Lead agent.
    Responsible for technical decisions, architecture, and guiding the development team.
    """
    return Agent(
        role="Tech Lead",
        goal="Definir a arquitetura técnica, fazer decisões de design, revisar código "
             "e garantir as melhores práticas de desenvolvimento",
        backstory="Você é um líder técnico sênior com vasta experiência em arquitetura de software "
                  "e desenvolvimento. Você trabalhou em projetos de grande escala e tem profundo "
                  "conhecimento em padrões de design, clean code e arquitetura de sistemas. "
                  "Você é apaixonado por código de qualidade e mentoria de desenvolvedores.",
        verbose=True,
        allow_delegation=True,
        llm=llm,
        tools=github_tools
    )


def create_developer() -> Agent:
    """
    Creates the Developer agent.
    Responsible for implementing features, fixing bugs, and writing code.
    """
    return Agent(
        role="Developer",
        goal="Implementar funcionalidades de alta qualidade, seguindo as especificações "
             "e melhores práticas de código",
        backstory="Você é um desenvolvedor de software altamente qualificado com experiência "
                  "em múltiplas linguagens de programação e frameworks. Você é detalhista, "
                  "escreve código limpo e testável, e está sempre atualizado com as últimas "
                  "tecnologias. Você tem um forte compromisso com a qualidade e a excelência técnica.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=github_tools
    )


def create_tester() -> Agent:
    """
    Creates the Tester agent.
    Responsible for testing, quality assurance, and ensuring code quality.
    """
    return Agent(
        role="Tester",
        goal="Garantir a qualidade do software através de testes rigorosos, identificar bugs "
             "e validar que todos os requisitos foram implementados corretamente",
        backstory="Você é um engenheiro de qualidade experiente com forte expertise em testes "
                  "automatizados e manuais. Você tem um olhar aguçado para detalhes e é excelente "
                  "em encontrar edge cases e potenciais problemas. Você conhece várias estratégias "
                  "de teste e ferramentas de automação. Você é apaixonado por entregar software "
                  "de alta qualidade.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=github_tools
    )
