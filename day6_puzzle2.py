from pathlib import Path
from sys import argv

from data_reading import read_file_lines


_COMMA = ","

_BIRTH_DELAY = 7
_FIRST_BIRTH_DELAY = 9


# This script performs the same task as day6_puzzle1, but much faster.

data_path = Path(argv[1])
duration = int(argv[2])

lanternfish_data = next(read_file_lines(data_path))
lanternfish = [int(lf) for lf in lanternfish_data.split(_COMMA)]
fish_count = len(lanternfish)

duration_range = range(duration)
birth_calendar = [0 for _ in duration_range]

for time in lanternfish:
	birth_calendar[time] += 1

for day in duration_range:
	births = birth_calendar[day]

	if births > 0:
		fish_count += births

		try:
			birth_calendar[day + _BIRTH_DELAY] += births
		except IndexError:
			pass
		
		try:
			birth_calendar[day + _FIRST_BIRTH_DELAY] += births
		except IndexError:
			pass

print(f"{fish_count} lanternfish after {duration} days")
