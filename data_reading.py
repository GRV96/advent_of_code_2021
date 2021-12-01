_NEW_LINE = "\n"


def data_from_lines(data_path, conversion=None):
	# data_path is of type pathlib.Path.
	# conversion is a function that takes a line as its
	# only argument and transforms it into usable data.
	with data_path.open(mode="r") as data_file:
		content = data_file.read()

	lines = content.split(_NEW_LINE)
	data = list()

	if conversion is None:
		conv_or_not = lambda line: line
	else:
		conv_or_not = lambda line: conversion(line)

	for line in lines:
		if len(line) > 0:
			data.append(conv_or_not(line))

	return data
