"""
IT Squad Crew
This module brings together all agents and tasks to create the IT squad crew.
"""

from crewai import Crew, Process
from agents import (
    create_project_manager,
    create_tech_lead,
    create_developer,
    create_tester
)
from tasks import create_all_tasks


def create_it_squad_crew(project_description: str) -> Crew:
    """
    Creates and configures the IT squad crew.
    
    Args:
        project_description: Description of the project to be executed by the squad
        
    Returns:
        Configured Crew instance with all agents and tasks
    """
    # Create all agents
    project_manager = create_project_manager()
    tech_lead = create_tech_lead()
    developer = create_developer()
    tester = create_tester()
    
    # Create all tasks
    tasks = create_all_tasks(project_description)
    
    # Create and configure the crew
    crew = Crew(
        agents=[project_manager, tech_lead, developer, tester],
        tasks=tasks,
        process=Process.sequential,  # Tasks will be executed in sequence
        verbose=2,  # Detailed output
        full_output=True  # Return full output including individual task results
    )
    
    return crew


def run_it_squad(project_description: str) -> dict:
    """
    Runs the IT squad crew with the given project description.
    
    Args:
        project_description: Description of the project to be executed
        
    Returns:
        Dictionary containing the results of all tasks
    """
    print("="*80)
    print("🚀 Iniciando IT Squad com CrewAI")
    print("="*80)
    print(f"\nDescrição do Projeto:\n{project_description}\n")
    print("="*80)
    
    # Create the crew
    crew = create_it_squad_crew(project_description)
    
    # Execute the crew
    print("\n📋 Executando o squad de TI...\n")
    result = crew.kickoff()
    
    print("\n" + "="*80)
    print("✅ Squad de TI finalizado!")
    print("="*80)
    
    return result
