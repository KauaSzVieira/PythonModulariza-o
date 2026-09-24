# Declaração de Variáveis
numero: int = 0


def verificar():
    global numero

    if numero % 2 == 0 and numero % 3 == 0:
        print("É divisível por 2 e 3")
    elif numero % 2 == 0 and numero % 3 != 0:
        print("É divisível por 2 e não é divisível por 3")
    elif numero % 2 != 0 and numero % 3 == 0:
        print("Não é divisível por 2 e é divisível por 3")
    else:
        print("Não é divisível por 2 e 3")


def main():
    global numero

    numero = int(input("Insira um valor inteiro: "))

    verificar()


if __name__ == '__main__':
    main()
