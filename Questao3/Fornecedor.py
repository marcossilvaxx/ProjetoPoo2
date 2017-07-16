from Pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome, endereço, telefone, valorCredito, valorDivida):
        super(Fornecedor, self).__init__(nome, endereço, telefone)
        self.valorCredito = valorCredito
        self.valorDivida = valorDivida

    def obterSaldo(self):
        resultado = self.valorCredito - self.valorDivida
        return resultado