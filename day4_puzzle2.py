from pathlib import Path
from sys import argv
from typing import Generator

from data_reading import read_file_lines
from day4_bingo_grid import BingoGrid, MarkingResult


_SPACE = " "


def _line_to_numbers(line: str, separator: str) -> Generator[int, None, None]:
	return (
		int(number)
		for number in line.split(separator)
		if len(number) > 0
	)


data_path = Path(argv[1])

gen_lines = read_file_lines(data_path)
gen_numbers = _line_to_numbers(next(gen_lines), ",")

# Skip an empty line.
next(gen_lines)

grids: list[BingoGrid] = list()
grid_lines: list[tuple[int]] = list()
for line in gen_lines:
	if len(line) == 0:
		grids.append(BingoGrid(grid_lines))
		grid_lines.clear()
	else:
		number_line = tuple(_line_to_numbers(line, _SPACE))
		grid_lines.append(number_line)

grid_count = len(grids)
grid_range = range(grid_count)

# The set ensures that no winner is counted more than once.
winners = set()
last_winner_num = -1
for number in gen_numbers:

	for i in grid_range:
		grid = grids[i]
		marking_result = grid.mark_number(number)

		if marking_result == MarkingResult.WIN:
			winners.add(i)

			if len(winners) >= grid_count:
				last_winner_num = i
				last_winner_score = number * grid.sum_of_unmarked_numbers()
				break
	
	if last_winner_num >= 0:
		break

print(f"Last winning grid: {last_winner_num}\nScore: {last_winner_score}")
