from pathlib import Path
from sys import argv

from data_reading import data_from_lines


data_path = Path(argv[1])

depths = data_from_lines(data_path, int)

increases = 0
prev_depth = 10e6

for depth in depths:
	if depth > prev_depth:
		increases += 1

	prev_depth = depth

print(f"Increases: {increases}")
