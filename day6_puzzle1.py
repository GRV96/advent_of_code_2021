from pathlib import Path
from sys import argv

from data_reading import convert_list_content, data_from_lines


_COMMA = ","

_INIT_TIME = 8
_RESET_TIME = 6


data_path = Path(argv[1])
duration = int(argv[2])

lanternfish_data = data_from_lines(data_path)[0]
lanternfish = lanternfish_data.split(_COMMA)
convert_list_content(lanternfish, int)

for day in range(duration):

	for i in range(len(lanternfish)):

		if lanternfish[i] > 0:
			lanternfish[i] -= 1

		else:
			lanternfish[i] = _RESET_TIME
			lanternfish.append(_INIT_TIME)

print(f"{len(lanternfish)} lanternfish after {duration} days")
