from pathlib import Path
from sys import argv

from data_reading import data_from_lines


_PIPE = "|"
_SPACE = " "
_UNIQUE_SEG_NUMS = (2, 4, 3, 7) # For 1, 4, 7 and 8


data_path = Path(argv[1])

note_entries = data_from_lines(data_path)

identifiable_num_count = 0

for entry in note_entries:
	readings = entry.split(_PIPE)
	readings = readings[1].split(_SPACE)

	for reading in readings:
		if len(reading) in _UNIQUE_SEG_NUMS:
			identifiable_num_count += 1

print(f"Number of 1s, 4s, 7s and 8s: {identifiable_num_count}")
