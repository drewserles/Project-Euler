"""
PROBLEM 60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
-----------------------------------------------------------------------------
OBSERVATIONS
-Concatenating two numbers and checking if the result is prime is very slow
better option is to create a sieve of eratosthenes and then check the index
of the new concat number
-Want to arbitrarily try checking primes up to 10,000 so that means we need
a sieve of size 100,000,000
-----------------------------------------------------------------------------
STRATEGY
-Generate a sieve and primes up to 10,000
-For each prime, check the primes after it to see if they concatenate to a prime
if no continue on, but if yes check a 3rd, starting at the first prime after
the 2nd
-The newest number only needs to be checked with the existing numbers since
they've already been shown to concat with each other
-Follow this 5 numbers deep. Keep track of any sets of 5 that work, then at the
end find the smallest sum
"""
import time
from pe_helpers import gen_sieve
start = time.time()

# Create a sieve up to a 100M. Generate a list of primes up to 10k
sieve = gen_sieve(100000000)
primes = []
for i in range(2, 10000):
	if sieve[i]:
		primes.append(i)

prime_size = len(primes)


# Concatenate two numbers - Returns 1 if both orderings are prime
def CatPrime(num1, num2):
  ord1 = int(str(num1)+str(num2))
  ord2 = int(str(num2)+str(num1))
  return sieve[ord1] and sieve[ord2]

# Check all possible concats of a list of primes
def PermCatPrime(p, p_list):
  for r in p_list:
    if not CatPrime(r, p):
      return False
  return True

"""
body
"""

solutions = []
    
# Work
# Note - as you continue on, you know the previous numbers all work together, so you
# just need to check the new one
for i1 in range(prime_size):
  p1 = primes[i1]
  for i2 in range(i1+1, prime_size):
    p2 = primes[i2]
    if PermCatPrime(p2, [p1]):
      for i3 in range(i2+1, prime_size):
        p3 = primes[i3]
        if PermCatPrime(p3, [p1, p2]):
          for i4 in range(i3+1, prime_size):
            p4 = primes[i4]
            if PermCatPrime(p4, [p1, p2, p3]):
              for i5 in range(i4+1, prime_size):
                p5 = primes[i5]
                if PermCatPrime(p5, [p1, p2, p3, p4]):
                  solutions.append([p1, p2, p3, p4, p5])

solutions = [sum(n) for n in solutions]
best_sol = min(solutions)
# Answer
end = time.time()
print("Problem Solution: {}".format(best_sol))
print("Problem Solved In {} seconds".format(end - start))

