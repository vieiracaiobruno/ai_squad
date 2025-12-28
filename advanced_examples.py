"""
Advanced usage examples for the Developer Agent.

This script demonstrates more complex and real-world use cases
of the Developer Agent with GitHub integration.
"""
from developer_agent import create_developer_agent


def example_issue_triage_workflow(repository: str):
    """
    Example: Automated issue triage workflow.
    
    This example demonstrates how to:
    1. Search for new issues
    2. Analyze them
    3. Add appropriate labels or comments
    """
    print(f"=== Issue Triage Workflow for {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    # Step 1: Find new issues
    task1 = "List all open issues that were created in the last 7 days"
    print("Step 1: Finding new issues...")
    result1 = agent.run(task1)
    print(f"Result: {result1}\n")
    
    # Step 2: For a specific issue, add a triage comment
    # Note: This is a template - adjust issue number based on result1
    # task2 = "Add a comment to issue #123 saying 'Thank you for reporting this. We will review it soon.'"
    # result2 = agent.run(task2)
    # print(f"Result: {result2}\n")


def example_documentation_check(repository: str):
    """
    Example: Check documentation files.
    
    This example demonstrates reading multiple documentation files
    to verify their contents.
    """
    print(f"=== Documentation Check for {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = """
    Read the README.md file and tell me:
    1. Does it have installation instructions?
    2. Does it have usage examples?
    3. What is the main purpose of the repository?
    """
    
    print("Analyzing documentation...")
    result = agent.run(task)
    print(f"\nAnalysis Result:\n{result}\n")


def example_pr_review_assistant(repository: str):
    """
    Example: Pull Request review assistant.
    
    This demonstrates listing and analyzing pull requests.
    """
    print(f"=== PR Review Assistant for {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    # List open PRs
    task1 = "List all open pull requests with their titles and authors"
    print("Fetching open pull requests...")
    result1 = agent.run(task1)
    print(f"Open PRs:\n{result1}\n")
    
    # Get details of a specific PR
    # Uncomment and adjust PR number based on results
    # task2 = "Get detailed information about pull request #42"
    # result2 = agent.run(task2)
    # print(f"PR Details:\n{result2}\n")


def example_code_search(repository: str, search_query: str):
    """
    Example: Search for code patterns.
    
    This demonstrates using the code search functionality.
    """
    print(f"=== Code Search in {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = f"Search the repository for code containing: {search_query}"
    print(f"Searching for: {search_query}")
    result = agent.run(task)
    print(f"\nSearch Results:\n{result}\n")


def example_repository_health_check(repository: str):
    """
    Example: Get a health overview of the repository.
    
    This demonstrates getting comprehensive repository information.
    """
    print(f"=== Repository Health Check for {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = """
    Provide a health overview of this repository including:
    1. Number of open vs closed issues
    2. Recent activity
    3. Number of open pull requests
    4. Repository description and main language
    """
    
    print("Analyzing repository health...")
    result = agent.run(task)
    print(f"\nHealth Report:\n{result}\n")


def example_branch_management(repository: str):
    """
    Example: Branch management operations.
    
    This demonstrates listing and working with branches.
    """
    print(f"=== Branch Management for {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    # List all branches
    task1 = "List all branches in the repository"
    print("Listing branches...")
    result1 = agent.run(task1)
    print(f"Branches:\n{result1}\n")
    
    # Note: Creating branches requires careful consideration
    # Uncomment only if you want to actually create a branch
    # task2 = "Create a new branch called 'feature/test-branch'"
    # result2 = agent.run(task2)
    # print(f"Branch Creation:\n{result2}\n")


def example_issue_statistics(repository: str):
    """
    Example: Gather statistics about issues.
    
    This demonstrates analyzing issue patterns.
    """
    print(f"=== Issue Statistics for {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = """
    Analyze the issues in this repository and tell me:
    1. How many issues are currently open?
    2. What are the common topics or themes in recent issues?
    3. Are there any critical or high-priority issues?
    """
    
    print("Analyzing issue statistics...")
    result = agent.run(task)
    print(f"\nStatistics:\n{result}\n")


def example_file_content_analysis(repository: str, file_path: str):
    """
    Example: Analyze a specific file.
    
    This demonstrates reading and analyzing file contents.
    """
    print(f"=== File Analysis: {file_path} in {repository} ===\n")
    
    agent = create_developer_agent(github_repository=repository)
    
    task = f"""
    Read the file {file_path} and:
    1. Summarize its purpose
    2. Identify the main components or functions
    3. Note any TODO comments or areas for improvement
    """
    
    print(f"Analyzing {file_path}...")
    result = agent.run(task)
    print(f"\nAnalysis:\n{result}\n")


def example_multi_repository_comparison():
    """
    Example: Compare multiple repositories.
    
    This demonstrates using multiple agent instances for different repos.
    """
    print("=== Multi-Repository Comparison ===\n")
    
    repos = [
        "langchain-ai/langchain",
        "openai/openai-python"
    ]
    
    for repo in repos:
        print(f"\nAnalyzing {repo}...")
        agent = create_developer_agent(github_repository=repo)
        
        task = "Give me a brief overview of this repository's purpose and recent activity"
        result = agent.run(task)
        print(f"Result for {repo}:\n{result}\n")
        print("-" * 60)


def example_create_issue_from_template(repository: str):
    """
    Example: Create an issue with proper formatting.
    
    WARNING: This will actually create an issue in the repository!
    Only run this on repositories you own.
    """
    print(f"=== Creating Issue in {repository} ===\n")
    print("WARNING: This will create a real issue!\n")
    
    # Uncomment to actually run
    # agent = create_developer_agent(github_repository=repository)
    
    # task = """
    # Create a new issue with:
    # Title: "Example Issue from Developer Agent"
    # Body: 
    # ## Description
    # This is a test issue created by the Developer Agent.
    # 
    # ## Steps to Reproduce
    # 1. This is a test
    # 2. No actual bug to reproduce
    # 
    # ## Expected Behavior
    # This is just a demonstration
    # 
    # Please close this issue as it's just a test.
    # """
    
    # result = agent.run(task)
    # print(f"Result:\n{result}\n")
    
    print("(Commented out for safety - uncomment to run)")


def example_automated_response():
    """
    Example: Automated response to specific issue patterns.
    
    This demonstrates how you could build an automated issue responder.
    """
    print("=== Automated Issue Response Pattern ===\n")
    
    # This is a conceptual example
    print("""
    Conceptual workflow for automated responses:
    
    1. Search for issues with specific keywords (e.g., "install error")
    2. Check if they already have responses
    3. If not, add a helpful comment with common solutions
    4. Tag with appropriate labels
    
    This could be run as a scheduled job to help with issue triage.
    """)


def interactive_mode():
    """
    Example: Interactive mode where user can enter tasks.
    
    This demonstrates building an interactive CLI tool.
    """
    print("=== Interactive Developer Agent ===\n")
    print("Enter tasks for the agent to perform.")
    print("Type 'quit' to exit.\n")
    
    repository = input("Enter repository (owner/repo): ")
    
    agent = create_developer_agent(github_repository=repository)
    
    while True:
        task = input("\nEnter task (or 'quit'): ")
        
        if task.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not task.strip():
            continue
        
        print("\nExecuting task...")
        result = agent.run(task)
        print(f"\nResult:\n{result}\n")


def main():
    """Main function with example selection."""
    print("=" * 70)
    print("Advanced Developer Agent Examples")
    print("=" * 70)
    print()
    print("Available examples:")
    print("1. Issue Triage Workflow")
    print("2. Documentation Check")
    print("3. PR Review Assistant")
    print("4. Code Search")
    print("5. Repository Health Check")
    print("6. Branch Management")
    print("7. Issue Statistics")
    print("8. File Content Analysis")
    print("9. Multi-Repository Comparison")
    print("10. Automated Response Pattern (Conceptual)")
    print("11. Interactive Mode")
    print()
    print("Note: Most examples use public repositories for demonstration.")
    print("For write operations (create issue, etc.), use your own repository!")
    print()
    
    # Example: Run documentation check on LangChain repo
    print("Running Example: Documentation Check on langchain-ai/langchain")
    print()
    example_documentation_check("langchain-ai/langchain")
    
    print("\n" + "=" * 70)
    print("To run other examples:")
    print("- Uncomment the desired example in the main() function")
    print("- Adjust repository names as needed")
    print("- Be careful with write operations!")
    print("=" * 70)


if __name__ == "__main__":
    main()
