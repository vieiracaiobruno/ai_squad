# LangChain GitHub Integration Documentation

## Overview

This document explains how the AI Squad Developer agent integrates with GitHub using LangChain's GitHub toolkit.

## LangChain GitHub Tools

LangChain provides a comprehensive GitHub toolkit through the `langchain-community` package. The integration uses:

### 1. GitHubAPIWrapper

The `GitHubAPIWrapper` is a utility class that wraps the GitHub API using the PyGithub library.

```python
from langchain_community.utilities.github import GitHubAPIWrapper

github = GitHubAPIWrapper(
    github_api_token="your_token",
    github_repository="owner/repo"
)
```

**Key Parameters**:
- `github_api_token`: Your GitHub Personal Access Token
- `github_repository`: Default repository in format "owner/repo"
- `github_base_url`: Optional custom GitHub API URL (for GitHub Enterprise)
- `active_branch`: Optional default branch to work with

### 2. GitHubToolkit

The `GitHubToolkit` provides a collection of tools that can be used by LangChain agents.

```python
from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit

toolkit = GitHubToolkit.from_github_api_wrapper(github)
tools = toolkit.get_tools()
```

**Available Tools**:

1. **GetIssue**: Fetch details of a specific issue by number
   - Input: Issue number
   - Output: Issue details (title, body, state, comments, etc.)

2. **GetIssues**: List issues from the repository
   - Input: Optional filters (state, labels, etc.)
   - Output: List of issues

3. **CommentOnIssue**: Add a comment to an existing issue
   - Input: Issue number and comment text
   - Output: Confirmation message

4. **CreateIssue**: Create a new issue
   - Input: Title and body of the issue
   - Output: Created issue details

5. **CreatePullRequest**: Create a new pull request
   - Input: Title, body, head branch, base branch
   - Output: Created PR details

6. **CreateFile**: Create a new file in the repository
   - Input: File path, content, commit message
   - Output: Confirmation message

7. **ReadFile**: Read contents of a file
   - Input: File path
   - Output: File contents

8. **UpdateFile**: Update an existing file
   - Input: File path, new content, commit message
   - Output: Confirmation message

9. **DeleteFile**: Delete a file from the repository
   - Input: File path, commit message
   - Output: Confirmation message

10. **SearchIssues**: Search for issues using GitHub's search syntax
    - Input: Search query
    - Output: Matching issues

11. **SearchCode**: Search for code in the repository
    - Input: Search query
    - Output: Matching code snippets

12. **Overview**: Get repository statistics and information
    - Input: None
    - Output: Repository overview

13. **ListBranches**: List all branches
    - Input: None
    - Output: List of branch names

14. **SetActiveBranch**: Change the active branch
    - Input: Branch name
    - Output: Confirmation message

15. **CreateBranch**: Create a new branch
    - Input: Branch name, optional source branch
    - Output: Confirmation message

16. **GetPR**: Get details of a specific pull request
    - Input: PR number
    - Output: PR details

17. **ListPRs**: List all pull requests
    - Input: Optional filters
    - Output: List of pull requests

18. **ListOpenPRs**: List only open pull requests
    - Input: None
    - Output: List of open PRs

### 3. Agent Integration

The toolkit is integrated with a LangChain agent using the ZERO_SHOT_REACT_DESCRIPTION agent type:

```python
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0)

agent = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
```

**Agent Type Explanation**:
- **ZERO_SHOT_REACT_DESCRIPTION**: Uses tool descriptions to decide which tools to use
- **ReAct Pattern**: Reasoning + Acting - the agent thinks about what to do, acts, observes the result, and repeats

### 4. How It Works

1. **User provides a task**: "Create an issue about the login bug"

2. **Agent reasons**: Analyzes the task and available tools
   - Determines it needs to use the CreateIssue tool

3. **Agent acts**: Executes the tool with appropriate parameters
   - Calls CreateIssue with title and description

4. **Agent observes**: Receives the result from the tool
   - Gets confirmation and issue number

5. **Agent responds**: Returns the result to the user
   - "Successfully created issue #42"

## Implementation in AI Squad

### Developer Agent Class

The `DeveloperAgent` class encapsulates the GitHub integration:

