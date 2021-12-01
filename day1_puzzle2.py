from pathlib import Path
from sys import argv

from data_reading import data_from_lines


WINDOW_SIZE = 3


class MeasurementWindow:

	def __init__(self, measurements):
		self._measurements = tuple(measurements)
		self._sum = sum(self._measurements)

	def __iter__(self):
		return iter(self._measurements)

	def __len__(self):
		return len(self._measurements)

	@property
	def measurements(self):
		return self._measurements

	@property
	def sum(self):
		return self._sum


data_path = Path(argv[1])

depths = data_from_lines(data_path, int)
depth_count = len(depths)
loop_limit = depth_count - depth_count % WINDOW_SIZE

windows = list()
for i in range(loop_limit):
	windows.append(MeasurementWindow(depths[i: i+WINDOW_SIZE]))

increases = 0
prev_sum = 10e6 # Arbitrarily high number

for window in windows:
	sum = window.sum

	if sum > prev_sum:
		increases += 1

	prev_sum = sum

print(f"Sum increases: {increases}")
