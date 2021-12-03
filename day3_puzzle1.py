from pathlib import Path
from sys import argv

from data_reading import data_from_lines


ONE_AS_STR = "1"


data_path = Path(argv[1])

bin_nums = data_from_lines(data_path)
num_count = len(bin_nums)
bit_count = len(bin_nums[0])

ones = [0 for _ in range(bit_count)]

for number in bin_nums:

	for i in range(len(number)):

		if number[i] == ONE_AS_STR:
			ones[i] += 1

gamma = 0
epsilon = 0

for i in range(bit_count):
	ones_count = ones[i]
	addition = 2**(bit_count-i-1)

	if ones_count > num_count/2:
		gamma += addition

	else:
		epsilon += addition

print(f"Gamma rate: {gamma}")
print(f"Epsilon rate: {epsilon}")
print(f"Gamma * epsilon: {gamma * epsilon}")
