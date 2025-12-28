# 🇧🇷 Guia Completo - AI Squad com CrewAI

## 📖 Visão Geral

Este projeto implementa um **Squad de TI Automatizado** usando o framework CrewAI. O squad é composto por 4 agentes de IA especializados que trabalham juntos de forma colaborativa, simulando uma equipe real de desenvolvimento de software.

## 🎯 O que este projeto faz?

O AI Squad pode **planejar, arquitetar, desenvolver e testar** projetos de software de forma autônoma. Você fornece uma descrição do projeto, e os agentes trabalham em sequência:

1. **Project Manager** - Analisa requisitos e cria um plano detalhado
2. **Tech Lead** - Define arquitetura técnica e padrões
3. **Developer** - Implementa as funcionalidades
4. **Tester** - Valida qualidade e testa tudo

## 🚀 Começando

### Passo 1: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 2: Configurar Credenciais

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione suas credenciais:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
GITHUB_TOKEN=ghp_xxxxxxxxxxxxx
```

#### Como obter a OpenAI API Key:

1. Acesse https://platform.openai.com/
2. Faça login ou crie uma conta
3. Vá em "API Keys" no menu
4. Clique em "Create new secret key"
5. Copie a chave (começa com `sk-proj-`)

#### Como obter o GitHub Token:

O projeto suporta duas formas de autenticação com o GitHub:

**Opção 1: Personal Access Token (Recomendado para começar)**

Mais simples e rápida de configurar:

1. Acesse https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome descritivo (ex: "AI Squad Token")
4. **Selecione os seguintes escopos (permissões):**
   - ✅ `repo` - Acesso completo a repositórios
   - ✅ `workflow` - Atualizar workflows
   - ✅ `read:org` - Ler informações da organização (opcional)
5. Clique em "Generate token"
6. **IMPORTANTE**: Copie o token imediatamente (começa com `ghp_`)
7. Adicione ao arquivo `.env`:
   ```
   GITHUB_TOKEN=ghp_seu_token_aqui
   ```

**Opção 2: GitHub App (Para produção/organizações)**

Para ambientes de produção ou uso organizacional:

1. Crie um GitHub App em https://github.com/settings/apps/new
2. Configure as permissões necessárias
3. Gere uma chave privada (.pem)
4. Instale o app no seu repositório ou organização
5. Adicione ao arquivo `.env`:
   ```
   GITHUB_APP_ID=123456
   GITHUB_APP_PRIVATE_KEY=/caminho/para/chave.pem
   GITHUB_REPOSITORY=owner/repo
   ```

> 💡 **Dica**: Para uso pessoal e aprendizado, use a Opção 1 (Personal Access Token). É muito mais simples!
3. Dê um nome (ex: "AI Squad")
4. Selecione os escopos:
   - `repo` (acesso total aos repositórios)
   - `workflow` (atualizar workflows)
   - `admin:org` (gerenciar organizações)
5. Clique em "Generate token"
6. Copie o token (começa com `ghp_`)

### Passo 3: Executar o Squad

```bash
python main.py
```

## 💡 Exemplos de Uso

### Exemplo 1: Projeto Básico (main.py)

O arquivo `main.py` já vem com um exemplo de projeto TODO app. Basta executar:

```bash
python main.py
```

### Exemplo 2: Projetos Customizados (examples.py)

O arquivo `examples.py` contém vários exemplos prontos:

```python
# Exemplo de aplicação web
python examples.py  # Descomente a função desejada

# Ou use programaticamente:
from crew import run_it_squad

project = """
Criar um sistema de e-commerce com:
- Catálogo de produtos
- Carrinho de compras
- Sistema de pagamento
- Painel administrativo
"""

result = run_it_squad(project)
```

### Exemplo 3: Seu Próprio Projeto

Crie seu próprio script:

```python
from crew import run_it_squad

# Descreva seu projeto em português
meu_projeto = """
Desenvolver uma API de gerenciamento de biblioteca com:
- Cadastro de livros (título, autor, ISBN, categoria)
- Sistema de empréstimos
- Controle de devoluções
- Relatórios de livros mais emprestados
- Autenticação de usuários
- Documentação OpenAPI
"""

# Execute o squad
resultado = run_it_squad(meu_projeto)

