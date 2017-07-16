from Funcionario import Funcionario
from Produto import Produto

class Vendedor(Funcionario):
    def __init__(self, nome, idade, genero, salario, matricula, valorVendas):
        super(Vendedor, self).__init__(nome, idade, genero, salario, matricula)
        self.valorVendas = valorVendas
        self.vendas = []


    def vender(self, nomeProd, valorProd, numProd):
        for i in range(numProd):
            p = Produto(nomeProd, valorProd)
            self.vendas.append(p)