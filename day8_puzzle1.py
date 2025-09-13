from pathlib import Path
from sys import argv

from data_reading import read_file_lines


_PIPE = "|"
_SPACE = " "
_UNIQUE_SEG_NUMS = (2, 4, 3, 7) # For 1, 4, 7 and 8


data_path = Path(argv[1])

gen_note_entries = read_file_lines(data_path)

identifiable_num_count = 0
for entry in gen_note_entries:
	split_entry = entry.split(_PIPE)
	outputs = split_entry[1].split(_SPACE)

	for output in outputs:
		if len(output) in _UNIQUE_SEG_NUMS:
			identifiable_num_count += 1

print(f"Number of 1s, 4s, 7s and 8s: {identifiable_num_count}")
