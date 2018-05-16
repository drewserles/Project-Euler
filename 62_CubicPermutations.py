"""
PROBLEM 62
https://projecteuler.net/problem=62
-----------------------------------------------------------------------------
OBSERVATIONS
-If we generate all the cube numbers between 1 and N, and iterate through them,
the solution to our question will be encountered first, and the other 4
permutations of this number will be later in the list
-----------------------------------------------------------------------------
STRATEGY
-
"""

import time
start = time.time()

# Return True if num is a perfect cube
def perfect_cube(num):
    return round(num**(1./3))**3 == num

# Generate cubed number up to n = 10,000
cubes = [x**3 for x in range(101, 10000)]

# Return True if num1 and num2 have all the same digits (permutations)
def is_perm(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    return len(str_num1) == len(str_num2) and sorted(str_num1) == sorted(str_num2)

"""
Take in a cubed number and its position in the cube list. Check the numbers
later in the list. If one is a permutation of "num" add it to family list.
Continue this until we're checking numbers that have more digits (can't be
permutations)
"""
def perm_count(num, pos):
	max_num = 10**len(str(num))
	family = [num]
	for n in cubes[pos + 1:]:
		if n > max_num:
			break
		if is_perm(num, n):
			family.append(n)
	return family

# find family cubes with "number" of cubed permutations. Return the list of the
# group of cubes. It will be in order so the answer we're looking for is at index
# 0
def find_fam(number):
	for n in range(len(cubes)):
		res = perm_count(cubes[n], n)
		if len(res) == number:
			return res
	return [0]
		
"""
answer
"""
solution = find_fam(5)
end = time.time()
print("Problem Solution: {}".format(solution[0]))
print("Problem Solved In {} seconds".format(end - start))


