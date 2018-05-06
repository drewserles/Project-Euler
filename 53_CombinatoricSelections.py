"""
PROBLEM 53
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.

It is not until n = 23 that a value of nCr exceeds 1 million.
23C10 = 1,144,066
How many, not necessarily distinct values of nCr for 1 <= n <= 100 are
greater than 1 million?
-----------------------------------------------------------------------------
OBSERVATIONS
1. The largest value of nCr occurs for r = n/2 when n is even, or round(n/2)
and round(n/2) + 1 if n is odd
2. The number of combinations decreases as r gets bigger/smaller away from this
	middle value
3. Looking at range n = [1, 100] but first number of combinations more than
	a million occurs at n = 23, so we can start there.
-----------------------------------------------------------------------------
STRATEGY
-Know that the largest r will be over a million for all n >= 23. decrease r
until it's not greater than 1 million, then return number of combinations found
x 2
"""

import time
import math

start = time.time()

# Return number of combinations
def combinations(n, r):
	f = math.factorial
	return f(n) // (f(r) * f(n - r))

# Return the number of values of nCr there are over 1,000,000 
def c_over_million(n):
	r = n//2
	if combinations(n, r) < 1000000:
		return 0
	
	if n % 2 == 0:
		count = 1
	else:
		count = 2
	
	while r > 0:
		r -= 1
		if combinations(n, r) > 1000000:
			count += 2
		else:
			break
	return count

# Body
mill_count = 0
for i in range(23, 101):
	mill_count += c_over_million(i)

end = time.time()
print("Problem Solution: {}".format(mill_count))
print("Problem Solved In {} seconds".format(end - start))