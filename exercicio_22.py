# Declaração de Variáveis
a: int = 0
b: int = 0
maior: int = 0
menor: int = 0


def menor_maior():
    global a, b, maior, menor

    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    print(menor, maior)


def main():
    global a, b

    a = int(input("Insira o primeiro valor: "))
    b = int(input("Insira o segundo valor: "))

    menor_maior()


if __name__ == '__main__':
    main()