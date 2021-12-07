from math import floor
from pathlib import Path
from sys import argv

from data_reading import\
	convert_list_content,\
	data_from_lines


_COMMA = ","


def _round_half_up(n, decimals=0):
	# Source: https://realpython.com/python-rounding/#rounding-half-up
	multiplier = 10 ** decimals
	return floor(n*multiplier + 0.5) / multiplier

data_path = Path(argv[1])

positions = data_from_lines(data_path)[0].split(_COMMA)
convert_list_content(positions, int)

average_position = sum(positions)/len(positions)
average_position = int(_round_half_up(average_position))

fuel_cost = 0

for position in positions:
	fuel_cost += abs(position - average_position)

print(f"Alignement position: {average_position}")
print(f"Fuel cost: {fuel_cost}")
