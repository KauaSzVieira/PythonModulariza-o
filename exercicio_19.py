# Declaração de Variáveis
valor1: float = 0
valor2: float = 0
maior: float = 0


def maior_valor():
    global valor1, valor2, maior

    if valor1 > valor2:
        maior = valor1
    else:
        maior = valor2

    print(maior)


def main():
    global valor1, valor2

    valor1 = float(input("Insira o primeiro valor: "))
    valor2 = float(input("Insira o segundo valor: "))

    maior_valor()


if __name__ == '__main__':
    main()