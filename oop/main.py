import textwrap
from cliente import PessoaFisica, PessoaJuridica
from conta import ContaCorrente, ContaPoupanca
from banco import Banco
from os import system


def depositar(saldo, valor, extrato, /):  # Positional only
    pass


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # keyword only
    pass


def exibir_extrato(saldo, /, *, extrato):  # positional only | keyword only
    pass


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
    print('\nConta criada com Sucesso!')


def buscar_cliente(cpf_cnpj, banco):
    if banco.clientes_pf.get(cpf_cnpj, None) is None:
        cliente = banco.clientes_pj.get(cpf_cnpj, None)
        if cliente is None:
            print('\nCliente não possui cadastro!')
            espera()
        return cliente
    
    return banco.clientes_pf[cpf_cnpj]


def menus(tipo):

    match tipo:
        case 'menu pricipal':
            MENU = '''
                ========= MENU ==========
                    [1] Criar Usuário
                    [2] Criar Conta
                    [3] Listar Usúarios
                    [4] Acessar Conta
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
                    [5] Listar Contas
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
    contas_contador = 0

    while True:
        system('cls')
        opcao_menu_principal = int(input(menus('menu pricipal')))

        match opcao_menu_principal:
            case 1: # Criar usuário
                while True:
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
                cpf_cnpj = input('Informe o cpf ou cpnj: ')
                cliente = buscar_cliente(cpf_cnpj, banco)

                while cliente:
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
                banco.listar_clientes()
                espera()
            case 4:
                cpf_cnpj = input('Informe o cpf ou cpnj: ')
                cliente = buscar_cliente(cpf_cnpj, banco)

                while cliente:
                    opcao_acesso = int(input(menus('acessar conta')))
                    match opcao_acesso:
                        case 1:
                            break
                        case 2:
                            break
                        case 3:
                            break
                        case 4:
                            break
                        case 5:
                            cliente.listar_contas()
                            espera()
                            break
                        case 0:
                            break
                        case _:
                            pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 0:
                break


if __name__ == '__main__':
    main()
