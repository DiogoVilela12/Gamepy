from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Escolha a dificuldade \nFacil [ 1, 2, 3, 4, 5 ] Dificil \n'))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para seguinte operação:')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pnts')

    continuar: int = int(input('Você quer continuar jogando ? 1- Sim  2-Não'))

    if continuar == 1:
        jogar(pontos)
    elif continuar == 2:
        print(f'Você finalizou com {pontos} ponto(s)')
        print(f'Até a proxima')
    else:
        continuar = int(input('Resposta invalida digite novamente: \nContinuar jogando ? 1- Sim  2-Não'))


if __name__ == '__main__':
    main()


