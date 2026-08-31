import os
from datetime import datetime

from dotenv import load_dotenv
from trello import TrelloClient


# ============================================================
# CONFIGURAÇÃO
# ============================================================

load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")

QUADRO_NOME = "Meu Projeto"
LISTA_ORIGEM = "To Do"
LISTA_DESTINO = "Done"
NOME_CARD = "Tarefa Automática"


# ============================================================
# UTILITÁRIOS
# ============================================================

def validar_credenciais():
    """
    Verifica se as credenciais necessárias foram carregadas.
    """
    if not TRELLO_API_KEY or not TRELLO_TOKEN:
        print(
            "❌ Credenciais do Trello não encontradas.\n"
            "Verifique se TRELLO_API_KEY e TRELLO_TOKEN "
            "estão configurados no arquivo .env."
        )
        return False

    return True


def conectar_trello():
    """
    Cria e retorna o cliente da API do Trello.
    """
    return TrelloClient(
        api_key=TRELLO_API_KEY,
        token=TRELLO_TOKEN
    )


def encontrar_quadro(client, nome_quadro):
    """
    Procura um quadro pelo nome.
    """
    for board in client.list_boards():
        if nome_quadro.lower() in board.name.lower():
            return board

    return None


def encontrar_lista(board, nome_lista):
    """
    Procura uma lista dentro do quadro pelo nome.
    """
    for lista in board.list_lists():
        if nome_lista.lower() in lista.name.lower():
            return lista

    return None


# ============================================================
# AUTOMAÇÃO
# ============================================================

def criar_card_diario(lista):
    """
    Cria o card automático referente ao dia atual.
    """
    hoje = datetime.now().strftime("%Y-%m-%d")
    horario = datetime.now().strftime("%H:%M:%S")

    nome_card = f"{NOME_CARD} - {hoje}"

    card = lista.add_card(
        name=nome_card,
        desc=f"Criado automaticamente em {horario}"
    )

    print(f"✅ Card criado: {card.name}")

    return card


def mover_cards_automaticos(
    lista_origem,
    lista_destino,
    card_atual
):
    """
    Move cards automáticos anteriores para a lista de destino.

    A regra atual é demonstrativa:
    qualquer card com o texto definido em NOME_CARD,
    diferente do card criado na execução atual, é movido.
    """
    cards_movidos = 0

    for card in lista_origem.list_cards():

        if (
            NOME_CARD.lower() in card.name.lower()
            and card.id != card_atual.id
        ):
            card.change_list(lista_destino.id)

            print(
                f"✅ Card movido para "
                f"'{lista_destino.name}': {card.name}"
            )

            cards_movidos += 1

    return cards_movidos


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def main():

    print("=" * 55)
    print("🤖 TRELLO WORKFLOW AUTOMATION")
    print("=" * 55)

    # --------------------------------------------------------
    # 1. CREDENCIAIS
    # --------------------------------------------------------

    if not validar_credenciais():
        return

    # --------------------------------------------------------
    # 2. CONEXÃO
    # --------------------------------------------------------

    try:
        client = conectar_trello()
        print("✅ Cliente Trello configurado")
    except Exception as error:
        print(f"❌ Erro ao configurar cliente: {error}")
        return

    # --------------------------------------------------------
    # 3. QUADRO
    # --------------------------------------------------------

    try:
        quadro = encontrar_quadro(
            client,
            QUADRO_NOME
        )
    except Exception as error:
        print(
            f"❌ Erro ao consultar quadros: {error}"
        )
        return

    if not quadro:
        print(
            f"❌ Quadro '{QUADRO_NOME}' "
            "não encontrado."
        )
        return

    print(f"✅ Quadro encontrado: {quadro.name}")

    # --------------------------------------------------------
    # 4. LISTAS
    # --------------------------------------------------------

    lista_origem = encontrar_lista(
        quadro,
        LISTA_ORIGEM
    )

    lista_destino = encontrar_lista(
        quadro,
        LISTA_DESTINO
    )

    if not lista_origem:
        print(
            f"❌ Lista de origem "
            f"'{LISTA_ORIGEM}' não encontrada."
        )
        return

    if not lista_destino:
        print(
            f"❌ Lista de destino "
            f"'{LISTA_DESTINO}' não encontrada."
        )
        return

    print(
        f"✅ Lista origem: "
        f"{lista_origem.name}"
    )

    print(
        f"✅ Lista destino: "
        f"{lista_destino.name}"
    )

    # --------------------------------------------------------
    # 5. CRIAR CARD
    # --------------------------------------------------------

    try:
        card_atual = criar_card_diario(
            lista_origem
        )
    except Exception as error:
        print(
            f"❌ Erro ao criar card: {error}"
        )
        return

    # --------------------------------------------------------
    # 6. MOVER CARDS
    # --------------------------------------------------------

    try:
        cards_movidos = mover_cards_automaticos(
            lista_origem,
            lista_destino,
            card_atual
        )
    except Exception as error:
        print(
            f"❌ Erro ao mover cards: {error}"
        )
        return

    # --------------------------------------------------------
    # 7. RESUMO
    # --------------------------------------------------------

    print("\n" + "=" * 55)
    print("🎉 AUTOMAÇÃO CONCLUÍDA")
    print("=" * 55)

    print(f"Card criado: {card_atual.name}")
    print(f"Cards movidos: {cards_movidos}")


if __name__ == "__main__":
    main()
