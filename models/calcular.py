from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 4)  # 1 Soma, 2 Subtração, 3 Multiplicação, 4 Divisão
        self.__resultado: float = self.gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2
    
    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao:
            op = 'Subtração'
        elif self.operacao == 3:
            op = 'Multiplicação'
        elif self.operacao == 4:
            op = 'Divisão'
        else:
            print('Operação desconhecida')
            exit(1)
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        elif self.dificuldade == 5:
            return randint(0, 100000)
        else:
            print('Dificuldade não selecionada... \nMODO HARDCORE LIGADO')
            return randint(0, 999999)


    @property
    def gerar_resultado(self: object) -> int:
        if self.operacao == 1: # Soma
            return self.valor1 + self.valor2
        elif self.operacao == 2: # Subtração
            return self.valor1 - self.valor2
        elif self.operacao == 3: # Multiplicação
            return self.valor1 * self.valor2
        else:
            return self.valor1 // self.valor2


    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:  # Soma
            return '+'
        elif self.operacao == 2:  # Subtração
            return '-'
        elif self.operacao == 3:  # Multiplicação
            return 'x'
        else:
            return '/'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta Incorreta!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
