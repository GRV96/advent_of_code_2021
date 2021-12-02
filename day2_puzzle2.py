from enum import Enum
from pathlib import Path
from sys import argv

from data_reading import data_from_lines


DOWN = "down"
FORWRARD = "forward"
UP = "up"


data_path = Path(argv[1])

movements = data_from_lines(data_path)

aim = 0
h_pos = 0
depth = 0

for movement in movements:
	parts = movement.split()
	direction = parts[0]
	magnitude = int(parts[1])

	if direction == DOWN:
		aim += magnitude

	elif direction == FORWRARD:
		h_pos += magnitude
		depth += aim * magnitude

	elif direction == UP:
		aim -= magnitude

print(f"Horizontal position * depth = {h_pos * depth}")
