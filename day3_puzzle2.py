from enum import Enum
from pathlib import Path
from sys import argv

from data_reading import data_from_lines


EMPTY_STR = ""
ONE_AS_STR = "1"
ZERO_AS_STR = "0"

class RatingValue(Enum):
	OG = 0 # Oxygen generator rating
	CS = 1 # CO2 scrubber rating


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


def make_bit_criteria(mcb, rating_value):
	if mcb == EMPTY_STR: # Equal number of zeroes and ones
		if rating_value == RatingValue.OG:
			return lambda bit: bit == ONE_AS_STR

		elif rating_value == RatingValue.CS:
			return lambda bit: bit == ZERO_AS_STR

		else:
			return None

	else:
		if rating_value == RatingValue.OG:
			return lambda bit: bit == mcb

		elif rating_value == RatingValue.CS:
			return lambda bit: bit != mcb

		else:
			return None


data_path = Path(argv[1])

bin_numbers = data_from_lines(data_path)
bit_count = len(bin_numbers[0])

og_numbers = list(bin_numbers)
cs_numbers = list(bin_numbers)

for i in range(bit_count):
	og_most_common_bit = get_most_common_bit(og_numbers, i)
	og_criteria = make_bit_criteria(og_most_common_bit, RatingValue.OG)

	j = 0
	while len(og_numbers) > 1:
		try:
			number = og_numbers[j]
		except IndexError:
			break

		bit = number[i]

		if og_criteria(bit):
			j += 1
		else:
			og_numbers.remove(number)

	cs_most_common_bit = get_most_common_bit(cs_numbers, i)
	cs_criteria = make_bit_criteria(cs_most_common_bit, RatingValue.CS)
	j = 0
	while len(cs_numbers) > 1:
		try:
			number = cs_numbers[j]
		except IndexError:
			break

		bit = number[i]

		if cs_criteria(bit):
			j += 1
		else:
			cs_numbers.remove(number)

og_rating = int(og_numbers[0], 2)
cs_rating = int(cs_numbers[0], 2)

print(f"Oxygen generation rating: {og_rating}")
print(f"CO2 scrubber rating: {cs_rating}")
print(f"Life support rating: {og_rating * cs_rating}")
