from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, genero, salario, matricula):
        super(Funcionario, self).__init__(nome, idade, genero)
        self.salario = salario
        self.matricula = matricula

    def calcularINSS(self):
        pagarINSS = 11 / 100 * self.salario
        return pagarINSS