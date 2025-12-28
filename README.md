# 🚀 AI Squad - CrewAI IT Team

Um projeto de squad de TI automatizado usando CrewAI, com integração ao GitHub via LangChain.

## 📋 Sobre o Projeto

Este projeto implementa um squad completo de TI usando o framework CrewAI, composto por quatro agentes especializados que trabalham em conjunto para planejar, arquitetar, desenvolver e testar projetos de software:

- **👔 Project Manager**: Coordena o projeto, define escopo e gerencia o workflow
- **🏗️ Tech Lead**: Define arquitetura técnica e padrões de desenvolvimento
- **💻 Developer**: Implementa funcionalidades seguindo as especificações
- **🧪 Tester**: Garante qualidade através de testes rigorosos

Cada agente tem acesso a ferramentas do GitHub através da integração com LangChain, permitindo:
- Criar e gerenciar repositórios
- Criar branches e fazer commits
- Abrir e revisar pull requests
- Criar e gerenciar issues
- E muito mais!

## 🛠️ Tecnologias Utilizadas

- **CrewAI**: Framework para criar e orquestrar agentes de IA
- **LangChain**: Para integração com ferramentas externas
- **OpenAI GPT-4**: Modelo de linguagem para os agentes
- **GitHub API**: Para operações no GitHub
- **Python 3.8+**: Linguagem de programação

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/vieiracaiobruno/ai_squad.git
cd ai_squad
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione suas credenciais:

```env
# Obrigatório - OpenAI API Key
OPENAI_API_KEY=sua_chave_openai_aqui

# Obrigatório - GitHub Personal Access Token
GITHUB_TOKEN=seu_token_github_aqui

# Opcional - Configuração do modelo
OPENAI_MODEL_NAME=gpt-4
```

#### Como obter as credenciais:

**OpenAI API Key:**
1. Acesse https://platform.openai.com/
2. Faça login ou crie uma conta
3. Vá para API Keys
4. Crie uma nova chave API

**GitHub Token:**
1. Acesse https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome descritivo
4. Selecione os escopos necessários: `repo`, `workflow`, `admin:org`
5. Clique em "Generate token" e copie o token

## 🚀 Como Usar

### Uso Básico

Execute o script principal:

```bash
python main.py
```

### Personalizar o Projeto

Edite o arquivo `main.py` e modifique a variável `project_description` com a descrição do seu projeto:

```python
project_description = """
Seu projeto personalizado aqui...
"""
```

### Uso Programático

Você também pode usar o squad programaticamente em seus próprios scripts:

```python
from crew import run_it_squad

# Defina seu projeto
project_description = """
Desenvolver uma API de e-commerce...
"""

# Execute o squad
result = run_it_squad(project_description)

# Use os resultados
print(result)
```

## 📁 Estrutura do Projeto

```
ai_squad/
├── .env.example          # Template de variáveis de ambiente
├── .gitignore           # Arquivos ignorados pelo Git
├── README.md            # Este arquivo
├── requirements.txt     # Dependências do projeto
├── main.py             # Script principal de execução
├── crew.py             # Configuração da crew
├── agents.py           # Definição dos agentes
├── tasks.py            # Definição das tarefas
└── tools.py            # Integração com GitHub via LangChain
```

## 🤖 Agentes

### Project Manager
- **Papel**: Gerente de Projetos
- **Objetivo**: Coordenar o projeto e garantir eficiência
- **Habilidades**: Planejamento, gestão de riscos, comunicação
- **Ferramentas**: GitHub API (issues, milestones, projects)

### Tech Lead
- **Papel**: Líder Técnico
- **Objetivo**: Definir arquitetura e melhores práticas
- **Habilidades**: Arquitetura de software, code review, mentoria
- **Ferramentas**: GitHub API (branches, PRs, code review)

### Developer
- **Papel**: Desenvolvedor
- **Objetivo**: Implementar funcionalidades de alta qualidade
- **Habilidades**: Programação, clean code, testes
- **Ferramentas**: GitHub API (commits, branches, PRs)

### Tester
- **Papel**: Engenheiro de QA
- **Objetivo**: Garantir qualidade através de testes
- **Habilidades**: Testes automatizados/manuais, QA
- **Ferramentas**: GitHub API (issues, PR reviews)

## 🔄 Workflow do Squad

1. **Planejamento**: Project Manager analisa requisitos e cria plano de ação
2. **Arquitetura**: Tech Lead define arquitetura técnica e padrões
3. **Desenvolvimento**: Developer implementa as funcionalidades
4. **Testes**: Tester valida qualidade e identifica bugs

## 🔧 Customização

### Modificar Agentes

Edite o arquivo `agents.py` para ajustar:
- Roles (papéis)
- Goals (objetivos)
- Backstories (histórico)
- Tools (ferramentas disponíveis)

### Modificar Tasks

Edite o arquivo `tasks.py` para ajustar:
- Descrições das tarefas
- Contexto fornecido
- Outputs esperados

### Adicionar Novas Ferramentas

Edite o arquivo `tools.py` para adicionar mais ferramentas do LangChain.

## 📚 Recursos Adicionais

- [Documentação CrewAI](https://github.com/crewAIInc/crewAI)
- [Documentação LangChain](https://python.langchain.com/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👤 Autor

Caio Bruno Vieira

## 🙏 Agradecimentos

- [CrewAI](https://github.com/crewAIInc/crewAI) pelo framework incrível
- [LangChain](https://github.com/langchain-ai/langchain) pelas ferramentas de integração
- OpenAI pelo GPT-4
