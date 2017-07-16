class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return "[Produto: %s; Valor: %.2f]" % (self.nome, self.valor)