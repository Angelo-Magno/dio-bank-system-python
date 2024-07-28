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
