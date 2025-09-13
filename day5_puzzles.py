from pathlib import Path
from sys import argv

from data_reading import read_file_lines


_ARROW = " -> "
_COMMA = ","


def _sign(number):
	sign = 0

	if number > 0:
		sign = 1

	elif number < 0:
		sign = -1

	return sign


data_path = Path(argv[1])
puzzle_num = int(argv[2])

if puzzle_num == 1:
	consider_diagonals = False
elif puzzle_num == 2:
	consider_diagonals = True
else:
	print(f"{puzzle_num} is not a puzzle number.")
	exit(1)

vent_line_data = read_file_lines(data_path)

diagram = dict()

for vld in vent_line_data:
	coords = vld.split(_ARROW)

	start = coords[0].split(_COMMA)
	start_x = int(start[0])
	start_y = int(start[1])

	end = coords[1].split(_COMMA)
	end_x = int(end[0])
	end_y = int(end[1])

	delta_x = end_x - start_x
	delta_y = end_y - start_y
	sign_delta_x = _sign(delta_x)
	sign_delta_y = _sign(delta_y)

	step = sign_delta_x if delta_x != 0 else sign_delta_y

	# Vertical line
	if start_x == end_x:
		for i in range(start_y, end_y+step, step):
			coord_key = (start_x, i)
			diagram[coord_key] = diagram.get(coord_key, 0) + 1

	# Horizontal line
	elif start_y == end_y:
		for j in range(start_x, end_x+step, step):
			coord_key = (j, start_y)
			diagram[coord_key] = diagram.get(coord_key, 0) + 1

	# Diagonal line
	elif consider_diagonals:
		point_count = abs(delta_x) + 1 if delta_x > 0 else abs(delta_y) + 1

		for n in range(point_count):
			coord_key =\
				(start_x + n * sign_delta_x, start_y + n * sign_delta_y)
			diagram[coord_key] = diagram.get(coord_key, 0) + 1

hot_point_count = 0
for overlappings in diagram.values():
	if overlappings >= 2:
		hot_point_count += 1

print(f"Two lines or more overlap at {hot_point_count} points.")
