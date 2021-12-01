depths = [
	199,
	200,
	208,
	210,
	200,
	207,
	240,
	269,
	260,
	263]

increases = 0
prev_depth = 10e6

for depth in depths:
	if depth > prev_depth:
		increases += 1

	prev_depth = depth

print(f"Increases: {increases}")
