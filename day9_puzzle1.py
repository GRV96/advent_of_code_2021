from pathlib import Path
from sys import argv

from data_reading import read_file_lines


def _evaluate_location(heightmap, row, column):
	height = _get_from_heightmap(heightmap, i, j)
	neighbor_heights = (
		_get_from_heightmap(heightmap, row-1, column), # Up
		_get_from_heightmap(heightmap, row+1, column), # Down
		_get_from_heightmap(heightmap, row, column-1), # Left
		_get_from_heightmap(heightmap, row, column+1)) # Right

	is_low_point = True
	for neighbor_height in neighbor_heights:
		if neighbor_height <= height:
			is_low_point = False
			break

	return height, is_low_point


def _get_from_heightmap(heightmap, row, column):
	try:
		value = heightmap[row][column]
	except IndexError:
		value = 10

	return value


def _line_to_ints(line: str) -> tuple[int]:
	return *(int(digit) for digit in line),


data_path = Path(argv[1])
heightmap = *(
	_line_to_ints(heightmap_line)
	for heightmap_line in read_file_lines(data_path)
),

risk_level_sum = 0
for i in range(len(heightmap)):
	row = heightmap[i]

	for j in range(len(row)):
		height, is_low_point = _evaluate_location(heightmap, i, j)

		if is_low_point:
			risk_level = height + 1
			risk_level_sum += risk_level

print(f"Sum of the risk levels: {risk_level_sum}")
