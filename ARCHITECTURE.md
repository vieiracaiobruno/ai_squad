# Architecture and Design

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AI Squad System                          │
│                                                             │
│  ┌──────────────┐         ┌──────────────┐                 │
│  │              │         │              │                 │
│  │  User Input  │────────▶│  Main CLI    │                 │
│  │              │         │  (main.py)   │                 │
│  └──────────────┘         └──────┬───────┘                 │
│                                  │                          │
│                                  ▼                          │
│                          ┌───────────────┐                  │
│                          │  Developer    │                  │
│                          │  Agent        │                  │
│                          │ (developer_   │                  │
│                          │  agent.py)    │                  │
│                          └───────┬───────┘                  │
│                                  │                          │
│              ┌───────────────────┼───────────────────┐      │
│              │                   │                   │      │
│              ▼                   ▼                   ▼      │
│      ┌──────────────┐   ┌──────────────┐   ┌──────────────┐│
│      │  LangChain   │   │  GitHub API  │   │   OpenAI     ││
│      │  Agent       │   │  Wrapper     │   │   GPT-4      ││
│      └──────┬───────┘   └──────┬───────┘   └──────┬───────┘│
│             │                  │                   │        │
│             └──────────────────┼───────────────────┘        │
│                                │                            │
│                        ┌───────▼────────┐                   │
│                        │ GitHub Toolkit │                   │
│                        │  (18+ tools)   │                   │
│                        └───────┬────────┘                   │
└────────────────────────────────┼──────────────────────────┘
                                 │
                                 ▼
                         ┌──────────────┐
                         │   GitHub     │
                         │   REST API   │
                         └──────────────┘
```

## Component Details

### 1. Configuration Layer (`config.py`)

```python
┌─────────────────────────┐
│      Config Class       │
├─────────────────────────┤
│ - OPENAI_API_KEY        │
│ - GITHUB_TOKEN          │
│ - GITHUB_REPOSITORY     │
├─────────────────────────┤
│ + validate()            │
│ + is_configured()       │
└─────────────────────────┘
```

**Responsibilities**:
- Load environment variables from `.env`
- Validate required configuration
- Provide configuration to other components

### 2. Developer Agent (`developer_agent.py`)

```python
┌─────────────────────────────────┐
│      DeveloperAgent Class       │
├─────────────────────────────────┤
│ - github_wrapper                │
│ - toolkit                       │
│ - llm                           │
│ - agent                         │
├─────────────────────────────────┤
│ + __init__(...)                 │
│ + run(task: str) -> str         │
│ + get_available_tools()         │
│ + get_tool_descriptions()       │
└─────────────────────────────────┘
```

**Responsibilities**:
- Initialize GitHub API wrapper
- Create GitHub toolkit with tools
- Initialize LangChain agent with LLM
- Execute user tasks
- Handle errors and exceptions

### 3. GitHub Integration Flow

```
User Task: "List open issues"
     │
     ▼
┌──────────────────────────────────────────┐
│ 1. Agent receives task                   │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│ 2. Agent analyzes task                   │
│    - Uses GPT-4 to understand intent     │
│    - Reviews available tools             │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│ 3. Agent selects tool                    │
│    - Chooses "GetIssues" tool            │
│    - Determines parameters               │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│ 4. Tool execution                        │
│    - Calls GitHub API via PyGithub       │
│    - Retrieves open issues               │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│ 5. Agent processes result                │
│    - Receives issue data                 │
│    - Formats for user                    │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│ 6. Return to user                        │
│    - Formatted list of issues            │
└──────────────────────────────────────────┘
```

### 4. LangChain ReAct Pattern

The agent uses the ReAct (Reasoning + Acting) pattern:

```
┌─────────────────────────────────────────┐
│           THOUGHT PHASE                 │
│  "I need to list open issues"           │
│  "I should use the GetIssues tool"      │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│           ACTION PHASE                  │
│  Tool: GetIssues                        │
│  Input: {"state": "open"}               │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│         OBSERVATION PHASE               │
│  "Found 5 open issues:                  │
│   #1: Bug in login                      │
│   #2: Feature request..."               │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│           THOUGHT PHASE                 │
│  "I have the information needed"        │
│  "I can now answer the user"            │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│         FINAL ANSWER PHASE              │
│  "Here are the open issues: ..."        │
└─────────────────────────────────────────┘
```

## Data Flow

### Configuration Loading

```
.env file
   │
   ├─ OPENAI_API_KEY ──────────┐
   ├─ GITHUB_TOKEN ────────────┼──▶ Config Class
   └─ GITHUB_REPOSITORY ───────┘
                                │
                                ▼
                        DeveloperAgent
```

### Task Execution

```
User Input
   │
   ▼
main.py (CLI Parser)
   │
   ├─ Validate Config
   │
   ├─ Create Agent
   │
   └─ Execute Task ──────────────────┐
                                     │
                                     ▼
                            DeveloperAgent
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                    ▼                ▼                ▼
              LangChain          GitHub           OpenAI
               Agent            Toolkit            GPT-4
                    │                │                │
                    └────────────────┼────────────────┘
                                     │
                                     ▼
                              GitHub REST API
                                     │
                                     ▼
                            Repository Data
                                     │
                                     ▼
                            Formatted Result
                                     │
                                     ▼
                               User Output
