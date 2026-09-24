# Declaração de Variáveis
a: int = 0
b: int = 0
c: int = 0
d: int = 0
valores = []


def ordenar():
    global a, b, c, d, valores

    valores = [a, b, c, d]
    valores.sort()

    print(valores)


def main():
    global a, b, c, d

    a = int(input("Insira o primeiro valor: "))
    b = int(input("Insira o segundo valor: "))
    c = int(input("Insira o terceiro valor: "))
    d = int(input("Insira o quarto valor: "))

    ordenar()


if __name__ == '__main__':
    main()