"""
GitHub Tools Integration
This module provides GitHub tools for the IT squad with support for both:
1. Personal Access Token (PAT) - Simpler setup, recommended for individual use
2. GitHub App - For production and organizational use

Based on LangChain documentation: https://docs.langchain.com/oss/python/integrations/tools/github
"""

import os
from dotenv import load_dotenv
from typing import Optional, List
from crewai.tools import BaseTool

# Load environment variables
load_dotenv()

# Initialize github_tools as an empty list by default
github_tools = []


def create_github_tools_with_pat(token: str, repository: Optional[str] = None) -> List:
    """
    Create GitHub tools using Personal Access Token (PAT).
    
    This is the simpler method that uses PyGithub directly with a personal access token.
    Recommended for individual developers and quick setup.
    
    Args:
        token: GitHub Personal Access Token
        repository: Optional repository in format "owner/repo"
    
    Returns:
        List of tools for GitHub operations
    """
    try:
        from github import Github, Auth
        from langchain.tools import Tool
        from langchain_community.utilities.github import GitHubAPIWrapper
        
        # Create PyGithub client with token authentication
        auth = Auth.Token(token)
        g = Github(auth=auth)
        
        # Verify authentication works
        try:
            user = g.get_user()
            print(f"✓ GitHub authenticated as: {user.login}")
        except Exception as e:
            print(f"⚠️  GitHub authentication failed: {e}")
            return []
        
        # Create basic GitHub tools using PyGithub
        tools = []
        
        # Tool: Get repository info
        def get_repo_info(repo_name: str) -> str:
            """Get information about a GitHub repository. Input should be 'owner/repo'."""
            try:
                repo = g.get_repo(repo_name)
                return f"""Repository: {repo.full_name}
Description: {repo.description}
Stars: {repo.stargazers_count}
Forks: {repo.forks_count}
Open Issues: {repo.open_issues_count}
Default Branch: {repo.default_branch}
Language: {repo.language}
URL: {repo.html_url}"""
            except Exception as e:
                return f"Error getting repository info: {e}"
        
        tools.append(Tool(
            name="get_github_repo_info",
            func=get_repo_info,
            description="Get detailed information about a GitHub repository. Input should be the repository name in format 'owner/repo', for example 'microsoft/vscode' or 'facebook/react'."
        ))
        
        # Tool: List repository files
        def list_repo_files(repo_and_path: str) -> str:
            """List files in a repository directory. Input format: 'owner/repo:path' or just 'owner/repo' for root."""
            try:
                if ':' in repo_and_path:
                    repo_name, path = repo_and_path.split(':', 1)
                else:
                    repo_name, path = repo_and_path, ''
                
                repo = g.get_repo(repo_name)
                contents = repo.get_contents(path)
                
                if not isinstance(contents, list):
                    contents = [contents]
                
                files = []
                for content in contents:
                    file_type = "dir" if content.type == "dir" else "file"
                    files.append(f"[{file_type}] {content.path}")
                
                return "\n".join(files) if files else "No files found"
            except Exception as e:
                return f"Error listing files: {e}"
        
        tools.append(Tool(
            name="list_github_repo_files",
            func=list_repo_files,
            description="List files and directories in a GitHub repository. Input format: 'owner/repo:path' to list a specific directory, or 'owner/repo' to list the root directory. For example: 'microsoft/vscode:src' or 'facebook/react'"
        ))
        
        # Tool: Read file content
        def read_file_content(repo_file: str) -> str:
            """Read content of a file from a repository. Input format: 'owner/repo:path/to/file'."""
            try:
                if ':' not in repo_file:
                    return "Error: Input must be in format 'owner/repo:path/to/file'"
                
                repo_name, file_path = repo_file.split(':', 1)
                repo = g.get_repo(repo_name)
                content = repo.get_contents(file_path)
                
                if content.type != "file":
                    return f"Error: {file_path} is not a file"
                
                # Decode content (it's base64 encoded)
                file_content = content.decoded_content.decode('utf-8')
                return file_content
            except Exception as e:
                return f"Error reading file: {e}"
        
        tools.append(Tool(
            name="read_github_file",
            func=read_file_content,
            description="Read the content of a file from a GitHub repository. Input must be in format 'owner/repo:path/to/file', for example 'microsoft/vscode:README.md' or 'facebook/react:packages/react/index.js'"
        ))
        
        # Tool: Search code
        def search_code(query: str) -> str:
            """Search for code across GitHub. Input should be a search query."""
            try:
                results = g.search_code(query)
                findings = []
                for i, result in enumerate(results[:10], 1):  # Limit to 10 results
                    findings.append(f"{i}. {result.repository.full_name}/{result.path}")
                
                return "\n".join(findings) if findings else "No results found"
            except Exception as e:
                return f"Error searching code: {e}"
        
        tools.append(Tool(
            name="search_github_code",
            func=search_code,
            description="Search for code across all of GitHub. Input should be a search query, you can use qualifiers like 'language:python', 'repo:owner/name', 'path:src/', etc. For example: 'def authenticate language:python' or 'class Component repo:facebook/react'"
        ))
        
        # Tool: List issues
        def list_issues(repo_name: str) -> str:
            """List open issues in a repository. Input should be 'owner/repo'."""
            try:
                repo = g.get_repo(repo_name)
                issues = repo.get_issues(state='open')
                
                issue_list = []
                for i, issue in enumerate(list(issues)[:20], 1):  # Limit to 20 issues
                    issue_list.append(f"#{issue.number}: {issue.title} (@{issue.user.login})")
                
                return "\n".join(issue_list) if issue_list else "No open issues"
            except Exception as e:
                return f"Error listing issues: {e}"
        
        tools.append(Tool(
            name="list_github_issues",
            func=list_issues,
            description="List open issues in a GitHub repository. Input should be the repository name in format 'owner/repo', for example 'microsoft/vscode' or 'facebook/react'. Returns up to 20 most recent open issues."
        ))
        
        # Tool: Get issue details
        def get_issue(repo_and_issue: str) -> str:
            """Get details of a specific issue. Input format: 'owner/repo:issue_number'."""
            try:
                if ':' not in repo_and_issue:
                    return "Error: Input must be in format 'owner/repo:issue_number'"
                
                repo_name, issue_num = repo_and_issue.split(':', 1)
                repo = g.get_repo(repo_name)
                issue = repo.get_issue(int(issue_num))
                
                return f"""Issue #{issue.number}: {issue.title}
State: {issue.state}
Author: @{issue.user.login}
Created: {issue.created_at}
Comments: {issue.comments}

{issue.body}"""
            except Exception as e:
                return f"Error getting issue: {e}"
        
        tools.append(Tool(
            name="get_github_issue",
            func=get_issue,
            description="Get detailed information about a specific GitHub issue. Input must be in format 'owner/repo:issue_number', for example 'microsoft/vscode:123' or 'facebook/react:456'"
        ))
        
        # Tool: List pull requests
        def list_prs(repo_name: str) -> str:
            """List open pull requests in a repository. Input should be 'owner/repo'."""
            try:
                repo = g.get_repo(repo_name)
                prs = repo.get_pulls(state='open')
                
                pr_list = []
                for i, pr in enumerate(list(prs)[:20], 1):  # Limit to 20 PRs
                    pr_list.append(f"#{pr.number}: {pr.title} (@{pr.user.login})")
                
                return "\n".join(pr_list) if pr_list else "No open pull requests"
            except Exception as e:
                return f"Error listing PRs: {e}"
        
        tools.append(Tool(
            name="list_github_prs",
            func=list_prs,
            description="List open pull requests in a GitHub repository. Input should be the repository name in format 'owner/repo', for example 'microsoft/vscode' or 'facebook/react'. Returns up to 20 most recent open pull requests."
        ))
        
        # Tool: Search repositories
        def search_repos(query: str) -> str:
            """Search for repositories on GitHub. Input should be a search query."""
            try:
                results = g.search_repositories(query)
                repos = []
                for i, repo in enumerate(list(results)[:15], 1):  # Limit to 15 results
                    repos.append(f"{i}. {repo.full_name} ⭐{repo.stargazers_count} - {repo.description or 'No description'}")
                
                return "\n".join(repos) if repos else "No repositories found"
            except Exception as e:
                return f"Error searching repositories: {e}"
        
        tools.append(Tool(
            name="search_github_repositories",
            func=search_repos,
            description="Search for repositories on GitHub. Input should be a search query, you can use qualifiers like 'language:python', 'stars:>1000', 'topic:machine-learning', etc. For example: 'web framework language:python' or 'react stars:>10000'"
        ))
        
        print(f"✓ GitHub tools initialized with Personal Access Token")
        print(f"  Created {len(tools)} GitHub tools")
        
        return tools
        
    except ImportError as e:
        print(f"⚠️  Required package not installed: {e}")
        print("   Please run: pip install PyGithub")
        return []
    except Exception as e:
        print(f"⚠️  Error creating GitHub tools with PAT: {e}")
        return []


