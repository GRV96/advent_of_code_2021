from pathlib import Path
from sys import argv

from data_reading import read_file_lines


_PIPE: str = "|"
_SPACE: str = " "

_DIGIT_TO_PATTERN_SIZE: dict[int, int] = {
	0: 6,
	1: 2,
	2: 5,
	3: 5,
	4: 4,
	5: 5,
	6: 6,
	7: 3,
	8: 7,
	9: 6
}

_PATTERN_SIZE_TO_DIGIT: dict[int, int] = {
	2: 1,
	3: 7,
	4: 4,
	7: 8
}


def _are_patterns_equivalent(pattern1: str, pattern2: str) -> bool:
	if len(pattern1) != len(pattern2):
		return False

	for segment in pattern1:
		if segment not in pattern2:
			return False

	return True


def _raise_digit_error(digit: int) -> None:
	if digit < 0 or digit > 9:
		raise ValueError(f"Digits range from 0 to 9. Recieved {digit}.")


class DigitPatternMap:
	UNDEF_DIGIT: int = -1

	def __init__(self) -> None:
		self._digit_to_pattern = dict()
		self._pattern_to_digit = dict()

	def get_digit(self, pattern: str) -> int:
		for patt, digit in self._pattern_to_digit.items():
			if _are_patterns_equivalent(patt, pattern):
				return digit

		return pattern, self.__class__.UNDEF_DIGIT

	def get_digit_to_pattern(self) -> dict[int, str]:
		return dict(self._digit_to_pattern)

	def get_pattern(self, digit: int) -> str:
		_raise_digit_error(digit)
		return self._digit_to_pattern.get(digit)

	def get_pattern_to_digit(self) -> dict[str, int]:
		return dict(self._pattern_to_digit)

	def has_digit(self, digit: int) -> bool:
		_raise_digit_error(digit)
		return digit in self._digit_to_pattern

	def has_pattern(self, pattern: str) -> bool:
		return pattern in self._pattern_to_digit

	def register(self, digit: int, pattern: str) -> None:
		_raise_digit_error(digit)
		self._digit_to_pattern[digit] = pattern
		self._pattern_to_digit[pattern] = digit


class PatternCollection:
	def __init__(self, patterns) -> None:
		self._content = tuple(patterns)

	def __iter__(self):
		return iter(self._content)

	def get_patterns_of_size(self, pattern_size: int) -> tuple[str, ...]:
		return *(pattern
		   for pattern in self._content
		   if len(pattern) == pattern_size),


def _nb_segs_not_in_other_pattern(pattern1: str, pattern2: str) -> int:
	"""
	Counts the segments in the first pattern that do not appear in the second
	pattern.
	"""
	count = 0

	for seg in pattern1:
		if seg not in pattern2:
			count += 1

	return count


def _map_digit_to_pattern(
		digit_pattern_map: DigitPatternMap,
		known_digit: int,
		unknown_digit: int,
		difference: int) -> None:
	_raise_digit_error(known_digit)
	_raise_digit_error(unknown_digit)

	pattern_size = _DIGIT_TO_PATTERN_SIZE[unknown_digit]
	known_pattern = digit_pattern_map.get_pattern(known_digit)

	for pattern in patterns:

		if len(pattern) != pattern_size\
				or digit_pattern_map.has_pattern(pattern):
			continue

		if difference >= 0:
			diff = _nb_segs_not_in_other_pattern(pattern, known_pattern)
		else:
			diff = _nb_segs_not_in_other_pattern(known_pattern, pattern)

		if diff == difference:
			digit_pattern_map.register(unknown_digit, pattern)
			break


data_path = Path(argv[1])

gen_note_entries = read_file_lines(data_path)

output_sum = 0

for entry in gen_note_entries:
	split_entry = entry.split(_PIPE)
	patterns = PatternCollection(split_entry[0].strip().split(_SPACE))
	outputs = split_entry[1].strip().split(_SPACE)

	digit_pattern_map = DigitPatternMap()

	for pattern in patterns:
		pattern_length = len(pattern)
		digit = _PATTERN_SIZE_TO_DIGIT.get(
			pattern_length, DigitPatternMap.UNDEF_DIGIT)

		if digit != DigitPatternMap.UNDEF_DIGIT:
			digit_pattern_map.register(digit, pattern)

	# 2 has three segments that 4 does not have.
	_map_digit_to_pattern(digit_pattern_map, 4, 2, 3)

	# 3 has three segments that 1 does not have.
	_map_digit_to_pattern(digit_pattern_map, 1, 3, 3)

	# 5 is the last digit with five segments.
	for pattern in patterns.get_patterns_of_size(5):
		if not digit_pattern_map.has_pattern(pattern):
			digit_pattern_map.register(5, pattern)
			break

	# 6 has five segments that 1 does not have.
	_map_digit_to_pattern(digit_pattern_map, 1, 6, 5)

	# 9 has two segments that 4 does not have.
	_map_digit_to_pattern(digit_pattern_map, 4, 9, 2)

	# 0 is the last unknown pattern.
	for pattern in patterns:
		if not digit_pattern_map.has_pattern(pattern):
			digit_pattern_map.register(0, pattern)
			break

	number = 0
	digits = *(digit_pattern_map.get_digit(output) for output in outputs),
	nb_digits = len(digits)
	for i in range(nb_digits):
		number += digits[i] * 10 ** (nb_digits - i - 1)

	output_sum += number

print(f"Output sum: {output_sum}")
