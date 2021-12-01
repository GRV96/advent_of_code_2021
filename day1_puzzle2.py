from pathlib import Path
from sys import argv

from data_reading import data_from_lines


class Measurement:

	def __init__(self, data, window_ids):
		self._data = data
		self._window_ids = tuple(window_ids)

	def __str__(self):
		if len(self._window_ids) >= 2:
			window_str = str(self._window_ids)
		else:
			window_str = f"({self._window_ids[0]})"

		return f"{self._data} {window_str}"

	@property
	def data(self):
		return self._data

	@property
	def window_ids(self):
		return self._window_ids


def measurement_from_line(line):
	parts = line.split()
	return Measurement(parts[0], parts[1:])


data_path = Path(argv[1])

measurements = data_from_lines(data_path, measurement_from_line)
for measurement in measurements:
	print(measurement)
