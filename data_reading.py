from day4_bingo_grid import BingoGrid


_COMMA = ","
_NEW_LINE = "\n"

_FILE_MODE_R = "r"

_TYPES_LIST_TUPLE = (list, tuple)


def data_from_lines(data_path, conversion=None):
	# data_path is of type pathlib.Path.
	# conversion is a function that takes a line as its
	# only argument and transforms it into usable data.
	lines = lines_from_file(data_path)
	data = list()

	if conversion is None:
		conv_or_not = lambda line: line
	else:
		conv_or_not = lambda line: conversion(line)

	for line in lines:
		if len(line) > 0:
			data.append(conv_or_not(line))

	return data


def lines_from_file(path):
	# path is of type pathlib.Path.
	with path.open(mode=_FILE_MODE_R) as data_file:
		content = data_file.read()

	return content.split(_NEW_LINE)


def read_bingo(data_path):
	lines = lines_from_file(data_path)
	line_count = len(lines)

	numbers = lines[0].split(_COMMA)
	_tuplist_to_ints(numbers)

	grid_borders = list()
	for i in range(line_count):
		line = lines[i]

		if len(line.strip()) == 0:
			grid_borders.append(i)

	grids = list()
	for i in range(1, len(grid_borders)):
		grid_start = grid_borders[i-1]
		grid_end = grid_borders[i]

		grid_content = lines[grid_start+1: grid_end]
		for j in range(len(grid_content)):
			grid_content[j] = grid_content[j].split()
		_tuplist_to_ints(grid_content)

		grids.append(BingoGrid(grid_content))

	return numbers, grids


def _tuplist_to_ints(tuplist):
	for i in range(len(tuplist)):
		x = tuplist[i]

		if isinstance(x, _TYPES_LIST_TUPLE):
			_tuplist_to_ints(x)

		else:
			try:
				tuplist[i] = int(x)
			except:
				pass
