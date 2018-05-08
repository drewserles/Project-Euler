"""
PROBLEM 56
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the 
maximum digital sum?
-----------------------------------------------------------------------------
OBSERVATIONS

-----------------------------------------------------------------------------
STRATEGY
Fairly straightforward to brute force this one. Test the combinations of
(a, b) values
"""

import time
start = time.time()

# Return the digit sum of x
def dig_sum(x):
	tot_sum = 0
	while x > 0:
		tot_sum += x % 10
		x //= 10
	return tot_sum

"""
body
"""
max_dig_sum = 0
for a in range(1, 100):
	for b in range(1, 100):
		new_val = dig_sum(a**b)
		if new_val > max_dig_sum:
			max_dig_sum = new_val
			
end = time.time()
print("Problem Solution: {}".format(max_dig_sum))
print("Problem Solved In {} seconds".format(end - start))