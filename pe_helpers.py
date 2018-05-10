import math

# RETURN TRUE IF INPUT NUMBER IS PRIME
def is_prime(num):
	if num < 2:
		return False
	elif num < 4:
		return True
	elif num % 2 == 0:
		return False
	else:
		r = math.sqrt(num)
		f = 3
		while f <= r:
			if num % f == 0:
				return False
			f += 2
		return True
	
# RETURN A SIEVE OF ERATOSTHENES OF SIZE 'sieve_size" 
# IN THAT RANGE
def gen_sieve(sieve_size):
	sieve = [1]*sieve_size
	sieve[0] = 0
	sieve[1] = 0
	for i in range(sieve_size):
		if sieve[i]:
		# Remove all multiples of i in the sieve
			j = 2*i
			while j < sieve_size:
				sieve[j] = 0
				j += i
	return sieve