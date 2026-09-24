# Declaração de Variáveis
a: float = 0
b: float = 0
c: float = 0
delta: float = 0
x1: float = 0
x2: float = 0


def bhaskara():
    global a, b, c, delta, x1, x2

    delta = b * b - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais")
    elif delta == 0:
        x1 = -b / (2 * a)
        print("Existe uma raiz real:", x1)
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print("Existem duas raízes reais:", x1, x2)


def main():
    global a, b, c

    a = float(input("Insira A: "))
    b = float(input("Insira B: "))
    c = float(input("Insira C: "))

    bhaskara()


if __name__ == '__main__':
    main()