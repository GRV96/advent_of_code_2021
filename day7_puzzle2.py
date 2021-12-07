from pathlib import Path
from sys import argv, exit

from data_reading import\
	convert_list_content,\
	data_from_lines


_COMMA = ","


def _fuel_cost_puzzle1(alignment, positions):
	cost = 0

	for position in positions:
		distance = abs(alignment - position)
		cost += distance

	return cost 


def _fuel_cost_puzzle2(alignment, positions):
	cost = 0

	for position in positions:
		distance = abs(alignment - position)
		cost += distance ** 2 + distance

	return cost / 2


data_path = Path(argv[1])
puzzle_num = int(argv[2])

positions = data_from_lines(data_path)[0].split(_COMMA)
convert_list_content(positions, int)

if puzzle_num == 1:
	fuel_cost_fnc = _fuel_cost_puzzle1
elif puzzle_num == 2:
	fuel_cost_fnc = _fuel_cost_puzzle2
else:
	print(f"{puzzle_num} is not a puzzle number.")
	exit(1)

min_fuel_cost = float("inf")
min_fuel_cost_pos = -1

for position in range(min(positions), max(positions)+1):
	cost = fuel_cost_fnc(position, positions)

	if cost < min_fuel_cost:
		min_fuel_cost = cost
		min_fuel_cost_pos = position

min_fuel_cost = int(min_fuel_cost)

print(f"Alignment position: {min_fuel_cost_pos}")
print(f"Fuel cost: {min_fuel_cost}")
