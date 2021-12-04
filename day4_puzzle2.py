from pathlib import Path
from sys import argv

from data_reading import read_bingo
from day4_bingo_grid import MarkingResult


data_path = Path(argv[1])

numbers, grids = read_bingo(data_path)
grid_count = len(grids)
grid_range = range(grid_count)

winners = set()
last_winner_num = -1
for number in numbers:

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
