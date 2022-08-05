from models.calculate import Calculate

def main() -> None:
	points: int = 0
	play(points)

def play(points) -> None:
	difficulty: int = int(input('Choose the desired difficulty level (1, 2, 3 or 4): '))

	calc: Calculate = Calculate(difficulty)

	print('Solve the following challenge: ')

	calc.show_operation()

	result: int = int(input())

	if calc.check_result(result):
		points += 1
		print(f'You have {points} point(s).')

	continue_game: int = int(input('Do you want to keep playing? (1 - Yes, 0 - No): '))

	if continue_game:
		play(points)
	else:
		print(f'You got {points} point(s).')
		print('See you next time!')

if __name__ == '__main__':
	main()