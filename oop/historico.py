from datetime import datetime
from collections import defaultdict


class Historico:
    def __init__(self):
        self._transacoes = defaultdict(list)

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes[datetime.now().strftime("%d-%m-%Y")].append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
 