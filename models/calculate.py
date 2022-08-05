from random import randint

class Calculate:

	def __init__(self: object, difficulty: int, ) -> None:
		self.__difficulty: int = difficulty
		self.__first_value: int = self._generate_value
		self.__second_value: int = self._generate_value
		self.__operation: int = randint(1, 3)
		self.__result: int = self._generate_result

	@property
	def difficulty(self: object) -> int:
		return self.__difficulty

	@property
	def first_value(self: object) -> int:
		return self.__first_value

	@property
	def second_value(self: object) -> int:
		return self.__second_value
	
	@property
	def operation(self: object) -> int:
		return self.__operation

	@property
	def result(self: object) -> int:
		return self.__result

	def __str__(self: object) -> str:
		op: str = ''
		if self.operation == 1:
			op = 'Sum'
		elif self.operation == 2:
			op = 'Subtract'
		else:
			op = 'Multiply'

		return f'First value: {self.first_value} \nSecond value: {self.second_value} \nDifficulty: {self.difficulty} \nOperation: {op}'

	@property
	def _generate_value(self: object) -> int:
		if self.difficulty == 1:
			return randint(0, 10)
		elif self.difficulty == 2:
			return randint(0, 100)
		elif self.difficulty == 3:
			return randint(0, 1000)
		elif self.difficulty == 4:
			return randint(0, 10000)
		else:
			print('Very funny... Now solve this one: ')
			return randint(0, 100000)

	@property
	def _generate_result(self: object) -> int:
		if self.operation == 1:
			return self.first_value + self.second_value
		elif self.operation == 2:
			return self.first_value - self.second_value
		else:
			return self.first_value * self.second_value

	@property
	def _op_symbol(self: object) -> str:
		if self.operation == 1:
			return '+'
		elif self.operation == 2:
			return '-'
		else:
			return '*'

	def check_result(self: object, answer: int) -> bool:
		correct: bool = False
		if self.result == answer:
			print('Correct!')
			correct = True
		else:
			print('Wrong answer!')
		print(f'{self.first_value} {self._op_symbol} {self.second_value} = {self.result}')
		return correct

	def show_operation(self: object) -> None:
		print(f'{self.first_value} {self._op_symbol} {self.second_value} = ?')