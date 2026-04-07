# 🤖 Agente de Automação Trello

Um agente Python para automatizar fluxos de trabalho no Trello, permitindo criar, mover e gerenciar cards automaticamente.

![Python 3.7](https://img.shields.io/badge/python-3.7+-blue.svg)

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

## 📋 Como Usar

Menu Principal :

## Agente Trello - Automação
========================================
1. 📋 Listar meus quadros
2. ➕ Criar novo card
3. 🔄 Mover card entre listas
4. 💬 Adicionar comentário a um card
5. 📊 Listar cards de uma lista

---

## Exemplo de Saída da Automação

## Iniciando Automação Diária
==================================================

Quadros disponíveis :
  1. Projeto Pessoal
  2. Trabalho
  3. Estudos

📁 Nome do quadro para automação: Projeto Pessoal

✅ Quadro selecionado: Projeto Pessoal

Listas disponíveis :
  1. To Do
  2. Doing
  3. Done

📝 Nome da lista para criar cards: To Do
✅ Nome da lista para mover cards concluídos: Done

📝 Criando card: Tarefa do dia - 2024-01-15
✅ Card criado com sucesso!

🔄 Verificando cards antigos...
✅ Card 'Reunião antiga' movido para 'Done'

✅ Automação concluída!
   - Card criado: Tarefa do dia - 2024-01-15
   - Cards movidos: 1

---

## 🎯 Exemplos de Automação Personalizada

- Criar card com checklist automático

card = lista.add_card(name="Revisão Diária")
card.add_checklist("Tarefas do dia", [
    "Verificar emails",
    "Atualizar status do projeto",
    "Fazer commit do código"
])

- Mover cards com label específica

for card in lista.list_cards():
    for label in card.labels:
        if label.name == "urgente":
            card.change_list(lista_destino.id)

- Agendar execução automática

Windows (Agendador de Tarefas):
```
batch
C:\Python39\python.exe C:\projetos\agente_automatico.py
```
Linux/Mac (Cron):
```
bash
# Executar todo dia às 9h
0 9 * * * /usr/bin/python3 /home/usuario/agente_automatico.py             
```

---

## 🛠️ Estrutura do Projeto
```
agente-trello/
├── .env                # Credenciais da API (não compartilhar)
├── .gitignore          # Arquivos ignorados pelo Git
├── agente.py           # Código principal do agente
├── automacao_total.py  # Versão sem interação (opcional)
└── README.md           # Documentação
```

---

## 🔒 Segurança

- As credenciais são armazenadas no arquivo .env (não versionado)
- Nunca compartilhe sua API Key ou Token
- Revogue tokens não utilizados nas configurações do Trello
- Use .gitignore para evitar commits acidentais

---

## 🤝 Contribuindo

- Faça um Fork do projeto
- Crie sua branch (git checkout -b feature/nova-funcionalidade)
- Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')
- Push para a branch (git push origin feature/nova-funcionalidade)
- Abra um Pull Request

---

## 👤 Autor

Marcus Guedes

- LinkedIn : https://www.linkedin.com/in/marcusguedes
- GitHub : https://github.com/MCLG1661
