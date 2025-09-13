from pathlib import Path
from sys import argv, exit
from typing import Iterable

from data_reading import read_file_lines


_COMMA = ","


def _fuel_cost_puzzle1(alignment: int, positions: Iterable[int]) -> int:
	cost = 0

	for position in positions:
		distance = abs(alignment - position)
		cost += distance

	return cost 


def _fuel_cost_puzzle2(alignment: int, positions: Iterable[int]) -> float:
	cost = 0

	for position in positions:
		distance = abs(alignment - position)
		cost += distance ** 2 + distance

	return cost / 2


data_path = Path(argv[1])
puzzle_num = int(argv[2])

positions = *(
	int(p) for p in
	next(read_file_lines(data_path)).split(_COMMA)
),

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
