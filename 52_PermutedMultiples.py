"""
PROBLEM 52
It can be seen that the number, 125874, and its double, 251748, contain exactly
 the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
-----------------------------------------------------------------------------
OBSERVATIONS
1. For x and 6x to contain the same digits, 6x can not have more digits than x.
	This means x < 1.667x10^n
-----------------------------------------------------------------------------
STRATEGY
Increment a guess starting at 1. Check if the 2x to 6x multiples have the same
digits as the guess. If yes we're done, if not continue.

Count up to the limit for the guess mentioned in Observation 1. When we've
reached that, set the guess to the beginning of the next order of magnitude
(ex. when 166 is reached, set guess to 1000). Calculate a new limit
"""

import time

start = time.time()

# Return true if 2x - 6x all contain the same digits
def check_multiples(x):
	two_x_sorted = sorted(str(2*x))
	for i in range(3, 7):
		i_x_sorted = sorted(str(i*x))
		if not (two_x_sorted == i_x_sorted):
			return False
	return True

"""
Return the maximum value the guess can be at order of magnitude "m"
as required by Observation 1.

max_guess(2) = 16
max_guess(3) = 166
"""
def max_guess(m):
	return (10**m) // 6

"""
Body
"""
guess = 1				# Number to check
mag = 1					# Order of magnitude used to calculate limit on guess
lim = max_guess(mag)		# Maximum value guess can take on in this range
while 1:
	if guess > lim:
		guess = 10**mag
		mag += 1
		lim = max_guess(mag)
	
	if check_multiples(guess):
		break
	
	guess += 1

end = time.time()
print("Problem Solution: {}".format(guess))
print("Problem Solved In {} seconds".format(end - start))