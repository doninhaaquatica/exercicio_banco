def menu(dados: list) -> str:
    """Menu
    ==========================================================
    Recebe uma lista de dados que deve ser tranformado em um menu.
        Exemplo:\n
        ``dados = ["exemplo1","exemplo2","exemplo3"]``\n
        print:\n
        1 - ``exenplo1``\n
        2 - ``exemplo2``\n
        3 - ``exemplo3``\n
        Escolha uma das opções:\n

        Args:
            dados (list): Lista que ira virar um menu

        Returns:
            str: valor que foi escolido.
    """
    while True:
        for index, name in enumerate(dados):
            print(f"{index+1} - {name}")
        try:
            escolha = int(input("Escolha uma das opções: "))
            if escolha in list(range(1, len(dados) + 1)):
                return dados[escolha - 1]
        except ValueError:
            print("Informação incorreta!!!")
