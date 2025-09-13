from pathlib import Path
from sys import argv

from data_reading import read_file_lines


_COMMA = ","

_BIRTH_DELAY = 6
_FIRST_BIRTH_DELAY = 8


data_path = Path(argv[1])
duration = int(argv[2])

lanternfish_data = next(read_file_lines(data_path))
lanternfish = [int(lf) for lf in lanternfish_data.split(_COMMA)]

for day in range(duration):

	for i in range(len(lanternfish)):

		if lanternfish[i] > 0:
			lanternfish[i] -= 1

		else:
			lanternfish[i] = _BIRTH_DELAY
			lanternfish.append(_FIRST_BIRTH_DELAY)

print(f"{len(lanternfish)} lanternfish after {duration} days")
