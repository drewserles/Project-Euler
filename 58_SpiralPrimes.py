"""
PROBLEM 58
https://projecteuler.net/problem=58
-----------------------------------------------------------------------------
OBSERVATIONS
-Starting with the centre (1) the next 4 on the diagonals, aka the corners
of the next layer are found by adding 2 to the current number. So 3, 5, 7, 9.
The next 4 are found by adding 4 to where we left off, giving 13, 17, 21, 15
etc.
-The question wants us to add a whole layer at once before checking the prime-
total ratio.
-Side length at the end is equal to the current add step + 1
-----------------------------------------------------------------------------
STRATEGY
Add the next 4 diagonal numbers at a time by keeping track of the last number
added. If the ratio goes below 0.1 then we're done. If not, increment the
step between numbers by 2 and repeat.
"""

from PrimeTest import is_prime
import time

start = time.time()

# Begin with the 1 at the centre
cur_num = 1
cur_add = 2
prime_cnt = 0
total_cnt = 1

while 1:
  # Add the whole next layer at once
  for _ in range(4):
    cur_num += cur_add
    if is_prime(cur_num):
      prime_cnt += 1
  total_cnt += 4
  
  # Check the ratio to see if we're done
  if (1.0 * prime_cnt / total_cnt) < 0.1:
    break
  
  # Increment number step size by 2 for the next layer
  cur_add += 2
  
end = time.time()
print("Problem Solution: {}".format(cur_add + 1))
print("Problem Solved In {} seconds".format(end - start))