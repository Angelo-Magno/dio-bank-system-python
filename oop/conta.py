from datetime import datetime
from historico import Historico

class Conta:
    def __init__(self, numero):
        self._numero = numero
        self._agencia = '0048'
        self._saldo = 0
        self._historico = Historico()

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if valor < 0:
            print("\n### Operação falhou! Valor inválido! ###")
            return False
        
        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True
    
    def sacar(self, valor):
        if self.saldo < valor:
            print("\n### Operação falhou! Você não tem saldo suficiente. ###")
            return False

        if valor < 0:
            print("\n### Operação falhou! O valor informado é inválido. ###")
            return False
       
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, limite_saques=3, limite_valor=500):
        super().__init__(numero=numero)
        self._limite_saques =  limite_saques
        self._limite_valor = limite_valor

    def sacar(self, valor):
        saques_dia = self._historico.transacoes[datetime.now().strftime("%d-%m-%Y")]
        if len(saques_dia) >= self._limite_saques:
            print('Você atingiu o limite de saques diário!')
            return False
        
        if valor > self._limite_valor:
            print(f'Valor excede o seu limite de R$: {self._limite_valor} !')
            return False
        
        return super().sacar(valor)


class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero=numero)
