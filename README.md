# 🤖 Agente de Automação Trello

Um agente Python para automatizar fluxos de trabalho no Trello, permitindo criar, mover e gerenciar cards automaticamente.

---

## ✨ Funcionalidades

- 📋 **Listar quadros** - Visualize todos os seus quadros do Trello
- ➕ **Criar cards** - Adicione novos cards com título e descrição
- 🔄 **Mover cards** - Transfira cards entre listas facilmente
- 💬 **Adicionar comentários** - Insira comentários em cards existentes
- 📊 **Listar cards** - Veja todos os cards de uma lista específica
- 🚀 **Automação diária** - Crie cards automaticamente e mova cards antigos

---

## 🚀 Começando

### Pré-requisitos

- Python 3.7 ou superior
- Conta no [Trello](https://trello.com/)
- VS Code ou qualquer editor de código

---

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/agente-trello.git
cd agente-trello
```

2. **Instale as dependências**
```bash
pip install py-trello python-dotenv
```

---

## Configure as Credenciais

- Acesse: https://trello.com/power-ups/admin
- Clique em "Create New Power-Up"
- Copie sua API Key na aba "API Key"
- Clique em "Token" para gerar seu token
- Crie um arquivo .env na raiz do projeto:
```env
TRELLO_API_KEY=sua_api_key_aqui
TRELLO_TOKEN=seu_token_aqui
```

---

## Execute o Agente
```bash
python agente.py
```

---

## 📋 Como usar

Menu Principal :

## Agente Trello - Automação
========================================
1. 📋 Listar meus quadros
2. ➕ Criar novo card
3. 🔄 Mover card entre listas
4. 💬 Adicionar comentário a um card
5. 📊 Listar cards de uma lista
6. 🚀 Executar automação diária
0. 👋 Sair
