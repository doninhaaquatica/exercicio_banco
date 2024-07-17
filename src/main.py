import utils
import os


def main():
    """main function"""
    saldo: float = 0.00
    saques = 3
    ação = 0
    extrato_list: list[dict] = []
    menu_list = [
        "deposito",
        "sacar",
        "extrato",
    ]
    while True:
        os.system("cls")
        # print(f"Saldo: ${saldo}")
        escolha = utils.menu(menu_list)
        if escolha == "deposito":
            while True:
                try:
                    valor_depositar = float(
                        input("Entre com o valor a ser depositado: ")
                    )
                    if valor_depositar > 0:
                        saldo += valor_depositar
                        extrato_list.append({escolha: valor_depositar})
                        break
                except ValueError:
                    pass
                print("valor invalido!!Tente novamente")

        if escolha == "sacar":
            while True:
                try:
                    valor_sacado = float(input("Entre com o valor a ser sacado: "))
                    if valor_sacado <= 500:
                        if saldo > valor_sacado:
                            if saques > 0:
                                saldo -= valor_sacado
                                extrato_list.append({escolha: valor_sacado})

                            else:
                                print("Valor limite se saldos no dia atingido")
                                input()

                        else:
                            print("Não há saldo suficiente!!")
                            input()

                    else:
                        print("Valor maximo permitido de saque é $500.00 !!!")
                        input()
                    break

                except ValueError:
                    print("Valor inserido invalido !!!!")

        if escolha == "extrato":
            print("=" * 10, "EXTRATO", "=" * 10)
            for dado in extrato_list:
                for chave, valor in dado.items():
                    print(f"{str(chave).capitalize()}: ${valor}")
            print("=" * 27)
            print(f"Saldo: {saldo}")
            print("=" * 27)

            input()


if __name__ == "__main__":
    main()
