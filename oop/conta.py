class Conta:
    def __init__(self, numero):
        self._numero = numero
        self._agencia = '0048'
        self._saldo = 0

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo


class ContaCorrente(Conta):
    def __init__(self, numero):
        super().__init__(numero=numero)


class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero=numero)
