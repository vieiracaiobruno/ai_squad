# 🎯 AI Squad Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        AI Squad System                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Input: Project Description
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         CrewAI Core                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Sequential Process Orchestration                    │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Agents     │     │    Tasks     │     │    Tools     │
└──────────────┘     └──────────────┘     └──────────────┘
        │                     │                     │
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                              ▼

┌─────────────────────────────────────────────────────────────┐
│                    Workflow Sequence                         │
│                                                              │
│  1. 👔 PROJECT MANAGER                                      │
│     ├─ Input: Project description                           │
│     ├─ Process: Analyze requirements, create plan           │
│     ├─ Tools: GitHub issues, milestones                     │
│     └─ Output: Detailed project plan                        │
│                      │                                       │
│                      ▼                                       │
│  2. 🏗️ TECH LEAD                                            │
│     ├─ Input: Project plan                                  │
│     ├─ Process: Define architecture, standards              │
│     ├─ Tools: GitHub branches, documentation                │
│     └─ Output: Technical architecture doc                   │
│                      │                                       │
│                      ▼                                       │
│  3. 💻 DEVELOPER                                            │
│     ├─ Input: Architecture and plan                         │
│     ├─ Process: Implement features                          │
│     ├─ Tools: GitHub commits, PRs                           │
│     └─ Output: Working code implementation                  │
│                      │                                       │
│                      ▼                                       │
│  4. 🧪 TESTER                                               │
│     ├─ Input: Implemented code                              │
│     ├─ Process: Test and validate quality                   │
│     ├─ Tools: GitHub issues, PR reviews                     │
│     └─ Output: Test report and validation                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Final Output                            │
│  • Complete project plan                                     │
│  • Technical architecture documentation                      │
│  • Implementation code and commits                           │
│  • Test results and quality report                           │
└─────────────────────────────────────────────────────────────┘

## Component Details

### Agents Layer
┌──────────────────────────────────────────┐
│ Agent Properties:                         │
│ • Role: Specialized function              │
│ • Goal: Specific objective                │
│ • Backstory: Experience and expertise     │
│ • Tools: Available capabilities           │
│ • LLM: GPT-4 (configurable)              │
│ • Allow Delegation: PM & TL can delegate │
└──────────────────────────────────────────┘

### Tools Layer
┌──────────────────────────────────────────────────────────────────┐
│ GitHub Integration (via PyGithub + LangChain):                   │
│                                                                   │
│ 8 Specialized Tools:                                             │
│ 1. get_github_repo_info - Repository information and stats       │
│ 2. list_github_repo_files - Browse repository structure          │
│ 3. read_github_file - Read file contents from repos              │
│ 4. search_github_code - Search code across GitHub                │
│ 5. list_github_issues - List repository issues                   │
│ 6. get_github_issue - Get detailed issue information             │
│ 7. list_github_prs - List pull requests                          │
│ 8. search_github_repositories - Search for repositories          │
│                                                                   │
│ Authentication Methods:                                           │
│ • Personal Access Token (PAT) - Simple setup                     │
│ • GitHub App - Production/organizational use                     │
└──────────────────────────────────────────────────────────────────┘

### External Services
┌──────────────────────────────────────────┐
│ OpenAI API (GPT-4)                        │
│ └─ Language model for agents              │
│                                           │
│ GitHub API (via PyGithub)                 │
│ └─ Repository operations and code search  │
└──────────────────────────────────────────┘

## Data Flow

```
User Input
    │
    ├─> Project Description
    │
    ▼
CrewAI Framework
    │
    ├─> Parse & Validate
    ├─> Create Agent Instances
    ├─> Initialize Tasks
    │
    ▼
Sequential Execution
    │
    ├─> Task 1 (Planning)
    │   ├─> Call OpenAI API
    │   ├─> Use GitHub Tools
    │   └─> Generate Output
    │
    ├─> Task 2 (Architecture)
    │   ├─> Receive Task 1 Output
    │   ├─> Call OpenAI API
    │   ├─> Use GitHub Tools
    │   └─> Generate Output
    │
    ├─> Task 3 (Development)
    │   ├─> Receive Task 2 Output
    │   ├─> Call OpenAI API
    │   ├─> Use GitHub Tools
    │   └─> Generate Output
    │
    └─> Task 4 (Testing)
        ├─> Receive Task 3 Output
        ├─> Call OpenAI API
        ├─> Use GitHub Tools
        └─> Generate Output
    │
    ▼
Final Result Aggregation
    │
    └─> Return Complete Results
```

## Module Structure

```
ai_squad/
│
├── main.py
│   └─ Entry point
│       ├─ Load environment
│       ├─ Validate config
│       └─ Call run_it_squad()
│
├── crew.py
│   └─ Squad orchestration
│       ├─ create_it_squad_crew()
│       │   ├─ Create agents
│       │   ├─ Create tasks
│       │   └─ Configure crew
│       │
│       └─ run_it_squad()
│           ├─ Initialize crew
│           └─ Execute kickoff()
│
├── agents.py
│   └─ Agent definitions
│       ├─ get_llm()
│       ├─ create_project_manager()
│       ├─ create_tech_lead()
│       ├─ create_developer()
│       └─ create_tester()
│
├── tasks.py
│   └─ Task definitions
│       ├─ create_planning_task()
│       ├─ create_architecture_task()
│       ├─ create_implementation_task()
│       └─ create_testing_task()
│
└── tools.py
    └─ Tool integration
        ├─ Load environment
        ├─ Initialize GitHub API
        └─ Export github_tools
```

## Configuration Flow

```
.env file
    │
    ├─> OPENAI_API_KEY ──────┐
    ├─> GITHUB_TOKEN ────────┤
    └─> OPENAI_MODEL_NAME ───┤
                              │
                              ▼
                        Load Environment
                              │
                              ├─> tools.py
                              │   └─> Initialize GitHub tools
                              │
                              └─> agents.py
                                  └─> Initialize LLM
                                      └─> Create agents
```

## GitHub Tools Integration

```
tools.py initialization flow:
    │
    ├─> Check GITHUB_TOKEN
    │   ├─> If present:
    │   │   ├─> Create PyGithub client
    │   │   ├─> Authenticate with GitHub
    │   │   └─> Create 8 specialized tools
    │   └─> If missing → Check GitHub App credentials
    │
    ├─> Check GITHUB_APP_ID + GITHUB_APP_PRIVATE_KEY
    │   ├─> If present:
    │   │   ├─> Use LangChain GitHubToolkit
    │   │   └─> Create tools via GitHub App
    │   └─> If missing → Return empty tools list
    │
    └─> Return github_tools list
        └─> Used by all agents

Available GitHub Tools:
1. get_github_repo_info      - Get repository information
2. list_github_repo_files    - List files in repository
3. read_github_file          - Read file contents
4. search_github_code        - Search code on GitHub
5. list_github_issues        - List repository issues
6. get_github_issue          - Get issue details
7. list_github_prs           - List pull requests
8. search_github_repositories - Search repositories
```

## Error Handling

```
main.py
    │
    ├─ Check OPENAI_API_KEY
    │  └─ If missing → Exit with error
    │
    ├─ Check GITHUB_TOKEN
    │  └─ If missing → Warning (optional)
    │
    └─ Execute squad
       │
       ├─ Try: run_it_squad()
       │
       └─ Catch exceptions
          └─ Display error message
```
