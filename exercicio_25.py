# Declaração de Variáveis
hora_inicio: int = 0
minuto_inicio: int = 0
hora_final: int = 0
minuto_final: int = 0
inicio: int = 0
final: int = 0
duracao: int = 0
horas: int = 0
minutos: int = 0


def calcular_duracao():
    global hora_inicio, minuto_inicio, hora_final, minuto_final
    global inicio, final, duracao, horas, minutos

    inicio = hora_inicio * 60 + minuto_inicio
    final = hora_final * 60 + minuto_final

    if final <= inicio:
        final = final + 24 * 60

    duracao = final - inicio
    horas = duracao // 60
    minutos = duracao % 60

    print(horas, "hora(s) e", minutos, "minuto(s)")


def main():
    global hora_inicio, minuto_inicio, hora_final, minuto_final

    hora_inicio = int(input("Insira a hora de início: "))
    minuto_inicio = int(input("Insira os minutos de início: "))
    hora_final = int(input("Insira a hora final: "))
    minuto_final = int(input("Insira os minutos finais: "))

    calcular_duracao()


if __name__ == '__main__':
    main()