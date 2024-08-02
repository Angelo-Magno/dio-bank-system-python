class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = {}

    def listar_contas(self):
        for conta in self.contas.values():
            print(f'Agencia: {conta.agencia} | Número da conta: {conta.numero} | Tipo: {conta.__class__.__name__}')

    def executar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco=endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def listar_contas(self):
        print(f'\nContas vinculadas ao cliente {self.nome}:')
        super().listar_contas()


class PessoaJuridica(Cliente):
    def __init__(self, cnpj, razao_social, endereco):
        super().__init__(endereco=endereco)
        self.cnpj = cnpj
        self.razao_social = razao_social
    
    def listar_contas(self):
        print(f'\nContas vinculadas a empresa: {self.razao_social}')
        super().listar_contas()
