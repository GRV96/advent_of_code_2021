from pathlib import Path
from sys import argv

from data_reading import data_from_lines


class Measurement:

	def __init__(self, data, window_ids):
		self._data = data
		self._window_ids = tuple(window_ids)

	def __str__(self):
		measurement_str = f"{self._data}"
		window_count = self.window_count

		if window_count == 1:
			window_str = f"({self._window_ids[0]})"
			measurement_str += f" {window_str}"

		elif window_count > 1:
			window_str = f"({self._window_ids[0]}"
			for i in range(1, window_count):
				window_str += f", {self._window_ids[i]}"
			window_str += ")"

			measurement_str += f" {window_str}"

		return measurement_str

	@property
	def data(self):
		return self._data

	@property
	def window_count(self):
		return len(self._window_ids)

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