```python
class DeveloperAgent:
    def __init__(self, github_token, github_repository, model_name="gpt-4"):
        # Initialize GitHub wrapper
        self.github_wrapper = GitHubAPIWrapper(
            github_api_token=github_token,
            github_repository=github_repository
        )
        
        # Initialize toolkit
        self.toolkit = GitHubToolkit.from_github_api_wrapper(
            self.github_wrapper
        )
        
        # Initialize LLM
        self.llm = ChatOpenAI(model=model_name, temperature=0)
        
        # Initialize agent
        self.agent = initialize_agent(
            tools=self.toolkit.get_tools(),
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
    
    def run(self, task: str) -> str:
        return self.agent.run(task)
```

### Configuration

Configuration is managed through environment variables:

```python
# .env file
OPENAI_API_KEY=sk-...
GITHUB_TOKEN=ghp_...
GITHUB_REPOSITORY=owner/repo
```

### Usage Examples

#### Example 1: List Issues

```python
agent = create_developer_agent()
result = agent.run("List the 5 most recent open issues")
```

**Behind the scenes**:
1. Agent identifies it needs to use GetIssues tool
2. Calls GitHub API to fetch issues
3. Formats and returns the results

#### Example 2: Create and Comment

```python
result = agent.run(
    "Create an issue titled 'Bug Report' and add a comment with details"
)
```

**Behind the scenes**:
1. Agent uses CreateIssue tool to create the issue
2. Gets the issue number from the response
3. Uses CommentOnIssue tool to add the comment
4. Returns confirmation

#### Example 3: Search and Read

```python
result = agent.run(
    "Search for issues about authentication and read the README.md file"
)
```

**Behind the scenes**:
1. Agent uses SearchIssues tool with query "authentication"
2. Uses ReadFile tool to get README.md contents
3. Combines and returns both results

## Advanced Usage

### Custom Repository Per Task

```python
agent = create_developer_agent()
result = agent.run(
    "List issues from langchain-ai/langchain repository"
)
```

### Complex Multi-Step Tasks

```python
result = agent.run(
    """
    1. Search for open bugs in the repository
    2. Create a summary issue that lists all of them
    3. Add a comment to each bug referencing the summary issue
    """
)
```

The agent will automatically:
- Break down the task into steps
- Use appropriate tools for each step
- Handle errors and retries
- Return the final result

## Best Practices

### 1. Token Permissions

Ensure your GitHub token has appropriate scopes:
- `repo`: Full repository access
- `read:org`: Read organization data
- `read:project`: Read project boards

### 2. Error Handling

The agent handles common errors:
- API rate limits
- Permission errors
- Network issues
- Parsing errors

### 3. Task Descriptions

Write clear, specific task descriptions:

✅ Good:
- "Create an issue titled 'Login Bug' with description 'Users cannot log in'"
- "List the 10 most recent open issues"
- "Read the contents of src/main.py"

❌ Avoid:
- "Do something with issues"
- "Fix the code"
- "Help me"

### 4. Performance

- Use specific tasks to reduce API calls
- Batch related operations when possible
- Monitor token usage for cost optimization

## Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Check GitHub token is valid
   - Verify token hasn't expired
   - Ensure proper permissions

2. **Rate Limit Exceeded**
   - Wait for rate limit reset
   - Use authenticated requests (higher limits)
   - Reduce frequency of requests

3. **Tool Execution Errors**
   - Check repository exists and is accessible
   - Verify file paths are correct
   - Ensure branch exists before operations

4. **Agent Confusion**
   - Simplify task description
   - Break complex tasks into steps
   - Provide more specific instructions

## References

- [LangChain GitHub Tools Documentation](https://python.langchain.com/docs/integrations/tools/github)
- [PyGithub Documentation](https://pygithub.readthedocs.io/)
- [GitHub REST API](https://docs.github.com/en/rest)
- [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/)

## Summary

The LangChain GitHub integration provides:
- ✅ Complete GitHub API access through natural language
- ✅ 18+ specialized tools for GitHub operations
- ✅ Intelligent agent that can perform complex multi-step tasks
- ✅ Easy-to-use Python API
- ✅ Robust error handling and retries

This integration makes it possible to automate GitHub workflows using simple natural language commands, powered by AI.
