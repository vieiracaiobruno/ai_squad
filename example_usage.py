"""
Example usage of the Developer Agent with GitHub integration.

This script demonstrates how to use the Developer agent to perform
various GitHub operations.
"""
from developer_agent import create_developer_agent


def example_list_tools():
    """Example: List all available GitHub tools."""
    print("=== Available GitHub Tools ===\n")
    
    agent = create_developer_agent(verbose=False)
    tools = agent.get_available_tools()
    
    print(f"The Developer agent has access to {len(tools)} GitHub tools:")
    for i, tool in enumerate(tools, 1):
        print(f"{i}. {tool}")
    
    print("\n=== Tool Descriptions ===\n")
    descriptions = agent.get_tool_descriptions()
    for tool_name, description in descriptions.items():
        print(f"{tool_name}:")
        print(f"  {description}\n")


def example_search_issues(repository: str):
    """Example: Search for open issues in a repository."""
    print(f"=== Searching for Issues in {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = f"List the 3 most recent open issues in the repository {repository}"
    result = agent.run(task)
    
    print("Result:")
    print(result)


def example_read_file(repository: str, file_path: str):
    """Example: Read a file from the repository."""
    print(f"=== Reading {file_path} from {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = f"Read the contents of the file {file_path} from the repository"
    result = agent.run(task)
    
    print("Result:")
    print(result)


def example_create_issue(repository: str, title: str, body: str):
    """Example: Create a new issue in the repository."""
    print(f"=== Creating Issue in {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = f"Create a new issue titled '{title}' with the following description: {body}"
    result = agent.run(task)
    
    print("Result:")
    print(result)


def example_comment_on_issue(repository: str, issue_number: int, comment: str):
    """Example: Comment on an existing issue."""
    print(f"=== Adding Comment to Issue #{issue_number} in {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = f"Add a comment to issue #{issue_number} with the text: {comment}"
    result = agent.run(task)
    
    print("Result:")
    print(result)


def main():
    """Main function to run examples."""
    print("=" * 60)
    print("Developer Agent with GitHub Integration - Examples")
    print("=" * 60)
    print()
    
    # Example 1: List available tools
    example_list_tools()
    
    # Example 2: Search for issues (uncomment and provide a repository)
    # example_search_issues("langchain-ai/langchain")
    
    # Example 3: Read a file (uncomment and provide repository and file path)
    # example_read_file("langchain-ai/langchain", "README.md")
    
    # Example 4: Create an issue (uncomment to use)
    # example_create_issue(
    #     "your-username/your-repo",
    #     "Bug: Something is broken",
    #     "Detailed description of the issue..."
    # )
    
    # Example 5: Comment on an issue (uncomment to use)
    # example_comment_on_issue(
    #     "your-username/your-repo",
    #     issue_number=1,
    #     comment="This is a comment from the Developer Agent!"
    # )
    
    print("\nTo use the other examples, uncomment them in the main() function")
    print("and provide appropriate repository names and parameters.")


if __name__ == "__main__":
    main()
