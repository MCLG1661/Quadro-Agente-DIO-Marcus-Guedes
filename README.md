# ⚙️ Trello Workflow Automation

*Automação de workflows e gerenciamento de tarefas com Python e Trello API*

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-API-0052CC?logo=trello&logoColor=white) 
![Workflow Automation](https://img.shields.io/badge/Workflow-Automation-2E8B57)
![API](https://img.shields.io/badge/Integration-REST%20API-orange)
![dotenv](https://img.shields.io/badge/Security-.env-yellow)
![DIO](https://img.shields.io/badge/DIO-Project-5A0FC8)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

O **Trello Automation Agent** é uma aplicação Python desenvolvida para automatizar
operações e fluxos de trabalho no Trello.

A solução integra-se ao Trello para permitir a criação, movimentação, consulta
e atualização de cards, além da execução de rotinas automatizadas para gerenciamento
de tarefas.

O projeto demonstra a aplicação prática de **Python, integração com APIs,
automação de processos e gerenciamento seguro de credenciais**.

---

## 🎯 Objetivo

Automatizar tarefas repetitivas de gerenciamento de projetos no Trello por meio
de uma aplicação Python.

A solução permite executar operações como :

- Consultar quadros
- Criar cards
- Movimentar cards entre listas
- Adicionar comentários
- Consultar cards
- Automatizar rotinas recorrentes

---

## 🏗️ Arquitetura Visual

<img width="800" height="400" alt="ChatGPT Image 12 de ago  de 2026, 19_55_15" src="https://github.com/user-attachments/assets/0b15ce53-1ebb-4168-bcd4-bde2541164de" />

A arquitetura do projeto separa a interação com o usuário, as operações de automação
e a comunicação com a API do Trello.

---

## ✨ Funcionalidades

📋 Listagem de Quadros

Consulta os quadros disponíveis na conta integrada.

➕ Criação de Cards

Permite criar novos cards informando título e descrição.

🔄 Movimentação de Cards

Transfere cards entre diferentes listas de um quadro.

💬 Comentários

Permite adicionar comentários a cards existentes.

📊 Consulta de Cards

Lista os cards existentes em uma lista específica.

🚀 Automação de Rotinas

Permite executar fluxos automatizados, como criação periódica de tarefas e
movimentação de cards de acordo com regras previamente definidas.

---

## 🏗️ Arquitetura

```text
┌─────────────────────────┐
│        Usuário          │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     Aplicação Python    │
│                         │
│ • Listar quadros        │
│ • Criar cards           │
│ • Mover cards           │
│ • Adicionar comentários │
│ • Consultar cards       │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       py-trello         │
│                         │
│ Camada de integração    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Trello API        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│         Trello          │
│                         │
│ Boards → Lists → Cards  │
└─────────────────────────┘
```

As credenciais utilizadas pela aplicação são carregadas por meio de variáveis
de ambiente, evitando sua inclusão diretamente no código-fonte.

---

## 🔄 Fluxo de Automação

Um fluxo típico pode ser representado por :

```text
Início
  ↓
Autenticação
  ↓
Selecionar Quadro
  ↓
Selecionar Lista
  ↓
Criar / Consultar Cards
  ↓
Aplicar Regras
  ↓
Mover / Atualizar Cards
  ↓
Finalizar Automação
```

---

## 🛠️ Tecnologias

**Python** - Desenvolvimento da automação

**Trello API** - Integração com o Trello 

**py-trello** - Comunicação com os recursos do Trello 

**python-dotenv** - Gerenciamento de variáveis de ambiente

**Git** - Versionamento 

**GitHub** - Repositório e documentação

---

## 🚀 Instalação

Pré-requisitos

- Python 3.7 ou superior
- Conta no Trello
- Credenciais para acesso à API
- Git

1. Clone o repositório

```bash
git clone https://github.com/MCLG1661/Quadro-Agente-DIO-Marcus-Guedes.git
```

Entre no diretório:

```bash
cd Quadro-Agente-DIO-Marcus-Guedes
```

2. Instale as dependências

```bash
pip install py-trello python-dotenv
```

---

## 🔐 Configuração das Credenciais

As credenciais **não devem ser inseridas diretamente no código**.

Crie um arquivo:

```text
.env
```

na raiz do projeto.

Adicione :

```env
TRELLO_API_KEY=sua_api_key_aqui
TRELLO_TOKEN=seu_token_aqui
```

Certifique-se de que `.env` esteja incluído no `.gitignore`.

> ⚠️ Nunca publique sua API Key ou Token no GitHub.

---

## ▶️ Executando

Execute :

```bash
python agente.py
```

A aplicação apresentará as operações disponíveis para gerenciamento do Trello.

---

## 📋 Menu Principal

```text
AGENTE TRELLO — AUTOMAÇÃO

1. 📋 Listar meus quadros
2. ➕ Criar novo card
3. 🔄 Mover card entre listas
4. 💬 Adicionar comentário
5. 📊 Listar cards de uma lista
```

---

## 🚀 Exemplo de Automação

Um fluxo automatizado pode:

1. Identificar um quadro
2. Selecionar listas de origem e destino
3. Criar uma nova tarefa
4. Consultar cards existentes
5. Aplicar uma regra de automação
6. Movimentar cards correspondentes

Exemplo conceitual :

```text
Quadro: Projeto Pessoal

To Do
  ↓
Nova tarefa criada
  ↓
Verificação dos cards
  ↓
Regra atendida?
  ↓
Sim
  ↓
Mover card
  ↓
Done
```

---

## 🎯 Exemplos de Automação Personalizada

Checklist automático

```python
card = lista.add_card(name="Revisão Diária")

card.add_checklist(
    "Tarefas do dia",
    [
        "Verificar emails",
        "Atualizar status do projeto",
        "Fazer commit do código"
    ]
)
```

Movimentação por Label

```python
for card in lista.list_cards():
    for label in card.labels:
        if label.name == "urgente":
            card.change_list(lista_destino.id)
```

---

## ⏰ Execução Programada

A aplicação também pode ser executada periodicamente utilizando recursos do
sistema operacional.

### Windows

Utilize o **Agendador de Tarefas** para executar o script Python no horário desejado.

Exemplo :

```text
C:\Python39\python.exe C:\projetos\agente_automatico.py
```

### Linux / macOS

Utilize `cron`.

Exemplo para execução diária às 9h:

```bash
0 9 * * * /usr/bin/python3 /home/usuario/agente_automatico.py
```

---

## 🛠️ Estrutura do Projeto

```text
Quadro-Agente-DIO-Marcus-Guedes/
│
├── agente.py
├── automacao_total.py
├── .gitignore
└── README.md
```

O arquivo `.env` deve existir apenas no ambiente local e **não deve ser
versionado no repositório**.

---

## 🔒 Segurança

O projeto utiliza variáveis de ambiente para separar credenciais do código.

Boas práticas :

- Nunca publique `.env`
- Nunca faça commit de API Keys
- Nunca publique Tokens
- Utilize `.gitignore`
- Revogue credenciais comprometidas
- Gere novas credenciais quando necessário

---

## 💡 Competências Demonstradas

- Python
- API Integration
- Workflow Automation
- Trello
- Gerenciamento de tarefas
- Manipulação de objetos
- Automação de processos
- Variáveis de ambiente
- Gerenciamento de credenciais
- Git e GitHub

---

## 🚀 Possíveis Evoluções

O projeto pode evoluir incorporando :

- Interface web
- FastAPI
- Webhooks
- Logs estruturados
- Tratamento avançado de erros
- Testes automatizados
- Docker
- Banco de dados
- Dashboard de automações
- Regras configuráveis
- Integração com outros serviços
- Notificações
- Inteligência Artificial

### 🤖 Evolução para um Agente de IA

Uma evolução particularmente interessante seria incorporar um LLM para interpretar
instruções em linguagem natural.

Por exemplo:

```text
"Crie um card para revisar o relatório amanhã e coloque como prioridade alta."
                         ↓
                       LLM
                         ↓
              Interpretação da intenção
                         ↓
                   Trello Tools
                         ↓
                    Trello API
                         ↓
                  Card criado
```

Nesse cenário, o projeto evoluiria de uma **automação programática** para um
**agente capaz de interpretar objetivos e executar ferramentas**.

---

## 🤝 Como Contribuir

Contribuições são bem-vindas.

1. Faça um Fork do projeto
2. Crie uma branch:

```bash
git checkout -b feature/nova-funcionalidade
```

3. Faça suas alterações
4. Faça o commit
5. Envie a branch
6. Abra um Pull Request

---

## 🎓 Contexto

Projeto desenvolvido como parte da jornada de aprendizado na **DIO**, aplicando
Python à automação de tarefas e integração com serviços externos.

---

## 👨‍💻 Autor

**Marcus Guedes**

Marketing | Data Science | Inteligência Artificial | Gestão de Projetos

GitHub: MCLG1661  

LinkedIn: Marcus Guedes

---

🤖 **Automatizando workflows e transformando tarefas repetitivas em processos programáveis.**
