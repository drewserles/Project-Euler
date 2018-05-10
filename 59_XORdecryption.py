"""
PROBLEM 59
https://projecteuler.net/problem=59
-----------------------------------------------------------------------------
OBSERVATIONS
-The key is 3 lowercase english characters. This means ascii codes 97 - 122
-The most common letter in english is e (ascii 101), and it's a good guess
that the most common character will be a space (ascii 32)
-An e XORed with a lower case letter produces a value between 0 - 31
-A space produces between 65 - 90
-----------------------------------------------------------------------------
STRATEGY
-Get a tally of all the ASCII codes in the raw data. The 3 highest values
in the range 0 - 31 were likely 'e' XORed with the 3 different chars in the
cipher
-These values were found to be [100, 103, 111]. Use trial and error to find the
correct ordering. Know it's correct when the output is readable text.
"""
import time
start = time.time()

# Read in encrypted text file
with open("p059_cipher.txt") as f:
	raw = f.read().replace('\n', '')
# Convert to a list of ints
raw = [int(x) for x in raw.split(',')]

# Each index of the array represents an int in the encrypted message
# Get a count of how many times each occurs
tally = [0]*95
for n in raw:
  tally[n] += 1

  # Return a list of the indices of the largest "l" numbers in "x"
def ind_lrg_nums(x, l):
  val = [0]*l
  ind = [0]*l
  for n in range(len(x)):
    for j in range(l):
      if x[n] > val[j]:
        for k in range(l-1, j, -1):
          ind[k], val[k] = ind[k-1], val[k-1]
        ind[j], val[j] = n, x[n]
        break
  return ind

# Get the top 3 values in the encrypted area that coujld be an e
key_val_enc = ind_lrg_nums(tally[0:32], 3)
# Xor these to get the key pair
key_vals = [n^101 for n in key_val_enc]
print(key_vals)
# Through trial and error find the correct ordering
my_key = [103, 111, 100]

# Take in list of integers, convert to ascii string
def int_to_char(x):
  new_str = ""
  for num in x:
    new_str += chr(num)
  return new_str

# XOR a list of ints with an encryption key (list of 3 ints)
def xor_list(source, key):
  key_len = len(key)
  for i in range(len(source)):
    key_idx = i % key_len
    source[i] = source[i] ^ key[key_idx]
  return source

# Unlock the message
xored = xor_list(raw, my_key)

# Print out the decrypted message for dramatic effect
print(int_to_char(xored))

# Answer
end = time.time()
print("Problem Solution: {}".format(sum(xored)))
print("Problem Solved In {} seconds".format(end - start))