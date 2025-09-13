from math import floor
from pathlib import Path
from statistics import median
from sys import argv

from data_reading import read_file_lines


_COMMA = ","


def _round_half_up(n: float, decimals: int = 0) -> float:
	# Source: https://realpython.com/python-rounding/#rounding-half-up
	multiplier = 10 ** decimals
	return floor(n * multiplier + 0.5) / multiplier


data_path = Path(argv[1])

positions = *(
	int(p) for p in
	next(read_file_lines(data_path)).split(_COMMA)
),

alignment_position = int(_round_half_up(median(positions)))

fuel_cost = 0

for position in positions:
	fuel_cost += abs(position - alignment_position)

print(f"Alignment position: {alignment_position}")
print(f"Fuel cost: {fuel_cost}")