def create_github_tools_with_app(app_id: str, private_key: str, repository: str) -> List:
    """
    Create GitHub tools using GitHub App authentication.
    
    This method uses LangChain's GitHubToolkit with GitHub App credentials.
    Recommended for production environments and organizational use.
    
    Args:
        app_id: GitHub App ID
        private_key: GitHub App Private Key (or path to key file)
        repository: Repository in format "owner/repo"
    
    Returns:
        List of tools for GitHub operations
    """
    try:
        from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
        from langchain_community.utilities.github import GitHubAPIWrapper
        
        # Create GitHub API wrapper with App credentials
        github = GitHubAPIWrapper(
            github_app_id=app_id,
            github_app_private_key=private_key,
            github_repository=repository
        )
        
        # Create toolkit
        github_toolkit = GitHubToolkit.from_github_api_wrapper(github)
        tools = github_toolkit.get_tools()
        
        print(f"✓ GitHub tools initialized with GitHub App")
        print(f"  Created {len(tools)} GitHub tools")
        
        return tools
        
    except Exception as e:
        print(f"⚠️  Error creating GitHub tools with GitHub App: {e}")
        return []


# Initialize GitHub tools based on available credentials
def initialize_github_tools() -> List:
    """
    Initialize GitHub tools based on available credentials.
    
    Priority:
    1. Try Personal Access Token (GITHUB_TOKEN) - Simpler setup
    2. Try GitHub App (GITHUB_APP_ID + GITHUB_APP_PRIVATE_KEY) - Production setup
    3. Return empty list if no credentials available
    """
    # Method 1: Personal Access Token (recommended for getting started)
    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        print("🔧 Initializing GitHub tools with Personal Access Token...")
        tools = create_github_tools_with_pat(
            token=github_token,
            repository=os.getenv("GITHUB_REPOSITORY")
        )
        if tools:
            return tools
    
    # Method 2: GitHub App (for production)
    github_app_id = os.getenv("GITHUB_APP_ID")
    github_app_private_key = os.getenv("GITHUB_APP_PRIVATE_KEY")
    github_repository = os.getenv("GITHUB_REPOSITORY")
    
    if github_app_id and github_app_private_key and github_repository:
        print("🔧 Initializing GitHub tools with GitHub App...")
        tools = create_github_tools_with_app(
            app_id=github_app_id,
            private_key=github_app_private_key,
            repository=github_repository
        )
        if tools:
            return tools
    
    # No credentials available
    print("⚠️  No GitHub credentials found.")
    print("   To enable GitHub integration, add one of the following to your .env file:")
    print("   ")
    print("   Option 1 (Recommended - Easier setup):")
    print("   GITHUB_TOKEN=your_personal_access_token")
    print("   ")
    print("   Option 2 (For production):")
    print("   GITHUB_APP_ID=your_app_id")
    print("   GITHUB_APP_PRIVATE_KEY=your_private_key")
    print("   GITHUB_REPOSITORY=owner/repo")
    print("   ")
    print("   See README.md for detailed instructions.")
    
    return []


# Initialize the tools
github_tools = initialize_github_tools()

# Export the tools for use by agents
__all__ = ['github_tools']
