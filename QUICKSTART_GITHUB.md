# 🚀 Guia Rápido - Integração com GitHub

## ⚡ Setup Rápido (5 minutos)

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Obter GitHub Token
1. Acesse: https://github.com/settings/tokens
2. Clique: "Generate new token" → "Generate new token (classic)"
3. Nome: "AI Squad"
4. Selecione: ✅ `repo` ✅ `workflow` ✅ `read:org`
5. Copie o token (começa com `ghp_`)

### 3. Configurar
```bash
cp .env.example .env
# Edite .env e adicione:
# GITHUB_TOKEN=ghp_seu_token_aqui
```

### 4. Verificar
```bash
python verify_github_integration.py
```

### 5. Testar
```bash
python example_github_integration.py
```

## 🔧 Ferramentas Disponíveis

| Ferramenta | Uso |
|-----------|-----|
| `get_github_repo_info` | Informações de repositório |
| `list_github_repo_files` | Listar arquivos |
| `read_github_file` | Ler arquivo |
| `search_github_code` | Buscar código |
| `list_github_issues` | Listar issues |
| `get_github_issue` | Detalhes de issue |
| `list_github_prs` | Listar PRs |
| `search_github_repositories` | Buscar repositórios |

## 💡 Exemplos de Uso

### Pesquisar Repositórios
```python
from crew import run_it_squad

project = """
Developer: Use GitHub tools to find 5 popular Python web frameworks.
Search for "web framework language:python stars:>1000"
"""

run_it_squad(project)
```

### Analisar Código
```python
project = """
Developer: Analyze the FastAPI repository structure.
1. Get info about "tiangolo/fastapi"
2. List files in the root directory
3. Read the README.md file
"""

run_it_squad(project)
```

### Pesquisar Exemplos
```python
project = """
Developer: Find examples of JWT authentication in Python.
Search GitHub code for "jwt authentication language:python"
Analyze the top 5 results.
"""

run_it_squad(project)
```

## 🆘 Problemas Comuns

### "No GitHub credentials found"
- ✅ Verifique se o `.env` existe
- ✅ Verifique se `GITHUB_TOKEN` está no `.env`
- ✅ Verifique se não há espaços extras

### "Authentication failed"
- ✅ Token correto? Deve começar com `ghp_`
- ✅ Token expirado? Crie um novo
- ✅ Escopos corretos? Deve ter `repo`, `workflow`, `read:org`

### "Rate limit exceeded"
- ✅ GitHub tem limite de 60 requests/hora sem autenticação
- ✅ Com token: 5000 requests/hora
- ✅ Aguarde 1 hora ou use outro token

## 📚 Mais Informações

- [README.md](README.md) - Documentação completa em inglês
- [GUIA_PT.md](GUIA_PT.md) - Guia completo em português
- [ARCHITECTURE.md](ARCHITECTURE.md) - Detalhes técnicos
- [GITHUB_INTEGRATION_SUMMARY.md](GITHUB_INTEGRATION_SUMMARY.md) - Resumo da implementação

## 🎯 Próximos Passos

1. ✅ Configure o GitHub Token
2. ✅ Execute `verify_github_integration.py`
3. ✅ Teste com `example_github_integration.py`
4. ✅ Crie seus próprios projetos usando GitHub tools!

---

**Dica**: As ferramentas do GitHub são **automáticas**! Os agentes as usam quando necessário. Você só precisa fornecer o token. 🎉
