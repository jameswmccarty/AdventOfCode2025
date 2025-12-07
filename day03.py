#!/usr/bin/python

# Advent of Code 2025 Day 03

def p1_linemax(digits):
	m = 0
	for i in range(len(digits)-1):
		for j in range(i+1,len(digits)):
			m = max(m, int(digits[i]+digits[j]))
	return m

if __name__ == "__main__":

	p1_total = 0
	i = 0
	with open("day03_input", "r") as infile:
		for line in infile:
			i += 1
			p1_total += p1_linemax(line.strip())
	print(p1_total)
