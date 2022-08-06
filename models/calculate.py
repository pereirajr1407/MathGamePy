from random import randint

class Calculate:

	def __init__(self: object, difficulty: int, ):
		self.__difficulty = difficulty
		self.__first_value = self._generate_value
		self.__second_value = self._generate_value
		self.__operation = randint(1, 3)
		self.__result = self._generate_result

	@property
	def difficulty(self: object):
		return self.__difficulty

	@property
	def first_value(self: object):
		return self.__first_value

	@property
	def second_value(self: object):
		return self.__second_value
	
	@property
	def operation(self: object):
		return self.__operation

	@property
	def result(self: object):
		return self.__result

	def __str__(self: object):
		op = ''
		if self.operation == 1:
			op = 'Sum'
		elif self.operation == 2:
			op = 'Subtract'
		else:
			op = 'Multiply'

	@property
	def _generate_value(self: object):
		if self.difficulty == "kid play":
			return randint(0, 10)
		elif self.difficulty == "easy":
			return randint(0, 100)
		elif self.difficulty == "medium":
			return randint(0, 1000)
		elif self.difficulty == "hard":
			return randint(0, 10000)

	@property
	def _generate_result(self: object):
		if self.operation == 1:
			return self.first_value + self.second_value
		elif self.operation == 2:
			return self.first_value - self.second_value
		else:
			return self.first_value * self.second_value

	@property
	def _op_symbol(self: object):
		if self.operation == 1:
			return '+'
		elif self.operation == 2:
			return '-'
		else:
			return 'x'

	def check_result(self: object, answer: int):
		correct = False
		if self.result == answer:
			print('Correct!')
			correct = True
		else:
			print('Wrong answer!')
		print(f'{self.first_value} {self._op_symbol} {self.second_value} = {self.result}')
		return correct

	def show_operation(self: object) -> None:
		print(f'{self.first_value} {self._op_symbol} {self.second_value} = ?')