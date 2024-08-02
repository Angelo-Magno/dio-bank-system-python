from abc import ABC, abstractmethod


class Transacao(ABC):  # interface
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        operacao_efetuada = conta.sacar(self._valor)
        
        if operacao_efetuada:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        operacao_efetuada = conta.depositar(self._valor)
        
        if operacao_efetuada:
            conta.historico.adicionar_transacao(self)



class Tranferencia(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        pass
