from pathlib import Path
from sys import argv

from data_reading import data_from_lines


_COMPLETION_CHAR_SCORE = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

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


def _closing_seq_score(closing_seq):
	score = 0

	for char in closing_seq:
		score *= 5
		score += _COMPLETION_CHAR_SCORE[char]

	return score


def _treat_line(line):
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

	closing_chars = str()
	opening_chars.reverse()

	for char in opening_chars:
		closing_char = _OPENING_CLOSING[char]
		closing_chars += closing_char

	return closing_chars


data_path = Path(argv[1])

lines = data_from_lines(data_path)

completion_scores = list()
illegal_score_sum = 0

for line in lines:
	result = _treat_line(line)

	if len(result) > 1:
		completion_score = _closing_seq_score(result)
		completion_scores.append(completion_score)

	else:
		illegal_score_sum += _ILLEGAL_CHAR_SCORE[result]

completion_scores.sort()
middle_comp_socre_index = int((len(completion_scores) - 1) / 2)
middle_comp_score = completion_scores[middle_comp_socre_index]

print(f"Illegal score sum: {illegal_score_sum}")
print(f"Middle completion socre: {middle_comp_score}")
