from pathlib import Path
from sys import argv

from data_reading import data_from_lines


_ARROW = " -> "
_COMMA = ","


data_path = Path(argv[1])

vent_line_data = data_from_lines(data_path)

diagram = dict()

for vld in vent_line_data:
	coords = vld.split(_ARROW)

	start = coords[0].split(_COMMA)
	start_x = int(start[0])
	start_y = int(start[1])

	end = coords[1].split(_COMMA)
	end_x = int(end[0])
	end_y = int(end[1])

	# Vertical line
	if start_x == end_x:
		step = 1 if end_y >= start_y else -1

		for i in range(start_y, end_y+step, step):
			coord_key = (start_x, i)
			diagram[coord_key] = diagram.get(coord_key, 0) + 1

	# Horizontal line
	if start_y == end_y:
		step = 1 if end_x >= start_x else -1

		for j in range(start_x, end_x+step, step):
			coord_key = (j, start_y)
			diagram[coord_key] = diagram.get(coord_key, 0) + 1

hot_point_count = 0
for overlappings in diagram.values():
	if overlappings >= 2:
		hot_point_count += 1

print(f"Two lines or more overlap at {hot_point_count} points.")
