from pathlib import Path
from sys import argv

from data_reading import read_file_lines


data_path = Path(argv[1])

depth_gen = read_file_lines(data_path)

increases = 0
prev_depth = int(next(depth_gen))

for depth in depth_gen:
	depth = int(depth)

	if depth > prev_depth:
		increases += 1

	prev_depth = depth

print(f"Increases: {increases}")
