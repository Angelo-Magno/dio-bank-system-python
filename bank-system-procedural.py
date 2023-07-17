cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         }

menu = """
========== MENU ==========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

==========================
> """

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    match opcao:
        case 1:  # Depositar
            valor = float(input("Informe o valor do depósito R$: "))

            if valor > 0:
                saldo += valor
                extrato += f"\t{cores['verde']}+ R$ {valor:.2f}{cores['limpar']}\n"
                print(f"{cores['verde']}Operação realizada com sucesso!{cores['limpar']}\n"
                      f'Seu saldo atual é de R$: {saldo:.2f}')

            else:
                print(f"{cores['vermelho']}Operação falhou! O valor informado é inválido.")

        case 2:  # Sacar
            valor = float(input("Informe o valor a sacar R$: "))

            if valor > 0:

                if valor > limite_valor_saque:
                    print(f"{cores['vermelho']}Operação inválida! "
                          f"O valor do saque excede o seu limite.{cores['limpar']}")

                elif valor > saldo:
                    print(f"{cores['vermelho']}Operação inválida! Saldo insuficiente.{cores['limpar']}\n"
                          f"Saldo atual R$: {saldo:.2f}")

                elif numero_saques >= LIMITE_SAQUES:
                    print(f"{cores['vermelho']}Operação inválida! "
                          f"Você atingiu seu limite máximo de saques.{cores['limpar']}")

                else:
                    saldo -= valor
                    extrato += f"\t{cores['vermelho']}- R$ {valor:.2f}{cores['limpar']}\n"
                    numero_saques += 1
                    print(f"{cores['verde']}Operação realizada com sucesso!{cores['limpar']}\n"
                          f'Seu saldo atual é de R$: {saldo:.2f}')

            else:
                print(f"{cores['vermelho']}Valor inválido!{cores['limpar']}")

        case 3:  # Exibir extrato
            print("\n" + "=" * 12 + " EXTRATO " + "=" * 12)
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo Total: R$ {saldo:.2f}")
            print("="*33)
            while True:
                op = input('\nPressione ENTER para voltar ao menu!').strip()
                if op == '':
                    break

        case 4:  # Sair do sistema
            break

        case _:
            print(f"{cores['vermelho']}Opção inválida! Informe uma opção de 1 a 4!{cores['limpar']}")