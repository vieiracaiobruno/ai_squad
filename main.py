"""
Main entry point for the AI Squad Developer Agent.

This script provides a command-line interface for interacting with
the Developer agent and performing GitHub operations.
"""
import argparse
import sys
from developer_agent import create_developer_agent
from config import Config


def main():
    """Main function for CLI interface."""
    parser = argparse.ArgumentParser(
        description="AI Squad Developer Agent - GitHub Integration"
    )
    
    parser.add_argument(
        "task",
        nargs="?",
        help="The task for the agent to perform (e.g., 'List open issues in the repository')"
    )
    
    parser.add_argument(
        "--repository",
        "-r",
        help="GitHub repository in format 'owner/repo' (overrides .env setting)"
    )
    
    parser.add_argument(
        "--list-tools",
        action="store_true",
        help="List all available GitHub tools"
    )
    
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Run in quiet mode (less verbose output)"
    )
    
    parser.add_argument(
        "--check-config",
        action="store_true",
        help="Check if configuration is properly set up"
    )
    
    args = parser.parse_args()
    
    # Check configuration
    if args.check_config:
        print("Checking configuration...")
        try:
            Config.validate()
            print("✓ Configuration is valid!")
            print(f"  - OpenAI API Key: {'*' * 10 + Config.OPENAI_API_KEY[-4:] if Config.OPENAI_API_KEY else 'Not set'}")
            print(f"  - GitHub Token: {'*' * 10 + Config.GITHUB_TOKEN[-4:] if Config.GITHUB_TOKEN else 'Not set'}")
            print(f"  - Default Repository: {Config.GITHUB_REPOSITORY or 'Not set'}")
            return 0
        except ValueError as e:
            print(f"✗ Configuration error: {e}")
            print("\nPlease create a .env file based on .env.example and fill in your credentials.")
            return 1
    
    # Validate configuration before proceeding
    try:
        Config.validate()
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("\nPlease create a .env file based on .env.example and fill in your credentials.")
        print("You can check configuration with: python main.py --check-config")
        return 1
    
    # Create agent
    try:
        agent = create_developer_agent(
            github_repository=args.repository,
            verbose=not args.quiet
        )
    except Exception as e:
        print(f"Error creating agent: {e}")
        return 1
    
    # List tools if requested
    if args.list_tools:
        print("Available GitHub Tools:")
        print("=" * 60)
        tools = agent.get_tool_descriptions()
        for i, (name, description) in enumerate(tools.items(), 1):
            print(f"\n{i}. {name}")
            print(f"   {description}")
        return 0
    
    # Execute task
    if not args.task:
        parser.print_help()
        print("\n" + "=" * 60)
        print("Examples:")
        print("  python main.py 'List the open issues in the repository'")
        print("  python main.py 'Read the README.md file' -r owner/repo")
        print("  python main.py 'Create an issue titled \"Bug Report\" with description \"Found a bug\"'")
        print("  python main.py --list-tools")
        print("  python main.py --check-config")
        return 1
    
    print(f"Executing task: {args.task}")
    print("=" * 60)
    
    result = agent.run(args.task)
    
    print("\n" + "=" * 60)
    print("Result:")
    print(result)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
