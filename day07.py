#!/usr/bin/python

# Advent of Code 2025 Day 07


if __name__ == "__main__":

	split_count = 0
	splitters = set()
	start = None
	with open("day07_input", "r") as infile:
		y = 0
		for line in infile.readlines():
			for x, char in enumerate(line.strip()):
				if char == "S":
					start = (x, y)
				elif char == "^":
					splitters.add((x, y))
			y += 1
	max_y = y
	y = start[1]
	beams = { start }
	while y < max_y:
		next_beams = set()
		for beam in beams:
			x, y = beam
			if (x, y+1) not in splitters:
				next_beams.add((x, y+1))
			else:
				split_count += 1
				next_beams.add((x-1, y+1))
				next_beams.add((x+1, y+1))
		beams = next_beams
		y += 1
	print(split_count)

