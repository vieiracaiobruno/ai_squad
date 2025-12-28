"""
GitHub Tools Integration
This module provides GitHub tools using LangChain for the IT squad.
"""

import os
from dotenv import load_dotenv
from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
from langchain_community.utilities.github import GitHubAPIWrapper

# Load environment variables
load_dotenv()

# Initialize GitHub API wrapper
github = GitHubAPIWrapper()

# Create GitHub toolkit with various tools
github_toolkit = GitHubToolkit.from_github_api_wrapper(github)

# Get the tools from the toolkit
github_tools = github_toolkit.get_tools()

# Export the tools for use by agents
__all__ = ['github_tools', 'github_toolkit']
