from pathlib import Path
from sys import argv

from data_reading import data_from_lines


_PIPE = "|"
_SPACE = " "


_NORMAL_DISPLAYS = {
	0: "abcefg",
	1: "cf",
	2: "acdeg",
	3: "acdfg",
	4: "bcdf",
	5: "abdfg",
	6: "abdefg",
	7: "acf",
	8: "abcdefg",
	9: "abcdfg"}

_SEG_COUNT_DIGITS = {
	2: (1,),
	3: (7,),
	4: (4,),
	5: (2, 3, 5),
	6: (0, 6, 9),
	7: (8,)}


def _digit_display_matches_wiring(digit, display, wiring):
	normal_display = _NORMAL_DISPLAYS[digit]
	expected_seg_count = len(normal_display)

	seg_count = 0

	for normal_segment in normal_display:
		possible_wirings = wiring[normal_segment]

		for segment in possible_wirings:

			if segment in display:
				seg_count += 1

			else:
				# The display does not match the normal display.
				return -1

	if seg_count == expected_seg_count:
		# The display fully matches the normal display.
		return 1

	# The display partially matches the normal display.
	return 0


def _displays_and_wiring(signal_patterns):
	signal_patterns = list(signal_patterns)
	actual_displays = _init_actual_displays(signal_patterns)
	wiring = _init_wiring(actual_displays)
#	for normal, actual in wiring.items():
#		print(normal + ": " + str(actual))

	while len(signal_patterns) > 0:

		for patterns in actual_displays.values():

			if len(patterns) == 1:
				try:
					signal_patterns.remove(patterns[0])
				except ValueError:
					pass

		for pattern in signal_patterns:
			pattern_length = len(pattern)

			if pattern_length not in _SEG_COUNT_DIGITS:
				continue

			possible_digits = _SEG_COUNT_DIGITS[pattern_length]

			for digit in possible_digits:
				possible_displays = actual_displays[digit]

				if len(possible_displays) == 1:
					continue

				i = 0
				while i < len(possible_displays):
					display = possible_displays[i]
					match = _digit_display_matches_wiring(digit, display, wiring)

					if match < 0:
						possible_displays.remove(display)

					elif match > 0:
						possible_displays.clear()
						possible_displays.append()
						i += 1

	return actual_displays, wiring


def _init_actual_displays(signal_patterns):
	# Keys: digits
	# Values: lists of possible patterns (strings)
	actual_displays = {n: list() for n in range(10)}

	for pattern in signal_patterns:
		pattern_length = len(pattern)

		if pattern_length not in _SEG_COUNT_DIGITS:
			continue

		if pattern_length == 2:
			actual_displays[1].append(pattern)

		elif pattern_length == 4:
			actual_displays[4].append(pattern)

		elif pattern_length == 3:
			actual_displays[7].append(pattern)

		elif pattern_length == 7:
			actual_displays[8].append(pattern)

		else:
			possible_digits = _SEG_COUNT_DIGITS[pattern_length]

			for digit in possible_digits:
				possible_displays = actual_displays[digit]
				possible_displays.append(pattern)

	return actual_displays


def _init_wiring(actual_displays):
	# Keys: normal segment characters
	# Values: sets of possible corresponding segment characters
	wiring = {character: set() for character in "abcdefg"}

	display_of_1 = actual_displays[1][0]
	display_of_4 = actual_displays[4][0]
	display_of_7 = actual_displays[7][0]
	display_of_8 = actual_displays[8][0]

	display_of_4_and_7 = display_of_4 + display_of_7

	wiring_a = wiring['a']
	wiring_b = wiring['b']
	wiring_c = wiring['c']
	wiring_d = wiring['d']
	wiring_e = wiring['e']
	wiring_f = wiring['f']
	wiring_g = wiring['g']

	for segment in display_of_7:

		if segment in display_of_1:
			wiring_c.add(segment)
			wiring_f.add(segment)

		elif segment not in wiring_a:
			wiring_a.add(segment)

	for segment in display_of_4:

		if segment not in display_of_1:
			wiring_b.add(segment)
			wiring_d.add(segment)

	for segment in display_of_8:

		if segment not in display_of_4_and_7:
			wiring_e.add(segment)
			wiring_g.add(segment)

	return wiring


data_path = Path(argv[1])

note_entries = data_from_lines(data_path)
signal_patterns = note_entries[0].split(_PIPE)[0]
signal_patterns = signal_patterns.split(_SPACE)

actual_displays, wiring = _displays_and_wiring(signal_patterns)
print(actual_displays)
