"""
GitHub Tools Integration
This module provides GitHub tools using LangChain for the IT squad.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize github_tools as an empty list by default
github_tools = []

try:
    from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
    from langchain_community.utilities.github import GitHubAPIWrapper
    
    # Try to initialize GitHub API wrapper if credentials are available
    if os.getenv("GITHUB_TOKEN"):
        # Create GitHub toolkit with various tools
        github = GitHubAPIWrapper()
        github_toolkit = GitHubToolkit.from_github_api_wrapper(github)
        github_tools = github_toolkit.get_tools()
        print(f"✓ GitHub tools initialized successfully with {len(github_tools)} tools")
    else:
        print("⚠️  GitHub token not found. GitHub tools will not be available.")
        print("   Add GITHUB_TOKEN to your .env file to enable GitHub integration.")
        
except Exception as e:
    print(f"⚠️  Could not initialize GitHub tools: {e}")
    print("   The squad will work without GitHub integration.")
    print("   To enable GitHub tools, ensure proper configuration in .env file.")

# Export the tools for use by agents
__all__ = ['github_tools']
