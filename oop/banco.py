class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes_pf = {}
        self.clientes_pj = {}

    def adicionar_cliente(self, cliente):
        if hasattr(cliente, 'cpf'):
            self.clientes_pf[cliente.cpf] = cliente
            print(f'Cliente {cliente.nome} adicionado ao banco {self.nome}.')
            return
      
        self.clientes_pj[cliente.cnpj] = cliente
        print(f'Cliente {cliente.razao_social} adicionado ao banco {self.nome}.')

        
    def listar_clientes(self):
        print('\n======== Clientes Pessoa Física ========')
        for cliente in self.clientes_pf.values():
            print(f'Cliente: {cliente.nome}, CPF: {cliente.cpf}')
        
        print('\n======== Clientes Pessoa Jurídica ========')
        for cliente in self.clientes_pj.values():
            print(f'Cliente: {cliente.razao_social}, CNPJ: {cliente.cnpj}')
    
