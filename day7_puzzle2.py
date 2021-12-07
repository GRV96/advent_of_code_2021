from pathlib import Path
from sys import argv

from data_reading import\
	convert_list_content,\
	data_from_lines


_COMMA = ","


def _fuel_cost(alignment, positions):
	cost = 0

	for position in positions:
		distance = abs(alignment - position)
		cost += distance ** 2 + distance

	return cost / 2


data_path = Path(argv[1])

positions = data_from_lines(data_path)[0].split(_COMMA)
convert_list_content(positions, int)

min_fuel_cost = float("inf")
min_fuel_cost_pos = -1

for position in range(min(positions), max(positions)+1):
	cost = _fuel_cost(position, positions)

	if cost < min_fuel_cost:
		min_fuel_cost = cost
		min_fuel_cost_pos = position

min_fuel_cost = int(min_fuel_cost)

print(f"Alignment position: {min_fuel_cost_pos}")
print(f"Fuel cost: {min_fuel_cost}")