# O resultado conterá o output de cada agente
print(resultado)
```

## 🔧 Estrutura dos Arquivos

```
ai_squad/
├── .env.example          # Template de configuração
├── README.md            # Documentação em inglês
├── GUIA_PT.md          # Este arquivo (guia em português)
├── requirements.txt     # Dependências Python
├── main.py             # Script principal
├── examples.py         # Exemplos prontos
├── crew.py             # Configuração do squad
├── agents.py           # Definição dos agentes
├── tasks.py            # Definição das tarefas
└── tools.py            # Integração com GitHub
```

## 👥 Os Agentes

### 👔 Project Manager (Gerente de Projetos)

**Responsabilidades:**
- Analisar requisitos do projeto
- Definir escopo e objetivos
- Criar lista de tarefas priorizadas
- Identificar riscos e dependências
- Definir marcos e prazos

**Habilidades:**
- Experiência em metodologias ágeis
- Gestão de projetos
- Comunicação efetiva

### 🏗️ Tech Lead (Líder Técnico)

**Responsabilidades:**
- Definir arquitetura do sistema
- Escolher tecnologias apropriadas
- Estabelecer padrões de código
- Revisar código
- Documentar decisões técnicas

**Habilidades:**
- Arquitetura de software
- Padrões de design
- Clean code
- Mentoria técnica

### 💻 Developer (Desenvolvedor)

**Responsabilidades:**
- Implementar funcionalidades
- Seguir padrões estabelecidos
- Escrever código limpo
- Criar commits descritivos
- Responder a code reviews

**Habilidades:**
- Múltiplas linguagens de programação
- Frameworks modernos
- Testes unitários
- Git e versionamento

### 🧪 Tester (Testador/QA)

**Responsabilidades:**
- Criar casos de teste
- Executar testes manuais e automatizados
- Identificar bugs
- Validar requisitos
- Criar issues para bugs

**Habilidades:**
- Testes automatizados
- Estratégias de QA
- Encontrar edge cases
- Ferramentas de teste

## 🛠️ Integração com GitHub

Os agentes têm acesso às seguintes ferramentas do GitHub:

- **Repositórios**: Criar, ler, atualizar
- **Branches**: Criar e gerenciar branches
- **Commits**: Fazer commits de código
- **Pull Requests**: Criar e revisar PRs
- **Issues**: Criar e gerenciar issues
- **Reviews**: Comentar em code reviews

Para usar essas ferramentas, certifique-se de configurar o `GITHUB_TOKEN` no arquivo `.env`.

## ⚙️ Customização

### Modificar Comportamento dos Agentes

Edite o arquivo `agents.py` para ajustar:

```python
def create_project_manager() -> Agent:
    return Agent(
        role="Project Manager",
        goal="Seu objetivo customizado...",
        backstory="Sua história customizada...",
        # ... outras configurações
    )
```

### Modificar Tarefas

Edite o arquivo `tasks.py` para ajustar as tarefas:

```python
def create_planning_task(project_description: str) -> Task:
    return Task(
        description="""
        Suas instruções customizadas...
        """,
        agent=create_project_manager(),
        expected_output="Seu output esperado..."
    )
```

### Adicionar Novos Agentes

1. Crie uma nova função em `agents.py`:

```python
def create_devops_engineer() -> Agent:
    return Agent(
        role="DevOps Engineer",
        goal="Configurar CI/CD e infraestrutura",
        backstory="Especialista em DevOps com 8 anos de experiência...",
        verbose=True,
        llm=get_llm(),
        tools=github_tools
    )
```

2. Adicione uma tarefa em `tasks.py`:

```python
def create_deployment_task() -> Task:
    return Task(
        description="Configurar pipeline de CI/CD...",
        agent=create_devops_engineer(),
        expected_output="Pipeline configurado e documentado"
    )
```

3. Adicione ao crew em `crew.py`:

```python
devops = create_devops_engineer()
crew = Crew(
    agents=[project_manager, tech_lead, developer, tester, devops],
    # ...
)
```

## 🐛 Solução de Problemas

### Erro: "OPENAI_API_KEY não encontrada"

**Solução**: Configure a chave no arquivo `.env`:
```env
OPENAI_API_KEY=sua-chave-aqui
```

### Aviso: "GitHub token not found"

**Solução**: O squad funciona sem GitHub, mas para usar as ferramentas do GitHub, configure:
```env
GITHUB_TOKEN=seu-token-aqui
```

### Erro: "Rate limit exceeded"

**Solução**: Você atingiu o limite de requisições da API OpenAI. Aguarde ou aumente seu plano.

### Erro de instalação de dependências

**Solução**: Certifique-se de usar Python 3.8+:
```bash
python --version  # Deve ser 3.8 ou superior
pip install --upgrade pip
pip install -r requirements.txt
```

## 📊 Entendendo os Resultados

Quando o squad termina, você recebe um resultado detalhado com:

1. **Plano do Projeto** - Do Project Manager
2. **Arquitetura Técnica** - Do Tech Lead
3. **Código Implementado** - Do Developer
4. **Relatório de Testes** - Do Tester

Cada seção contém insights detalhados e recomendações.

## 💰 Custos

Este projeto usa a API da OpenAI, que é paga:

- **GPT-4**: ~$0.03 por 1K tokens de input, ~$0.06 por 1K tokens de output
- Uma execução típica pode usar 10K-50K tokens (~$0.50-$2.50)

**Dica**: Para reduzir custos, você pode:
- Usar GPT-3.5-turbo (mais barato): Configure `OPENAI_MODEL_NAME=gpt-3.5-turbo` no `.env`
- Descrever projetos mais simples
- Desabilitar o modo verbose nos agentes

## 🎓 Recursos para Aprender Mais

- [Documentação CrewAI](https://github.com/crewAIInc/crewAI)
- [Documentação LangChain](https://python.langchain.com/)
- [API OpenAI](https://platform.openai.com/docs)
- [GitHub API](https://docs.github.com/en/rest)

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📞 Suporte

Se tiver dúvidas ou problemas:

1. Verifique a seção de Solução de Problemas acima
2. Consulte a documentação dos frameworks utilizados
3. Abra uma issue no GitHub

## ⚠️ Avisos Importantes

1. **Segurança**: Nunca commite seu arquivo `.env` com credenciais reais
2. **Custos**: Monitore o uso da API OpenAI para evitar custos inesperados
3. **GitHub**: Tenha cuidado com operações que modificam repositórios
4. **Teste**: Sempre teste em um ambiente de desenvolvimento primeiro

## 🌟 Dicas de Uso

1. **Seja específico**: Quanto mais detalhado seu projeto, melhores os resultados
2. **Itere**: Execute o squad várias vezes refinando a descrição
3. **Revise**: Os agentes são auxiliares, sempre revise o output
4. **Customize**: Ajuste os agentes para seu contexto específico
5. **Combine**: Use com outras ferramentas de desenvolvimento

---

**Desenvolvido com ❤️ usando CrewAI**
