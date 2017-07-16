from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, endereço, telefone, codigoSetor, salarioBase, imposto):
        super(Funcionario, self).__init__(nome, endereço, telefone)
        self.codigoSetor = codigoSetor
        self.salarioBase = salarioBase
        self.imposto = imposto
    def calcularSalarioTotal(self):
        resultado = self.salarioBase - (self.imposto / 100 * self.salarioBase)
        return resultado
