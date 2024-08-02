import textwrap
from banco import Banco
from cliente import PessoaFisica, PessoaJuridica
from conta import ContaCorrente, ContaPoupanca
from transacao import Deposito, Saque
from os import system


def depositar(cliente, conta):
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    cliente.executar_transacao(conta, transacao)


def sacar(cliente, conta):
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    cliente.executar_transacao(conta, transacao)


def exibir_extrato(conta):  # positional only | keyword only
    print("\n================ EXTRATO ================")
    extrato = ''
    historico = conta.historico

    if not historico.transacoes:
        extrato = "Não foram realizadas movimentações."

    for data, transacoes in historico.transacoes.items():
        extrato = f'\nData: {data}\n'
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: R$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_usuario(opcao, banco):
    if opcao == 1:
        cpf = input("Informe o CPF (somente números): ")

        if banco.clientes_pf.get(cpf):
            print(f"\nUsuário com CPF: {cpf} já possui cadastro!")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuario = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
        banco.adicionar_cliente(usuario)

    elif opcao == 2:
        cnpj = input("Informe o CNPJ (somente números): ")

        if banco.clientes_pj.get(cnpj):
            print(f"\nUsuário com CNPJ: {cnpj} já possui cadastro!")
            return
        
        razao_social = input("Informe a razão social: ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuario = PessoaJuridica(cnpj=cnpj, razao_social=razao_social, endereco=endereco)
        banco.adicionar_cliente(usuario)


def criar_conta(opcao, cliente, numero_conta):
    if opcao == 1:
        conta = ContaCorrente(numero_conta)
    elif opcao == 2:
        conta = ContaPoupanca(numero_conta)
    
    cliente.contas[numero_conta] = conta
    print(f'\nConta de número: {numero_conta} criada com Sucesso!')
    print('Lembre-se de guardar o número da sua conta!')


def buscar_cliente(cpf_cnpj, banco):
    if banco.clientes_pf.get(cpf_cnpj, None) is None:
        cliente = banco.clientes_pj.get(cpf_cnpj, None)
        if cliente is None:
            print('\nCliente não possui cadastro!')
            espera()
            return None
        
        return cliente
    
    return banco.clientes_pf[cpf_cnpj]


def buscar_conta(cliente, numero_conta):
    conta = cliente.contas.get(numero_conta, None)
    if conta is None:
        print('\nConta não encontrada!')
        espera()
        return None
    
    return conta


def menus(tipo):

    match tipo:
        case 'menu pricipal':
            MENU = '''
                ========= MENU ==========
                    [1] Criar Usuário
                    [2] Criar Conta
                    [3] Listar Usúarios
                    [4] Listar Contas
                    [5] Acessar Conta
                    [0] Sair
                Digite uma opção: '''
            return textwrap.dedent(MENU)
        
        case 'acessar conta':
            MENU = '''
                ========= MENU ==========
                    [1] Depositar
                    [2] Sacar
                    [3] Tranferir
                    [4] Exibir Extrato
                    [0] Sair
                Digite uma opção: '''
            return textwrap.dedent(MENU)

        case 'criar usuario':
            MENU = '''
                    ========= MENU ==========
                        [1] Pessoa Física
                        [2] Pessoa Jurídica
                        [0] Voltar
                    Digite uma opção: '''
            return textwrap.dedent(MENU)
        
        case 'criar conta':
            MENU = '''
                    ========= MENU ==========
                        [1] Criar Conta Corrente
                        [2] Criar Conta Poupança
                        [0] Voltar
                    Digite uma opção: '''
            return textwrap.dedent(MENU)

def espera():
    while True:
        op = input('\nPressione ENTER para voltar ao menu!').strip()
        if op == '':
            break



def main():
    banco = Banco("Bank of America")
    contas_contador = 1

    while True:
        system('cls')
        opcao_menu_principal = int(input(menus('menu pricipal')))

        match opcao_menu_principal:
            case 1: # Criar usuário
                while True:
                    system('cls')
                    opcao_criar_usuario = int(input(menus('criar usuario')))
                    match opcao_criar_usuario:
                        case 1 | 2:
                            criar_usuario(opcao_criar_usuario, banco)
                            espera()
                            break
                        case 0:
                            break
                        case _:
                            pass
                
            case 2: # Criar Conta
                system('cls')
                cpf_cnpj = input('Informe o cpf ou cpnj: ')
                cliente = buscar_cliente(cpf_cnpj, banco)

                while cliente:
                    system('cls')
                    opcao_criar_conta = int(input(menus('criar conta')))
                    match opcao_criar_conta:
                        case 1 | 2:
                            criar_conta(opcao_criar_conta, cliente, contas_contador)
                            contas_contador += 1
                            espera()
                            break
                        case 0:
                            break
                        case _:
                            pass

            case 3: # Listar usuários
                system('cls')
                banco.listar_clientes()
                espera()

            case 4: # Listar conta
                system('cls')
                cpf_cnpj = input('Informe o cpf ou cpnj: ')
                cliente = buscar_cliente(cpf_cnpj, banco)
                if cliente:
                    cliente.listar_contas()
                    espera()
                    
            case 5: # Acessar conta
                system('cls')
                cpf_cnpj = input('Informe o cpf ou cpnj: ')
                cliente = buscar_cliente(cpf_cnpj, banco)
                if cliente is None:
                    continue

                numero_conta = int(input('Informe o número da conta: '))
                conta = buscar_conta(cliente, numero_conta)
                
                while conta:
                    system('cls')
                    opcao_acesso = int(input(menus('acessar conta')))
                    match opcao_acesso:
                        case 1:
                            depositar(cliente, conta)
                            espera()
                        case 2:
                            sacar(cliente, conta)
                            espera()
                        case 3:
                            pass
                        case 4:
                            exibir_extrato(conta)
                            espera()
                        case 0:
                            break
                        case _:
                            pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 0:
                break


if __name__ == '__main__':
    main()
