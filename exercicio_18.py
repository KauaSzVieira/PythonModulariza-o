# Declaração de Variáveis
valor1: int = 0
valor2: int = 0
diferenca: int = 0


def diferenca_valores():
    global valor1, valor2, diferenca

    if valor1 > valor2:
        diferenca = valor1 - valor2
    else:
        diferenca = valor2 - valor1

    print(diferenca)


def main():
    global valor1, valor2

    valor1 = int(input("Insira o primeiro valor: "))
    valor2 = int(input("Insira o segundo valor: "))

    diferenca_valores()


if __name__ == '__main__':
    main()