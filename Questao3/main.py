from Fornecedor import Fornecedor
from Funcionario import Funcionario

def main():
    f = Fornecedor("marcos", "asd", 645, 100, 55)
    print(f.obterSaldo())

    f2 = Funcionario("marcos", "asd", 645, 5, 100, 10)
    print(f2.calcularSalarioTotal())
if __name__ == "__main__":
    main()