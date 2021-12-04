from enum import Enum


class MarkingResult(Enum):
	NO_MATCH = 0
	MATCH = 1
	WIN = 2


class BingoSquare:

	def __init__(self, number, marked=False):
		self._number = number
		self._marked = marked

	@property
	def number(self):
		return self._number

	@property
	def marked(self):
		return self._marked

	@marked.setter
	def marked(self, marked):
		self._marked = marked


class BingoGrid:
	# Row index: i
	# Column index: j

	def __init__(self, numbers):
		self._content = dict()
		self._init_content(numbers)

	def _init_content(self, numbers):
		for i in range(len(numbers)):
			number_line = numbers[i]

			for j in range(len(number_line)):
				self._content[(i, j)] = BingoSquare(number_line[j])

	def _column_wins(self, column):
		i = 0
		while True:
			try:
				square = self._content[i, column]
			except KeyError:
				break

			if not square.marked:
				return False

			i += 1

		return True

	def mark_number(self, number):
		for coords, square in self._content.items():
			num_at_coords = square.number

			if num_at_coords == number:
				square.marked = True

				if self._row_wins(coords[0]) or self._column_wins(coords[1]):
					return MarkingResult.WIN

				else:
					return MarkingResult.MATCH

		return MarkingResult.NO_MATCH

	def _row_wins(self, row):
		j = 0
		while True:
			try:
				square = self._content[row, j]
			except KeyError:
				break

			if not square.marked:
				return False

			j += 1

		return True

	def sum_of_unmarked_numbers(self):
		sum = 0

		for square in self._content.values():
			if not square.marked:
				sum += square.number

		return sum
