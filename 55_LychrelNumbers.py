"""
PROBLEM 55
https://projecteuler.net/problem=55
-----------------------------------------------------------------------------
OBSERVATIONS
-Problem is asking us to find the numbers that don't become palindromes
in less than 50 iterations
-It does not count if the number is a palindrome to begin with. The clue says
4994 is a Lychrel number
-----------------------------------------------------------------------------
STRATEGY
-Function to determine if a number is a palindrome
-Function to iterate reverse add process. If it doesn't become a palindrome
after 50 iterations it's a Lychrel number
-Count # of Lychrels under 10 000
"""

import time
start = time.time()

# Return true if x is a palindrome
def is_palindrome(x):
	x_str = str(x)
	for i in range(len(x_str)//2):
		if x_str[i] != x_str[-1 - i]:
			return False
	return True

# Return the reverse of number x:
def reverse(x):
	str_x = str(x)
	rev_x = ""
	for i in range(len(str_x)):
		rev_x += str_x[-1 - i]
	return int(rev_x)

# Return true is x is a Lychrel number
def is_lychrel(x):
	iters = 1
	while iters < 50:
		x += reverse(x)
		if is_palindrome(x):
			return False
		iters += 1
	return True

"""
body
"""
lych_count = 0
for i in range(1, 10000):
	if is_lychrel(i):
		lych_count += 1

end = time.time()
print("Problem Solution: {}".format(lych_count))
print("Problem Solved In {} seconds".format(end - start))