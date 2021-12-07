from math import floor
from pathlib import Path
from statistics import median
from sys import argv

from data_reading import\
	convert_list_content,\
	data_from_lines


_COMMA = ","


def _round_half_up(n, decimals=0):
	# Source: https://realpython.com/python-rounding/#rounding-half-up
	multiplier = 10 ** decimals
	return floor(n * multiplier + 0.5) / multiplier

data_path = Path(argv[1])

positions = data_from_lines(data_path)[0].split(_COMMA)
convert_list_content(positions, int)

alignment_position = sum(positions) / len(positions)
alignment_position = int(_round_half_up(alignment_position))

fuel_cost = 0

for position in positions:
	distance = abs(position - alignment_position)
	fuel_cost += int(distance * (distance + 1) / 2)

print(f"Alignement position: {alignment_position}")
print(f"Fuel cost: {fuel_cost}")
