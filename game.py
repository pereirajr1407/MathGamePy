from models.calculate import Calculate

def main():
	points = 0
	set_difficulty(points)

def set_difficulty(points):
	difficulty = str(input('Choose the difficulty level:\n\nKid Play\nEasy\nMedium\nHard\n').casefold())
	
	play(points, difficulty)

def play(points, difficulty):
	calc = Calculate(difficulty)

	print('Solve the following challenge: ')
	calc.show_operation()

	result = int(input())

	if calc.check_result(result):
		points += 1
		print('You got 1 point!')
		print(f'You have {points} point(s)!')
	elif not calc.check_result(result):
		points -=1
		print('You lost 1 point!')
		print(f'You have {points} point(s)')

	continue_game = str(input('Do you want to keep playing? (Yes, No): ').casefold())
	change_difficulty = ''
	
	if continue_game == "yes":
		change_difficulty = str(input('Do you want to change the difficulty? (Yes, No): ').casefold())

		print(change_difficulty)
		if change_difficulty == "yes":
			set_difficulty(points)
		else:
			play(points, difficulty)
	elif continue_game == "no":
		print(f'You got {points} point(s).')
		print('See you next time!')

if __name__ == '__main__':
	main()