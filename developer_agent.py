"""
Developer Agent with GitHub Integration using LangChain.

This module implements a Developer agent that can interact with GitHub
repositories using LangChain's GitHub toolkit.
"""
from typing import Optional, List
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
from langchain_community.utilities.github import GitHubAPIWrapper
from config import Config


class DeveloperAgent:
    """
    A Developer agent that integrates with GitHub using LangChain.
    
    This agent can perform various GitHub operations such as:
    - Creating, reading, and commenting on issues
    - Searching for issues and pull requests
    - Reading file contents from repositories
    - Managing branches
    - And more GitHub operations
    """
    
    def __init__(
        self,
        github_token: Optional[str] = None,
        github_repository: Optional[str] = None,
        model_name: str = "gpt-4",
        temperature: float = 0.0,
        verbose: bool = True
    ):
        """
        Initialize the Developer Agent.
        
        Args:
            github_token: GitHub personal access token. If not provided, reads from Config.
            github_repository: GitHub repository in format "owner/repo". If not provided, reads from Config.
            model_name: OpenAI model to use (default: gpt-4)
            temperature: Model temperature (default: 0.0)
            verbose: Whether to print agent actions (default: True)
        """
        # Use provided values or fall back to Config
        self.github_token = github_token or Config.GITHUB_TOKEN
        self.github_repository = github_repository or Config.GITHUB_REPOSITORY
        
        # Validate configuration
        if not self.github_token:
            raise ValueError("GitHub token is required")
        
        # Initialize GitHub API wrapper
        self.github_wrapper = GitHubAPIWrapper(
            github_app_id=None,
            github_app_private_key=None,
            github_repository=self.github_repository,
            github_base_url=None,
            active_branch=None,
            github_api_token=self.github_token
        )
        
        # Initialize GitHub toolkit
        self.toolkit = GitHubToolkit.from_github_api_wrapper(self.github_wrapper)
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            openai_api_key=Config.OPENAI_API_KEY
        )
        
        # Initialize agent with GitHub tools
        self.agent = initialize_agent(
            tools=self.toolkit.get_tools(),
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=verbose,
            handle_parsing_errors=True
        )
    
    def run(self, task: str) -> str:
        """
        Execute a task using the Developer agent.
        
        Args:
            task: The task description for the agent to perform
            
        Returns:
            The result of the agent's execution
        """
        try:
            result = self.agent.run(task)
            return result
        except Exception as e:
            return f"Error executing task: {str(e)}"
    
    def get_available_tools(self) -> List[str]:
        """
        Get a list of available GitHub tools.
        
        Returns:
            List of tool names
        """
        return [tool.name for tool in self.toolkit.get_tools()]
    
    def get_tool_descriptions(self) -> dict:
        """
        Get descriptions of all available tools.
        
        Returns:
            Dictionary mapping tool names to their descriptions
        """
        return {
            tool.name: tool.description 
            for tool in self.toolkit.get_tools()
        }


def create_developer_agent(
    github_repository: Optional[str] = None,
    verbose: bool = True
) -> DeveloperAgent:
    """
    Factory function to create a Developer agent.
    
    Args:
        github_repository: GitHub repository in format "owner/repo"
        verbose: Whether to print agent actions
        
    Returns:
        Initialized DeveloperAgent instance
    """
    # Validate configuration
    Config.validate()
    
    # Create and return agent
    return DeveloperAgent(
        github_repository=github_repository,
        verbose=verbose
    )
