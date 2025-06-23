from pathlib import Path
from sys import argv

from data_reading import data_from_lines


def _coords_are_low_point(heightmap, row, column, height):
	neighbor_heights = (
		_get_from_heightmap(heightmap, row-1, column), # Up
		_get_from_heightmap(heightmap, row+1, column), # Down
		_get_from_heightmap(heightmap, row, column-1), # Left
		_get_from_heightmap(heightmap, row, column+1)) # Right

	for neighbor_height in neighbor_heights:
		if neighbor_height >= 0 and neighbor_height <= height:
			return False

	return True


def _get_from_heightmap(heightmap, row, column):
	try:
		value = heightmap[row][column]
	except IndexError:
		value = -1

	return value


def _line_to_ints(line):
	return [int(digit) for digit in line]


data_path = Path(argv[1])

heightmap = data_from_lines(data_path, _line_to_ints)

risk_level_sum = 0

for i in range(len(heightmap)):
	row = heightmap[i]

	for j in range(len(row)):
		height = _get_from_heightmap(heightmap, i, j)

		if _coords_are_low_point(heightmap, i, j, height):
			risk_level = height + 1
			risk_level_sum += risk_level

print(f"Sum of the risk levels: {risk_level_sum}")
