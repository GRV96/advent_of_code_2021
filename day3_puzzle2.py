from pathlib import Path
from sys import argv

from data_reading import data_from_lines


EMPTY_STR = ""
ONE_AS_STR = "1"
ZERO_AS_STR = "0"


def get_most_common_bit(bin_numbers, index):
	mcb = EMPTY_STR
	ones = 0
	zeroes = 0

	for number in bin_numbers:
		bit = number[index]

		if bit == ONE_AS_STR:
			ones += 1

		elif bit == ZERO_AS_STR:
			zeroes += 1

	if ones > zeroes:
		mcb = ONE_AS_STR

	elif ones < zeroes:
		mcb = ZERO_AS_STR

	return mcb


data_path = Path(argv[1])

bin_numbers = data_from_lines(data_path)
bit_count = len(bin_numbers[0])

og_numbers = list(bin_numbers)
cs_numbers = list(bin_numbers)

for i in range(bit_count):
	most_common_bit = get_most_common_bit(og_numbers, i)

	j = 0
	while len(og_numbers) > 1:
		try:
			number = og_numbers[j]
		except IndexError:
			break

		bit = number[i]

		if most_common_bit == EMPTY_STR:
			# Equal number of zeroes and ones
			if bit == ZERO_AS_STR:
				og_numbers.remove(number)
				j -= 1

		else:
			if bit != most_common_bit:
				og_numbers.remove(number)
				j -= 1

		j += 1

	j = 0
	while len(cs_numbers) > 1:
		try:
			number = cs_numbers[j]
		except IndexError:
			break

		bit = number[i]

		if most_common_bit == EMPTY_STR:
			# Equal number of zeroes and ones
			if bit == ONE_AS_STR:
				cs_numbers.remove(number)
				j -= 1

		else:
			if bit == most_common_bit:
				cs_numbers.remove(number)
				j -= 1

		j += 1

og_rating = int(og_numbers[0], 2)
cs_rating = int(cs_numbers[0], 2)

print(f"Oxygen generation rating: {og_rating}")
print(f"CO2 scrubber rating: {cs_rating}")
print(f"Life support rating: {og_rating * cs_rating}")
