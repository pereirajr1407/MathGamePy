from models.calcular import Calcular

def main() -> None:
	pontos: int = 0
	jogar(pontos)

def jogar(pontos) -> None:
	dificuldade: int = int(input('Informe o nivel de dificuldade desejado (1, 2, 3 ou 4): '))

	calc: Calcular = Calcular(dificuldade)

	print('Informe o resultado para a seguinte operaçao: ')

	calc.mostrar_operacao()

	resultado: int = int(input())

	if calc.checar_resultado(resultado):
		pontos += 1
		print(f'Voce tem {pontos} ponto(s).')

	continuar: int = int(input('Deseja continuar no jogo? (1 - Sim, 0 - Nao): '))

	if continuar:
		jogar(pontos)
	else:
		print(f'Voce finalizou com {pontos} ponto(s).')
		print('Ate a proxima')

if __name__ == '__main__':
	main()