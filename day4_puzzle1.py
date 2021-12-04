from pathlib import Path
from sys import argv

from data_reading import read_bingo
from day4_bingo_grid import MarkingResult


data_path = Path(argv[1])

numbers, grids = read_bingo(data_path)
grid_range = range(len(grids))

winning_grid_num = -1
for number in numbers:
	#print(f"Number: {number}")

	for i in grid_range:
		grid = grids[i]
		marking_result = grid.mark_number(number)
		#print(f"\tGrid {i}: {marking_result}")

		if marking_result == MarkingResult.WIN:
			winning_grid_num = i
			winning_grid_score = number * grid.sum_of_unmarked_numbers()
			break
	
	if winning_grid_num >= 0:
		break

print(f"Grid {winning_grid_num} wins!\nScore: {winning_grid_score}")
