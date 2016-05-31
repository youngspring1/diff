#!/usr/bin/pythonw
# -*- coding: utf-8 -*-

# how to change string to strength
# the O(mn) algorithem
# call
# test()

# output:
# | s
# | t
# | r
# - i
# + e
# | n
# | g
# + t
# + h


import numpy
#import scipy
#import sklearn
#import matplotlib


def diff1(a, b):
	a_len = len(a)
	b_len = len(b)
	a_list = a
	b_list = b
	print(a + " len: " + str(a_len))
	print(b + " len: " + str(b_len))

# init matrix
	grid = numpy.zeros((a_len+1, b_len+1))
	for i in range(1, a_len+1):
		grid[i,0] = i
	for j in range(1, b_len+1):
		grid[0,j] = j

	#print grid

# levenshtein
	for row in range(1, a_len+1):
		for col in range(1, b_len+1):
			# up/down
			cost_a = grid[row-1, col] + 1
			# right/left
			cost_b = grid[row, col-1] + 1
			min = cprmin(cost_a, cost_b)
			if a_list[row-1] == b_list[col-1]:
				# diagonal
				cost_c = grid[row-1, col-1]
				min = cprmin(min, cost_c)
			grid[row, col] = min

	#print grid


# snake from end to start
# if snake from start to end
#     it's getting much more complex
	result = []
	row = a_len
	col = b_len
	while row > 0 and col > 0:
		# add
		a = grid[row, col-1]
		# delete
		d = grid[row-1, col]
		# common
		c = grid[row-1, col-1]

		if d < a:
			if a_list[row-1] == b_list[col-1] and c < d:
				result.append('| ' + a_list[row-1])
				row -= 1
				col -= 1
			else:
				result.append('- ' + a_list[row-1])
				row -= 1
		else:
			if a_list[row-1] == b_list[col-1] and c < a:
				result.append('| ' + a_list[row-1])
				row -= 1
				col -= 1
			else:
				result.append('+ ' + b_list[col-1])
				col -= 1


	while col > 0:
		result.append('+ ' + b_list[col-1])
		col -= 1

	while row > 0:
		result.append('- ' + a_list[row-1])
		row -= 1

	result.reverse()


# output
	n = len(result)
	for index in range(0,n):
		print result[index]



def cprmin(a, b):
	if a <= b:
		return a
	else:
		return b

def test():
	print("string -> strength")
	diff1("string", "strength")

# test
test()
