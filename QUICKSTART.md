# 🚀 Quick Start Guide

## Setup em 3 Passos

### 1. Instalar
```bash
pip install -r requirements.txt
```

### 2. Configurar
Crie arquivo `.env`:
```env
OPENAI_API_KEY=sua-chave-aqui
GITHUB_TOKEN=seu-token-aqui
```

### 3. Executar
```bash
python main.py
```

## Verificar Setup
```bash
python verify_setup.py
```

## Documentação Completa
- 🇺🇸 [README.md](README.md) - English
- 🇧🇷 [GUIA_PT.md](GUIA_PT.md) - Português

## Estrutura do Squad

```
Project Manager → Tech Lead → Developer → Tester
     ↓              ↓            ↓          ↓
   Plano      Arquitetura    Código     Testes
```

## Exemplo Rápido

```python
from crew import run_it_squad

projeto = """
Criar uma API REST de gerenciamento de tarefas:
- CRUD de tarefas
- Autenticação
- Testes
"""

resultado = run_it_squad(projeto)
```

## Custos Estimados

| Modelo | Custo por execução |
|--------|-------------------|
| GPT-4 | $0.50 - $2.50 |
| GPT-3.5 | $0.05 - $0.25 |

## Suporte

- 📖 Veja [GUIA_PT.md](GUIA_PT.md) para guia completo
- 🐛 Issues: Abra um issue no GitHub
- 💡 Exemplos: Veja [examples.py](examples.py)
