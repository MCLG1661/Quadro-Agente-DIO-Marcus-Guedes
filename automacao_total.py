import os
import time
from datetime import datetime
from dotenv import load_dotenv
from trello import TrelloClient

load_dotenv()

# Configurações fixas (edite aqui!)
QUADRO_NOME = "Meu Projeto"      # Nome do seu quadro
LISTA_ORIGEM = "To Do"            # Lista onde criar cards
LISTA_DESTINO = "Done"            # Lista para mover cards
NOME_CARD = "Tarefa Automática"   # Nome base do card

def main():
    # Conecta ao Trello
    client = TrelloClient(
        api_key=os.getenv('TRELLO_API_KEY'),
        token=os.getenv('TRELLO_TOKEN')
    )
    
    # Encontra o quadro
    quadro = None
    for b in client.list_boards():
        if QUADRO_NOME.lower() in b.name.lower():
            quadro = b
            break
    
    if not quadro:
        print(f"❌ Quadro '{QUADRO_NOME}' não encontrado!")
        return
    
    # Encontra as listas
    lista_criar = None
    lista_mover = None
    
    for lst in quadro.list_lists():
        if LISTA_ORIGEM.lower() in lst.name.lower():
            lista_criar = lst
        if LISTA_DESTINO.lower() in lst.name.lower():
            lista_mover = lst
    
    # Cria card do dia
    hoje = datetime.now().strftime("%Y-%m-%d")
    card = lista_criar.add_card(
        name=f"{NOME_CARD} - {hoje}",
        desc=f"Criado automaticamente em {datetime.now().strftime('%H:%M:%S')}"
    )
    print(f"✅ Card criado: {card.name}")
    
    # Move cards antigos (mais de 2 dias)
    for card in lista_criar.list_cards():
        if "Automática" in card.name and card.name != f"{NOME_CARD} - {hoje}":
            card.change_list(lista_mover.id)
            print(f"✅ Card movido: {card.name}")
    
    print("🎉 Automação concluída!")

if __name__ == "__main__":
    main()