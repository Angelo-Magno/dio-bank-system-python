import textwrap

cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         }


def menu():
    menu = """
    =============== MENU ===============
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova usuário
        [5] Nova conta
        [6] Listar contas
        [0] Sair
    > """
    return int(input(textwrap.dedent(menu)))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\t{cores['verde']}+ R$ {valor:.2f}{cores['limpar']}\n"
        print(f"{cores['verde']}Operação realizada com sucesso!{cores['limpar']}\n"
              f'Seu saldo atual é de R$: {saldo:.2f}')
    else:
        print(f"{cores['vermelho']}Operação falhou! O valor informado é inválido.{cores['limpar']}")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite_valor_saque, numero_saques, limite_saques):

    if valor > 0:

        if valor > limite_valor_saque:
            print(f"{cores['vermelho']}Operação inválida! "
                  f"O valor do saque excede o seu limite.{cores['limpar']}")

        elif valor > saldo:
            print(f"{cores['vermelho']}Operação inválida! Saldo insuficiente.{cores['limpar']}\n"
                  f"Saldo atual R$: {saldo:.2f}")

        elif numero_saques >= limite_saques:
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

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n" + " EXTRATO ".center(33, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo Total: R$ {saldo:.2f}")
    print("=" * 33)
    while True:
        op = input('\nPressione ENTER para voltar ao menu!').strip()
        if op == '':
            break


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    try:
        if usuarios[cpf]:
            print(f"\n{cores['vermelho']}Usuário com CPF: {cpf} já possui cadastro!{cores['limpar']}")

    except KeyError:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
        print(f"\n{cores['verde']}Usuário criado com sucesso!{cores['limpar']}")


def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    try:
        usuario = usuarios[cpf]
        numero_conta = len(contas) + 1
        contas[numero_conta] = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print(f"\n{cores['verde']}Conta criada com sucesso!{cores['limpar']}")

    except KeyError:
        print(f"\n{cores['vermelho']}Usuário não encontrado!\n"
              f"É preciso ser cadastrado para criar uma nova conta!{cores['limpar']}")


def listar_contas(contas):
    if len(contas) == 0:
        print(f"\n{cores['vermelho']}Não há contas cadastradas!{cores['limpar']}")
    else:
        for conta in contas.values():
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 50)
            print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = {}
    contas = {}

    while True:
        opcao = menu()

        match opcao:

            case 1:  # Depositar
                valor = float(input("Informe o valor do depósito: "))

                saldo, extrato = depositar(saldo, valor, extrato)

            case 2:  # Sacar
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite_valor_saque=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )

            case 3:  # Extrato
                exibir_extrato(saldo, extrato=extrato)

            case 4:  # Usuario
                criar_usuario(usuarios)

            case 5:  # Conta
                criar_conta(AGENCIA, contas, usuarios)

            case 6:  # Listar
                listar_contas(contas)

            case 0:  # Sair
                break

            case _:
                print(f"{cores['vermelho']}Opção inválida! Informe uma opção de 0 a 6!{cores['limpar']}")


main()
