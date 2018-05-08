"""
PROBLEM 57
https://projecteuler.net/problem=57
-----------------------------------------------------------------------------
OBSERVATIONS

-----------------------------------------------------------------------------
STRATEGY
Brute force solution. Do the calculation for each expansion number on its own.
Compare the number of digits in the numerator and denominator to see which is
bigger
"""

import time
start = time.time()

# Return a tuble of the numerator and denominator (ints) after an expansion
# of size "iters"
def expand(iters):
  num = 1
  denom = 2
  for _ in range(iters - 1):
    num += 2*denom
    num, denom = denom, num
  num += denom
  return (num, denom)

"""
body - check expansion size 1 - 1000 and increment if numerator has more digits
than denominator
"""
count = 0
for num_exp in range(1, 1001):
  ratio = expand(num_exp)
  if len(str(ratio[0])) > len(str(ratio[1])):
    count += 1
    
end = time.time()
print("Problem Solution: {}".format(count))
print("Problem Solved In {} seconds".format(end - start))
