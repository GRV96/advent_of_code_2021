from math import floor
from pathlib import Path
from sys import argv

from data_reading import\
	convert_list_content,\
	data_from_lines


_COMMA = ","


def fuel_cost(alignment, positions):
	cost = 0

	for position in positions:
		distance = abs(alignment - position)
		cost += distance ** 2 + distance

	return cost / 2


def _quarter(numbers):
	minimum = min(numbers)
	return (max(numbers) - minimum) / 4 + minimum


def _round_half_up(n, decimals=0):
	# Source: https://realpython.com/python-rounding/#rounding-half-up
	multiplier = 10 ** decimals
	return floor(n * multiplier + 0.5) / multiplier


data_path = Path(argv[1])

positions = data_from_lines(data_path)[0].split(_COMMA)
convert_list_content(positions, int)

quarter = _quarter(positions)

min_fuel_cost = float('inf')
min_fuel_cost_pos = -1

for position in positions:
	cost = fuel_cost(position, positions)

	if cost < min_fuel_cost:
		min_fuel_cost = cost
		min_fuel_cost_pos = position

min_fuel_cost = int(_round_half_up(min_fuel_cost))

print(f"Alignment position: {min_fuel_cost_pos}")
print(f"Fuel cost: {min_fuel_cost}")
