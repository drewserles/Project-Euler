"""
PROBLEM 63
https://projecteuler.net/problem=63
-----------------------------------------------------------------------------
OBSERVATIONS
-Power can be 1+ (no to the power of 0 because the base must be n digits as well)
-For base digits less than 10: once the power # has exceed the number of base
digits, the base count is never going to catch up to the power. Since you're
multiplying by less than 10, digits will lag behind power
-There are no solutions for a base >9. Every increase in the power digit causes
at least 1 extra digit in the base integer, so the number of digits can
never catch up to the power number if it's behind. 10^1 = 10 (2 digits), so
right from the beginning there are no solutions.
-----------------------------------------------------------------------------
STRATEGY
-Iterate through base numbers 1 - 10. For each one, beginning with an exponent
of 1, check if the number of digits in the number produced is equal to the
exponent. If yes, increment the total count of numbers found. If the exponent
is greater than the integer produced then it's time to stop and go to the next
base number.
"""
import time
start = time.time()

powerful_digit_count = 0
for base in range(1, 10):
    exp = 1
    while 1:
        digit_cnt = len(str(base**exp))
        if digit_cnt == exp:
            powerful_digit_count += 1
        elif digit_cnt < exp:
            break
        exp += 1

end = time.time()
print("Problem Solution: {}".format(powerful_digit_count))
print("Problem Solved In {} seconds".format(end - start))