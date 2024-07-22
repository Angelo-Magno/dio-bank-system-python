import textwrap
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco=endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class PessoaJuridica(Cliente):
    def __init__(self, cnpj, razao_social, endereco):
        super().__init__(endereco=endereco)
        self.cnpj = cnpj
        self.razao_social = razao_social


class Conta:
    def __init__(self, numero):
        self._numero = numero
        self._agencia = '0382'
        self._saldo = 0


class ContaCorrente(Conta):
    def __init__(self, numero):
        super().__init__(numero=numero)


class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero=numero)


class Historico:
    def __init__(self):
        self._transacoes = []


class Transacao(ABC):  # interface
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        pass

    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        pass

    def registrar(self, conta):
        pass


class Tranferencia(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        pass

    def registrar(self, conta):
        pass


def depositar(saldo, valor, extrato, /):  # Positional only
    pass


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # keyword only
    pass


def exibir_extrato(saldo, /, *, extrato):  # positional only | keyword only
    pass


def criar_usuario():
    pass


def criar_conta():
    pass

def main():
    MENU = '''
        ========= MENU ==========
            [1] Depositar
            [2] Sacar
            [3] Exibir Extrato
            [4] Criar Usuário
            [5] Criar Conta
            [6] Listar Usúarios
            [7] Listar Contas
            [0] Sair
        Digite uma opção: '''

    clientes = {}
    contas_contador = 0

    while True:
        opcao = int(input(textwrap.dedent(MENU)))
        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
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
