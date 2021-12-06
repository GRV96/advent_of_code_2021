from pathlib import Path
from sys import argv

from data_reading import convert_list_content, data_from_lines


_COMMA = ","

_DURATION = 80 # In days

_INIT_TIME = 8
_RESET_TIME = 6


data_path = Path(argv[1])

lanternfish_data = data_from_lines(data_path)[0]
lanternfish = lanternfish_data.split(_COMMA)
convert_list_content(lanternfish, int)

for day in range(_DURATION):

	for i in range(len(lanternfish)):

		if lanternfish[i] > 0:
			lanternfish[i] -= 1

		else:
			lanternfish[i] = _RESET_TIME
			lanternfish.append(_INIT_TIME)


print(f"{len(lanternfish)} lanternfish after {_DURATION} days")
