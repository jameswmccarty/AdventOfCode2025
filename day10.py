#!/usr/bin/python

# Advent of Code 2025 Day 10

from collections import deque

def press_dfs(goal, buttons):
	lights = (False,) * len(goal)
	seen = { lights }
	q = deque()
	q.append((0, lights))
	while q:
		steps, status = q.popleft()
		if status == goal:
			return steps
		for press in buttons:
			new_state = list(status)
			for pos in press:
				new_state[pos] ^= True
			new_state = tuple(new_state)
			if new_state not in seen:
				seen.add(new_state)
				q.append((steps+1, new_state))
	return float('inf')

def p1_min(line):
	line = line.strip().split()
	lights = []
	for idx, char in enumerate(line[0]):
		if char == '#':
			lights.append(True)
		else:
			lights.append(False)
	lights = tuple(lights[1:-1]) # strip brackets
	line.pop(0)
	line.pop(-1)
	buttons = [ eval(x[0:-1]+",)") for x in line ]
	return press_dfs(lights, buttons)


if __name__ == "__main__":

	presses = 0
	with open("day10_input", "r") as infile:
		for line in infile:
			presses += p1_min(line)
	print(presses)