```

## Tool Categories

### Read Operations (Safe)
```
┌──────────────────────────┐
│  GetIssue                │  Fetch single issue
│  GetIssues               │  List issues
│  GetPR                   │  Fetch single PR
│  ListPRs                 │  List PRs
│  ListOpenPRs             │  List open PRs
│  ReadFile                │  Read file contents
│  SearchIssues            │  Search issues
│  SearchCode              │  Search code
│  Overview                │  Repository info
│  ListBranches            │  List branches
└──────────────────────────┘
```

### Write Operations (Careful)
```
┌──────────────────────────┐
│  CreateIssue             │  Create new issue
│  CommentOnIssue          │  Add comment
│  CreatePullRequest       │  Create PR
│  CreateFile              │  Create new file
│  UpdateFile              │  Modify file
│  DeleteFile              │  Remove file
│  CreateBranch            │  Create branch
│  SetActiveBranch         │  Switch branch
└──────────────────────────┘
```

## Security Considerations

### Authentication Flow

```
┌─────────────────┐
│  User Provides  │
│  Credentials    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  .env File      │
│  (Not in Git)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Config Loads   │
│  Variables      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Agent Uses     │
│  Credentials    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  API Calls      │
│  Authenticated  │
└─────────────────┘
```

### Token Permissions Required

```
repo scope
   ├─ repo:status
   ├─ repo_deployment
   ├─ public_repo
   └─ repo:invite

read:org
   └─ read:org

read:project
   └─ read:project
```

## Extension Points

### Adding Custom Tools

```python
from langchain.tools import Tool

def custom_tool_function(input: str) -> str:
    # Your custom logic
    return "Result"

custom_tool = Tool(
    name="CustomTool",
    func=custom_tool_function,
    description="Description of what the tool does"
)

# Add to agent
agent = DeveloperAgent(...)
agent.agent.tools.append(custom_tool)
```

### Using Different LLMs

```python
# GPT-3.5 (cheaper, faster)
agent = DeveloperAgent(model_name="gpt-3.5-turbo")

# GPT-4 (more capable)
agent = DeveloperAgent(model_name="gpt-4")

# Custom temperature
agent = DeveloperAgent(
    model_name="gpt-4",
    temperature=0.7  # More creative
)
```

### Repository-Specific Agents

```python
# Create agents for different repositories
repo1_agent = create_developer_agent(
    github_repository="org1/repo1"
)

repo2_agent = create_developer_agent(
    github_repository="org2/repo2"
)

# Use them independently
repo1_result = repo1_agent.run("List issues")
repo2_result = repo2_agent.run("List issues")
```

## Performance Characteristics

### Typical Response Times

```
Simple Read (GetIssue):        2-5 seconds
List Operations (GetIssues):   3-8 seconds
Search Operations:             5-10 seconds
Complex Multi-step:            10-30 seconds
Write Operations:              5-15 seconds
```

### API Rate Limits

```
GitHub API (Authenticated):    5,000 requests/hour
GitHub API (Unauthenticated):  60 requests/hour
OpenAI API:                    Rate varies by plan
```

## Error Handling Strategy

```
User Request
     │
     ▼
Try Execute
     │
     ├─ Success ──────────────────▶ Return Result
     │
     └─ Error
          │
          ├─ GitHub API Error
          │    ├─ Rate Limit ─────▶ Inform User
          │    ├─ Auth Error ─────▶ Check Token
          │    └─ Not Found ──────▶ Verify Params
          │
          ├─ OpenAI API Error
          │    ├─ Rate Limit ─────▶ Retry/Wait
          │    └─ Invalid Key ────▶ Check Config
          │
          └─ Parsing Error ────────▶ Simplify Task
```

## Deployment Options

### Option 1: CLI Tool
```
User Terminal
     │
     ▼
python main.py "task"
     │
     ▼
Result in Terminal
```

### Option 2: Python Package
```
User Python Script
     │
     ▼
from developer_agent import create_developer_agent
agent = create_developer_agent()
result = agent.run("task")
     │
     ▼
Use Result in Code
```

### Option 3: API Service (Future)
```
HTTP Request
     │
     ▼
Flask/FastAPI Server
     │
     ▼
Developer Agent
     │
     ▼
JSON Response
```

## Summary

The AI Squad Developer Agent architecture follows these principles:

1. **Modularity**: Separated concerns (config, agent, CLI)
2. **Extensibility**: Easy to add new tools and features
3. **Security**: Credentials managed via environment variables
4. **Usability**: Multiple interfaces (CLI, Python API)
5. **Reliability**: Comprehensive error handling
6. **Documentation**: Extensive guides and examples

The system integrates three major technologies:
- **LangChain**: Agent framework and orchestration
- **OpenAI GPT-4**: Natural language understanding
- **GitHub API**: Repository operations

Together, they enable natural language control of GitHub operations.
