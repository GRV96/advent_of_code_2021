from day4_bingo_grid import BingoGrid


_COMMA = ","
_NEW_LINE = "\n"

_FILE_MODE_R = "r"


def convert_list_content(some_list, conversion):
	# conversion is a function that takes a list item as its
	# only argument and transforms it into a usable value.
	for i in range(len(some_list)):
		item = some_list[i]

		if isinstance(item, list):
			convert_list_content(item, conversion)

		else:
			try:
				some_list[i] = conversion(item)
			except:
				pass


def data_from_lines(data_path, conversion=None):
	# data_path is of type pathlib.Path.
	# conversion is a function that takes a line as its
	# only argument and transforms it into usable data.
	lines = _lines_from_file(data_path)
	data = list()

	if conversion is None:
		conv_or_not = lambda line: line
	else:
		conv_or_not = lambda line: conversion(line)

	# Even when no conversion is needed, data must go through
	# this loop so that all empty lines are eliminated.
	for line in lines:
		if len(line) > 0:
			data.append(conv_or_not(line))

	return data


def _lines_from_file(path):
	# path is of type pathlib.Path.
	with path.open(mode=_FILE_MODE_R) as data_file:
		content = data_file.read()

	return content.split(_NEW_LINE)


def read_bingo(data_path):
	# data_path is of type pathlib.Path.
	lines = _lines_from_file(data_path)
	line_count = len(lines)

	numbers = lines[0].split(_COMMA)
	convert_list_content(numbers, int)

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
		convert_list_content(grid_content, int)

		grids.append(BingoGrid(grid_content))

	return numbers, grids
