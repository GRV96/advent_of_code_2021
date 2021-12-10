from pathlib import Path
from sys import argv

from data_reading import data_from_lines


_ILLEGAL_CHAR_SCORE = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

_OPENING_CLOSING = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}

_OPENING_CHARS = _OPENING_CLOSING.keys()
_CLOSING_CHARS = _OPENING_CLOSING.values()


def _first_illegal_char(line):
	opening_chars = list() # Used as a stack

	for char in line:
		if char in _OPENING_CHARS:
			opening_chars.append(char)

		elif char in _CLOSING_CHARS:
			last_opening = opening_chars[-1]
			expected_closing = _OPENING_CLOSING[last_opening]

			if char != expected_closing:
				return char

			opening_chars.pop()

		else:
			return char

	return None


data_path = Path(argv[1])

lines = data_from_lines(data_path)

score_sum = 0

for line in lines:
	illegal_char = _first_illegal_char(line)

	if illegal_char is not None:
		score_sum += _ILLEGAL_CHAR_SCORE[illegal_char]

print(f"Illegal score sum: {score_sum}")
