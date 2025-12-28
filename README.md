# AI Squad - Developer Agent with GitHub Integration

AI Squad is a Python application that provides a Developer agent with GitHub integration capabilities using LangChain. The agent can perform various GitHub operations such as managing issues, reading files, searching repositories, and more.

## Features

- 🤖 **AI-Powered Developer Agent**: Leverages LangChain and OpenAI's GPT models
- 🔧 **GitHub Integration**: Full GitHub API integration using LangChain's GitHub toolkit
- 📝 **Issue Management**: Create, read, search, and comment on GitHub issues
- 📂 **File Operations**: Read file contents from repositories
- 🔍 **Search Capabilities**: Search for issues, pull requests, and more
- 💬 **Natural Language Interface**: Interact with GitHub using plain English
- 🛠️ **Extensible**: Easy to extend with additional tools and capabilities

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- GitHub Personal Access Token

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vieiracaiobruno/ai_squad.git
   cd ai_squad
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   
   Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and fill in your credentials:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GITHUB_TOKEN=your_github_token_here
   GITHUB_REPOSITORY=owner/repo  # Optional: default repository
   ```

### Getting Your Credentials

#### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key

#### GitHub Personal Access Token
1. Go to GitHub Settings → Developer settings → [Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a descriptive name
4. Select scopes (minimum required):
   - `repo` (for full repository access)
   - `read:org` (for organization information)
   - `read:project` (for project board access)
5. Generate and copy the token

## Usage

### Command Line Interface

The main entry point is `main.py`, which provides a CLI for interacting with the Developer agent.

**Check configuration**:
```bash
python main.py --check-config
```

**List available GitHub tools**:
```bash
python main.py --list-tools
```

**Execute a task**:
```bash
python main.py "List the 5 most recent open issues"
```

**Execute a task on a specific repository**:
```bash
python main.py "Read the README.md file" -r langchain-ai/langchain
```

**Run in quiet mode**:
```bash
python main.py "Search for issues about bugs" --quiet
```

### Python API

You can also use the Developer agent programmatically in your Python code:

```python
from developer_agent import create_developer_agent

# Create agent
agent = create_developer_agent(
    github_repository="owner/repo",  # Optional
    verbose=True
)

# Execute a task
result = agent.run("List all open issues in the repository")
print(result)

# Get available tools
tools = agent.get_available_tools()
print(f"Available tools: {tools}")
```

### Example Usage Scripts

Run the examples to see the agent in action:

```bash
python example_usage.py
```

## Available GitHub Tools

The Developer agent has access to the following GitHub operations through LangChain's GitHub toolkit:

1. **Get Issue**: Retrieve details about a specific issue
2. **Get Issues**: List issues from the repository
3. **Comment on Issue**: Add comments to existing issues
4. **Create Issue**: Create new issues
5. **Create Pull Request**: Create new pull requests
6. **Create File**: Create new files in the repository
7. **Read File**: Read contents of files from the repository
8. **Update File**: Update existing files
9. **Delete File**: Delete files from the repository
10. **Search Issues**: Search for issues using GitHub's search syntax
11. **Search Code**: Search for code in the repository
12. **Overview**: Get repository overview and statistics
13. **List Branches**: List all branches in the repository
14. **Set Active Branch**: Switch the active branch
15. **Create Branch**: Create new branches
16. **Get Pull Request**: Retrieve pull request details
17. **List Pull Requests**: List pull requests
18. **List Open Pull Requests**: List only open pull requests

## Example Tasks

Here are some example tasks you can ask the Developer agent to perform:

- "List the 10 most recent open issues"
- "Create an issue titled 'Bug Report' with description 'Found a bug in the login page'"
- "Read the README.md file from the repository"
- "Search for issues related to authentication"
- "Add a comment to issue #42 saying 'I'll work on this'"
- "List all open pull requests"
- "Get details about pull request #15"
- "Search for code containing 'function login'"
- "Create a new branch called 'feature/new-feature'"
- "List all branches in the repository"

## Architecture

The project follows a modular architecture:

```
ai_squad/
├── config.py              # Configuration management
├── developer_agent.py     # Developer agent implementation
├── main.py               # CLI entry point
├── example_usage.py      # Usage examples
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # Documentation
```

### Key Components

- **Config**: Manages environment variables and application settings
- **DeveloperAgent**: Main agent class that integrates LangChain with GitHub
- **GitHubAPIWrapper**: LangChain's GitHub API wrapper
- **GitHubToolkit**: Provides GitHub tools for the agent

## LangChain GitHub Integration

This project uses LangChain's GitHub integration, which provides:

- **GitHubAPIWrapper**: Wrapper around GitHub's API
- **GitHubToolkit**: Collection of tools for GitHub operations
- **Agent**: Uses ZERO_SHOT_REACT_DESCRIPTION agent type for task execution

The agent uses a ReAct (Reasoning + Acting) pattern to:
1. Understand the task
2. Decide which tool to use
3. Execute the tool
4. Observe the result
5. Repeat until the task is complete

## Troubleshooting

### Configuration Issues

If you see "Configuration error" messages:
1. Ensure `.env` file exists
2. Check that API keys are valid
3. Run `python main.py --check-config` to verify

### GitHub Token Permissions

If you get permission errors:
1. Verify your token has the required scopes
2. Check that you have access to the repository
3. Ensure the token hasn't expired

### API Rate Limits

GitHub API has rate limits:
- Authenticated requests: 5,000 requests per hour
- Unauthenticated: 60 requests per hour

If you hit rate limits, wait for the limit to reset.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## References

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub Tools](https://python.langchain.com/docs/integrations/tools/github)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## Support

For issues, questions, or suggestions, please open an issue on GitHub.
