from pathlib import Path
from sys import argv

from data_reading import data_from_lines


def _coords_are_low_point(heightmap, row, column, height):
	neighboor_heights = (
		_get_from_2d_tuplist(heightmap, row-1, column), # Up
		_get_from_2d_tuplist(heightmap, row+1, column), # Down
		_get_from_2d_tuplist(heightmap, row, column-1), # Left
		_get_from_2d_tuplist(heightmap, row, column+1)) # Right

	for neighboor_height in neighboor_heights:
		if neighboor_height <= height and neighboor_height >= 0:
			return False

	#print()
	#print(f" {neighboor_heights[0]} ")
	#print(f"{neighboor_heights[2]}{height}{neighboor_heights[3]}")
	#print(f" {neighboor_heights[1]} ")
	return True


def _get_from_2d_tuplist(tuplist, row, column):
	try:
		value = tuplist[row][column]
	except IndexError:
		value = -1

	return value


def _line_to_ints(line):
	numbers = list()

	for digit in line:
		numbers.append(int(digit))

	return numbers


data_path = Path(argv[1])

heightmap = data_from_lines(data_path, _line_to_ints)

risk_level_sum = 0

for i in range(len(heightmap)):
	row = heightmap[i]

	for j in range(len(row)):
		height = _get_from_2d_tuplist(heightmap, i, j)

		if _coords_are_low_point(heightmap, i, j, height):
			risk_level = height + 1
			risk_level_sum += risk_level

print(f"Sum of the risk levels: {risk_level_sum}")
