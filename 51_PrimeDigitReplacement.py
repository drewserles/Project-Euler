"""
PROBLEM 51
By replacing the 1st digit of the 2-digit number *3, it turns out
that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest
prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
-----------------------------------------------------------------------------
OBSERVATIONS
1. In an eight prime value family the smallest value for the repeating digit
	must be either be 0, 1, or 2
2. If search through increasingly big primes, the smallest number in the
	solution family will be encountered first.
-----------------------------------------------------------------------------
STRATEGY
Start with the smallest prime with repetition (11). Increment the guess to
the next prime until a solution is found.
For each prime, check if there is a repeating digit. Construct a family of
numbers by replacing the repeating digits with larger digits.
Check if the family of numbers contains 8 primes. If yes, the smallest value
in the family is the solution.
"""
import timeit
from PrimeTest import is_prime
start = timeit.default_timer()

FAMILY_SIZE = 8

# Construct a family of numbers by replacing the digits at "locations" with
# all the larger digits up to 9. Check for primality of new numbers.
# Return: array of the numbers in the family that are prime
def families(prime, digit, locations):
	prime_copy = prime[:]
	family = [prime]
	# the number subtracted is based on how many family members required
	# if you want 7, subtract 3. 8:2 etc.
	while len(family) > digit - (10 - FAMILY_SIZE) and digit < 9:
		for n in locations:
			prime_copy = prime_copy[:n] + str(digit + 1) + prime_copy[n + 1:]
		# print(prime_copy)
		if is_prime(int(prime_copy)):
			family.append(prime_copy)
		prime = prime_copy[:]
		digit += 1
	return family

# Find the string index locations of the repeating digits in "num". Pass
# locations to families() to determine how many primes are in the family.
# Return: If there are 8 numbers in the family that are prime, return them.
#	Otherwise return False
def repeat_id(num):
	inter = str(num)
	for i in range(3):
		digit_count = inter.count(str(i))
		if digit_count > 1:
			locs = []
			for n in range(len(inter)):
				if inter[n] == str(i):
					locs.append(n)
			fam = families(inter, i, locs)
			# A solution was found
			if len(fam) == FAMILY_SIZE:
				return fam
	return False

# Increment a guess by 2. If it's prime, check for repeating digits and
# family primality. When a solution is found break out.
guess = 11
while 1:
	if is_prime(guess):
		num_fam = repeat_id(guess)
		# A solution was found
		if num_fam is not False:
			break
	guess += 2

end = timeit.default_timer()
print("Problem Solution: {}".format(min(num_fam)))
print("Problem Solved In {} seconds".format(end - start))