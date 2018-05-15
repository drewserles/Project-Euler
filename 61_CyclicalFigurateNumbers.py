"""
PROBLEM 61
https://projecteuler.net/problem=61
-----------------------------------------------------------------------------
OBSERVATIONS
-Cyclic refers to last 2 digits of number A being first 2 digits of number B.
-Set of 6 numbers for the 6 figurate numbers 3 - 9
-The order of the cyclic doesn't have to correspond to the order of the
figurates (largest to smallest). This is shown in example triplet
-----------------------------------------------------------------------------
STRATEGY
-Generate all the 4 digit numbers for each figurate type (triangle, square etc)
-Start looking at the sequence from the triangle number. Generate all permutations
of the order the remaining numbers can take
-For each triangular number, check all the values that could come next for a
given permutation. If a digit is not cyclic then continue onto the next, if it
is then go to the next figurate type.

Example - Permutation (3, 1, 2, 4, 5) means that in the sequence the triangular
number is followed by a hexagonal, a square, a pentagonal, a heptagonal and an
octagonal. 
"""

import itertools
import time

start = time.time()

"""
Determine all the 4 digit numbers of type triangle to octagonal
"""
c1, c2, c3, c4, c5, c6 = 1, 1, 1, 1, 1, 1
tri, sq, pent, hex, hept, oct = 1, 1, 1, 1, 1, 1
triangle, square, pentagonal, hexagonal, heptagonal, octagonal = [], [], [], [], [], []
#triangle
while 1:
	tri = c1*(c1 + 1)//2
	s_len = len(str(tri))
	if s_len == 4:
		triangle.append(tri)
	elif s_len > 4:
		break
	c1 += 1
#square
while len(str(sq)) < 5:
	sq = c2**2
	if len(str(sq)) == 4:
		square += [sq]
	c2 += 1
#pentagonal
while len(str(pent)) < 5:
	pent = c3*(3*c3 - 1)//2
	if len(str(pent)) == 4:
		pentagonal.append(pent)
	c3 += 1
#hexagonal
while len(str(hex)) < 5:
	hex = c4*(2*c4 - 1)
	if len(str(hex)) == 4:
		hexagonal.append(hex)
	c4 += 1
#heptagonal
while len(str(hept)) < 5:
	hept = c5*(5*c5 - 3)//2
	if len(str(hept)) == 4:
		heptagonal.append(hept)
	c5 += 1
#octagonal
while len(str(oct)) < 5:
	oct = c6*(3*c6 - 2)
	if len(str(oct)) == 4:
		octagonal.append(oct)
	c6 += 1

polys = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

# Return all possible orders of numbers in range 1-max_poly
def order(max_poly):
	a = [x for x in range(1, max_poly)]
	return itertools.permutations(a)

# Return true if the last x digits of num1 == first x digits of num2
def is_cycle(num1, num2, x):
	return str(num1)[x:] == str(num2)[:x]

"""
Cycle can start anywhere, so start looking with the triangular number.
Iterate through the orderings returned by order(6). This takes the forms of tuples
with digits in the range 1- 5, where 1 represents a square number and 5
represents an octagonal. This is the order the numbers come in the cyclic

The next number in the sequence is used to index polys, the list of all cyclic
numbers.

Check if this number ordering is cyclic. If yes, continue to next figurate

@triangle_start: Set of 4 digit triangle numbers
@return: There's only one cyclicate figurate. Return that when found or an empty
			list
"""
def check(triangle_start):
	# Iterate through the orderings of the square - octagonal numbers
	for a in order(6):
		for i in triangle_start:
			for j in polys[a[0]]:
				if is_cycle(i, j, 2):
					for k in polys[a[1]]:
						if is_cycle(j, k, 2):
							for l in polys[a[2]]:
								if is_cycle(k, l, 2):
									for m in polys[a[3]]:
										if is_cycle(l, m, 2):
											for n in polys[a[4]]:
												if is_cycle(m, n, 2):
													if is_cycle(n, i, 2):
														return([i, j, k, l, m, n])
	return []

"""
body
"""
answer = check(triangle)
end = time.time()
print("Problem Solution: {}".format(sum(answer)))
print("Problem Solved In {} seconds".format(end - start))
