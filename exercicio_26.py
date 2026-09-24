# Declaração de Variáveis
a: int = 0
b: int = 0
maior: int = 0
menor: int = 0


def verificar_multiplo():
    global a, b, maior, menor

    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    if maior % menor == 0:
        print("O maior é múltiplo do menor")
    else:
        print("O maior não é múltiplo do menor")


def main():
    global a, b

    a = int(input("Insira o primeiro valor: "))
    b = int(input("Insira o segundo valor: "))

    verificar_multiplo()


if __name__ == '__main__':
    main()