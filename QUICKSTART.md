# Quick Start Guide

This guide will help you get started with the AI Squad Developer Agent quickly.

## Prerequisites

Before you begin, make sure you have:
- Python 3.8 or higher installed
- A GitHub account
- An OpenAI account with API access

## Step 1: Clone the Repository

```bash
git clone https://github.com/vieiracaiobruno/ai_squad.git
cd ai_squad
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- LangChain (core framework)
- LangChain Community (GitHub tools)
- LangChain OpenAI (GPT models)
- PyGithub (GitHub API client)
- python-dotenv (environment variables)
- Pydantic (data validation)

## Step 3: Get Your API Keys

### OpenAI API Key

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys
4. Click "Create new secret key"
5. Copy the key (it will look like `sk-...`)

### GitHub Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name: "AI Squad Developer Agent"
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org and team membership)
   - ✅ `read:project` (Read access to projects)
5. Click "Generate token"
6. Copy the token (it will look like `ghp_...`)

**Important**: Save these keys securely! You won't be able to see them again.

## Step 4: Configure Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Edit the `.env` file and add your keys:

```
OPENAI_API_KEY=sk-your_actual_openai_key_here
GITHUB_TOKEN=ghp_your_actual_github_token_here
GITHUB_REPOSITORY=owner/repo  # Optional: your default repository
```

## Step 5: Verify Configuration

```bash
python main.py --check-config
```

You should see:
```
✓ Configuration is valid!
  - OpenAI API Key: **********abc1
  - GitHub Token: **********xyz9
  - Default Repository: owner/repo
```

## Step 6: Test the Agent

List available tools:
```bash
python main.py --list-tools
```

Try a simple task:
```bash
python main.py "List the repository information" -r langchain-ai/langchain
```

## Step 7: Run Examples

```bash
python example_usage.py
```

This will show you the available GitHub tools.

## Common Tasks

### List Issues
```bash
python main.py "List the 5 most recent open issues" -r owner/repo
```

### Read a File
```bash
python main.py "Read the README.md file" -r owner/repo
```

### Search Issues
```bash
python main.py "Search for issues about bugs" -r owner/repo
```

### Create an Issue (be careful!)
```bash
python main.py "Create an issue titled 'Test Issue' with description 'This is a test'" -r owner/repo
```

## Understanding the Output

When you run a task, you'll see:

1. **Thought Process**: The agent thinking about what to do
2. **Action**: Which tool it's using
3. **Action Input**: Parameters for the tool
4. **Observation**: Result from the tool
5. **Final Answer**: The complete response

Example:
```
Thought: I need to list open issues in the repository
Action: Get Issues
Action Input: {"query": "is:open"}
Observation: Issue #1: Bug in login
Issue #2: Feature request for dark mode
...
Final Answer: Here are the recent open issues: ...
```

## Troubleshooting

### "Configuration error: OPENAI_API_KEY is required"
- Make sure you created the `.env` file
- Check that the API key is correct
- No spaces around the `=` sign

### "Authentication Failed"
- Verify your GitHub token is valid
- Check that it hasn't expired
- Ensure it has the required permissions

### "Rate Limit Exceeded"
- You've made too many GitHub API requests
- Wait an hour for the limit to reset
- Authenticated users get 5,000 requests/hour

### Agent takes a long time
- GPT-4 can take 10-30 seconds to respond
- Complex tasks require multiple API calls
- Use `--quiet` mode to reduce output

## Next Steps

Now that you have the agent working, you can:

1. **Read the full documentation**: See `README.md` for detailed information
2. **Learn about the integration**: Check `LANGCHAIN_GITHUB_INTEGRATION.md`
3. **Explore the code**: Look at `developer_agent.py` to understand the implementation
4. **Customize**: Modify the agent for your specific needs
5. **Integrate**: Use the agent in your own projects

## Using in Your Code

```python
from developer_agent import create_developer_agent

# Create the agent
agent = create_developer_agent(
    github_repository="owner/repo"
)

# Use it
result = agent.run("List all open pull requests")
print(result)
```

## Tips for Success

1. **Be Specific**: Clear tasks get better results
   - ✅ "List the 10 most recent open issues"
   - ❌ "Show me stuff"

2. **One Task at a Time**: Keep tasks focused
   - ✅ "Read the README.md file"
   - ❌ "Read all files and create a summary report"

3. **Specify the Repository**: Use `-r owner/repo`
   - Avoids ambiguity
   - Works with any public repository

4. **Monitor Usage**: OpenAI API calls cost money
   - Check your usage at https://platform.openai.com/usage
   - Start with simple tasks
   - Use GPT-3.5 for testing (modify `developer_agent.py`)

5. **Test Safely**: Try read-only operations first
   - List issues ✅
   - Read files ✅
   - Search ✅
   - Create issues (test on your own repo!)

## Getting Help

- **Documentation Issues**: Check `README.md` and `LANGCHAIN_GITHUB_INTEGRATION.md`
- **Code Questions**: Review `developer_agent.py` and comments
- **GitHub API**: See https://docs.github.com/en/rest
- **LangChain**: Visit https://python.langchain.com/docs
- **Issues**: Open an issue on GitHub

## What's Next?

You're now ready to use the AI Squad Developer Agent! Try:

1. Managing issues on your repositories
2. Automating repetitive GitHub tasks
3. Building workflows that combine multiple operations
4. Integrating the agent into your CI/CD pipeline
5. Creating custom tools for your specific needs

Happy automating! 🚀
