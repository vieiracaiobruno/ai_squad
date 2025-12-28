# 🚀 AI Squad - CrewAI IT Team

Um projeto de squad de TI automatizado usando CrewAI, com integração ao GitHub via LangChain.

## 📋 Sobre o Projeto

Este projeto implementa um squad completo de TI usando o framework CrewAI, composto por quatro agentes especializados que trabalham em conjunto para planejar, arquitetar, desenvolver e testar projetos de software:

- **👔 Project Manager**: Coordena o projeto, define escopo e gerencia o workflow
- **🏗️ Tech Lead**: Define arquitetura técnica e padrões de desenvolvimento
- **💻 Developer**: Implementa funcionalidades seguindo as especificações
- **🧪 Tester**: Garante qualidade através de testes rigorosos

Cada agente tem acesso a ferramentas do GitHub através da integração com PyGithub e LangChain, permitindo:
- **Buscar informações de repositórios** - Obter detalhes, estatísticas e metadados
- **Listar e ler arquivos** - Explorar estrutura de diretórios e ler conteúdo de arquivos
- **Pesquisar código** - Buscar código em todos os repositórios do GitHub
- **Gerenciar issues** - Listar, visualizar e criar issues
- **Trabalhar com pull requests** - Listar e analisar PRs abertos
- **Pesquisar repositórios** - Encontrar projetos relevantes no GitHub
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

**GitHub Token (Método Recomendado):**

Este projeto suporta duas formas de autenticação com o GitHub:

**Opção 1: Personal Access Token (PAT) - Recomendado para começar**

Mais simples e rápida de configurar. Ideal para desenvolvedores individuais:

1. Acesse https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome descritivo (ex: "AI Squad Token")
4. Selecione os escopos necessários:
   - `repo` - Acesso completo a repositórios privados e públicos
   - `workflow` - Atualizar workflows do GitHub Actions
   - `read:org` - Ler dados da organização (opcional, apenas se precisar)
5. Clique em "Generate token" e copie o token
6. Adicione ao arquivo `.env`:
   ```
   GITHUB_TOKEN=seu_token_aqui
   ```

**Opção 2: GitHub App - Para produção**

Mais segura para uso organizacional e produção:

1. Crie um GitHub App: https://github.com/settings/apps/new
2. Configure as permissões necessárias
3. Gere uma chave privada
4. Instale o app no seu repositório ou organização
5. Adicione ao arquivo `.env`:
   ```
   GITHUB_APP_ID=seu_app_id
   GITHUB_APP_PRIVATE_KEY=caminho_para_chave.pem
   GITHUB_REPOSITORY=owner/repo
   ```

Para mais detalhes sobre GitHub Apps: https://docs.github.com/en/apps/creating-github-apps

### Verificar a Configuração

Antes de executar o squad, você pode verificar se tudo está configurado corretamente:

```bash
# Verificar configuração básica (não requer OpenAI API Key)
python verify_github_integration.py

# Verificar configuração completa (requer todas as credenciais)
python verify_setup.py
```

Esses scripts vão verificar:
- ✅ Se as dependências estão instaladas
- ✅ Se as credenciais estão configuradas
- ✅ Se as ferramentas do GitHub estão funcionando

## 🚀 Como Usar

### Uso Básico

Execute o script principal:

```bash
python main.py
```

### Testar Integração com GitHub

Para ver o Developer agent usando as ferramentas do GitHub:

```bash
python example_github_integration.py
```

Este exemplo demonstra:
- Busca de repositórios no GitHub
- Análise de código de projetos existentes
- Leitura de arquivos de repositórios
- Pesquisa de exemplos de código

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
└── tools.py            # Integração com GitHub via PyGithub/LangChain
```

## 🔧 Ferramentas do GitHub

O projeto inclui integração completa com GitHub, fornecendo 8 ferramentas especializadas para os agentes:

### Ferramentas Disponíveis

1. **get_github_repo_info** - Obter informações detalhadas de um repositório
   - Estatísticas, descrição, linguagens, etc.

2. **list_github_repo_files** - Listar arquivos e diretórios
   - Explorar estrutura de repositórios

3. **read_github_file** - Ler conteúdo de arquivos
   - Analisar código-fonte e documentação

4. **search_github_code** - Buscar código no GitHub
   - Encontrar exemplos e implementações

5. **list_github_issues** - Listar issues abertas
   - Acompanhar bugs e funcionalidades

6. **get_github_issue** - Obter detalhes de uma issue específica
   - Analisar problemas em profundidade

7. **list_github_prs** - Listar pull requests abertos
   - Revisar mudanças propostas

8. **search_github_repositories** - Buscar repositórios
   - Descobrir projetos e bibliotecas

### Como Funciona

O Developer agent (e outros agentes) podem usar essas ferramentas automaticamente quando precisam:
- Pesquisar exemplos de código
- Analisar projetos similares
- Buscar soluções para problemas
- Explorar estruturas de repositórios
- Acompanhar issues e PRs

## 🤖 Agentes

### Project Manager
- **Papel**: Gerente de Projetos
- **Objetivo**: Coordenar o projeto e garantir eficiência
- **Habilidades**: Planejamento, gestão de riscos, comunicação
- **Ferramentas**: Todas as ferramentas do GitHub

### Tech Lead
- **Papel**: Líder Técnico
- **Objetivo**: Definir arquitetura e melhores práticas
- **Habilidades**: Arquitetura de software, code review, mentoria
- **Ferramentas**: Todas as ferramentas do GitHub

### Developer
- **Papel**: Desenvolvedor
- **Objetivo**: Implementar funcionalidades de alta qualidade
- **Habilidades**: Programação, clean code, testes
- **Ferramentas**: Todas as ferramentas do GitHub (foco em code search e file reading)

### Tester
- **Papel**: Engenheiro de QA
- **Objetivo**: Garantir qualidade através de testes
- **Habilidades**: Testes automatizados/manuais, QA
- **Ferramentas**: Todas as ferramentas do GitHub (foco em issues e PRs)

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
