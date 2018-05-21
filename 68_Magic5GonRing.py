"""
PROBLEM 68
https://projecteuler.net/problem=68
-----------------------------------------------------------------------------
OBSERVATIONS
-Maximum value occurs when the 5 biggest digits are in the centre pentagon,
minimum when it's the smallest 5. The max and min give an allowable range for
the values an arm can take on
-Starting with the smallest external node and moving clockwise, each external
node after that must be larger
-
-----------------------------------------------------------------------------
STRATEGY
-Iterate through possible digit combinations for first arm for a given sum
-All middle arms after that have 3 known pieces of information: 2nd digit is
the final digit from the previous arm, the first digit must be larger than
the original arms first digit, and no numbers can repeat
-Final arm has nothing to calculate - just use the last number.
-For each arm sum from min to max, check the possible starting arm permutations.
For each starting arm, check the permutations for the successive arms until
a contradiction/violation is found. If we get to the end (final arm) then a 
valid solution has been found
-At the end, find the largest 16 digit valid solution
"""

import time
start = time.time()

arm_cnt = 5
max_digit = arm_cnt * 2
digits = [x for x in range(1, max_digit + 1)]
min_arm_sum = ( sum(digits[arm_cnt:]) + 2*(sum(digits[:arm_cnt])) ) // arm_cnt
max_arm_sum = ( sum(digits[:arm_cnt]) + 2*(sum(digits[arm_cnt:])) ) // arm_cnt

# Takes in a value n and determine all the ways it can be split into 2 numbers. Order matters
def pair_combs(r, a):
	pairs = []
	for n1 in range(1, r):
		n2 = r - n1
		if n1 != n2 and n1 != a and n2 != a and n1 <= max_digit and n2 <= max_digit:
			pairs.append([a, n1, n2])
	return pairs

# Take in the existing numbers used and the 3 new numbers. Return true if it's a feasible new arm
# n1 and n3 are new
def valid_arm(used_nums, n1, n3):
	if n1 == n3:
		return False
	if n1 in used_nums or n3 in used_nums:
		return False
	if n1 < 1 or n3 < 1:
		return False
	if n1 > max_digit or n3 > max_digit:
		return False
	return True

# Take in a sum that the arm should total to and generate all possibilities
# This is the arm with the smallest outer node of all the arms (leading branch)
def gen_min_arm(n):
	arm_triplets = []
	# Iterate from 1 to the max the number can be. Max comes from arm needing to be the smallest in the ring (at least arms - 1 bigger values)
	for a in range(1, max_digit - arm_cnt + 2):
		remain_sum = n - a
		arm_triplets += pair_combs(remain_sum, a)
	return arm_triplets

# For the next arm in the array, we already have the middle digit (dig 3 in previous arm) -> so we can iterate possibilities for the outer node and then the smallest is calculated
# n is a list of lists. 2nd D list are valid arms so far (clockwise)
def gen_next_arm(arm_sum, prev_arms):
	solutions = []

	for n in prev_arms:
	# Work on the second arm, starting with the outside node (which must be larger than the initial outside node)
		for b1 in range(n[0] + 1, max_digit + 1):
			b2 = n[-1]
			b3 = arm_sum - b1 - b2
			if valid_arm(n, b1, b3):
				solutions.append(n + [b1, b2, b3])
	return solutions

# Add the final arm in the ring. This one is calculated because there's only one number left and 2/3 of the arm are in place
def gen_final_arm(arm_sum, prev_arms):
	solutions = []
	for n in prev_arms:
		# Final arm uses 2nd digit from first arm and final digit from previous arm
		c1 = arm_sum - n[1] - n[-1]
		if c1 not in n and c1 > 0 and c1 <= max_digit and c1 > n[0]:
			solutions.append(n + [c1, n[-1], n[1]])
	return solutions

# Generate the possible solutions
solutions = []
for N in range(min_arm_sum, max_arm_sum + 1):	
	# Starting arm
	arms_arr = gen_min_arm(N)
	# Middle arms
	for _ in range(arm_cnt - 2):
		arms_arr = gen_next_arm(N, arms_arr)
	# Final arm
	arms_arr = gen_final_arm(N, arms_arr)
	solutions += arms_arr
	
# Find the 16 digit solutions
max_vals = []
for n in solutions:
	val = ""
	for x in n:
		val += str(x)
	if len(val) == 16:
		max_vals.append(int(val))


end = time.time()
print("Problem Solution: {}".format(max(max_vals)))
print("Problem Solved In {} seconds".format(end - start))