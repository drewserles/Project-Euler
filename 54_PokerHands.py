"""
PROBLEM 54
https://projecteuler.net/problem=54
-----------------------------------------------------------------------------
OBSERVATIONS
-In each hand there is a clear winner. No ties
-----------------------------------------------------------------------------
STRATEGY
-Give each hands a ranking (10 for royal flush, 1 for high card)
-Add required information for tie break (ex. highest card for a straight)
-Compare scores for two hands and record who wins
"""

import time
start = time.time()

# Read in Hands file into list of strings
with open("p054_poker.txt") as f:
	content = f.readlines()
content = [x.strip() for x in content]
# Then turn each hand into a list of strings. Result is a 2D list
# where each entry is a list with 10 card entries.
splitset = [x.split() for x in content]

"""
Take in a list of 5 cards and return the best poker hand it makes.
-Convert cards to a numerical score (2 = 2, A = 14)
-Return a list where the first entry is a scored value for the hand
"""
def handID(hand):
	# Map cards to numerical value
	map = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
	# Make an ordered list of the hands numerical values
	ordered = sorted([map[n[0]] for n in hand], reverse=True)
	# Check the second index for each list entry. If they're all the same it's a flush
	if all(n[1] == hand[0][1] for n in hand):
		rf = ['A', 'K', 'Q', 'J', 'T']
		# ROYAL FLUSH - hand value 10
		if all(n[0] in rf for n in hand):
			return [10]
		# STRAIGHT FLUSH - hand value [9, high card]
		# 5 high straight flush - unique case where the Ace is low
		elif ordered[-1] == 2 and ordered[0] == 14 and all(ordered[n+1] == ordered[n] - 1 for n in range(1, 4)):
			return [9, 5]
		# Straight flush
		for n in range(4):
			if not ordered[n+1] == ordered[n] - 1:
				return [6, ordered[0]]
		return [9, ordered[0]]
	# STRAIGHTS - hand value [5, high card]
	# 5 high straight - Ace is low
	elif ordered[-1] == 2 and ordered[0] == 14 and all(ordered[n+1] == ordered[n] - 1 for n in range(1, 5)):
		return [5, 5]
	# Regular straight
	elif all(ordered[n+1] == ordered[n] - 1 for n in range(4)):
		return [5, ordered[0]]
	# PAIRS AND HIGH CARDS
	else:
		# Check if there's at least one pairing in the hand
		if any(ordered[i] in ordered[i+1:] for i in range(4)):
			# Figure out how many pairs are in the hand by making a count
			hand = 0
			for j in ordered:
				hand += ordered.count(j)
			# 1P - hand value [2, non paired cards]
			if hand == 7:
				ret = [2]
				# Find the location of the pair in the sorted hand so its
				# value and the high card value can be added to the return array
				for n in range(5):
					if ordered[n] == ordered[n+1]:
						ret.append(ordered[n])
						ret += ordered[:n]
						ret += ordered[n+2:]
						return ret
			# 2P - hand value [3, large pair, small pair, high card]
			elif hand == 9:
				ret = [3]
				new = []
				for n in range(5):
					if ordered[n] == ordered[n+1]:
							ret.append(ordered[n])
							new += ordered[:n]
							new += ordered[n+2:]
							for m in range(3):
								if new[m] == new[m+1]:
									ret.append(new[m])
									ret += new[:m]
									ret += new[m+2:]
									return ret

			# 3 OF A KIND - hand value [4, Triple, singles]
			elif hand == 11:
				ret = [4]
				for n in range(5):
					if ordered[n] == ordered[n+1]:
							ret.append(ordered[n])
							ret += ordered[:n]
							ret += ordered[n+3:]
							return ret
			# FULL HOUSE - hand value [7, 3 of kind, pair]
			elif hand == 13:
				ret = [7]
				ret.append(ordered[2])
				if ordered[0] != ordered[2]:
					ret.append(ordered[0])
				else:
					ret.append(ordered[4])
				return ret
			# 4 OF A KIND return [8, 4 of kind]
			else:
				ret = [8]
				if ordered[0] == ordered[1]:
					ret.append(ordered[0])
					ret.append(ordered[4])
				else:
					ret.append(ordered[1])
					ret.append(ordered[0])
				return ret

		# HIGH CARD HANDS - no pair, return [1, hands in card]
		else:
			return [1] + ordered

# Take in two poker hands as lists of card strings. Return True if the first
# hand is the winner and False if the second hand wins
def p1wins(hand1, hand2):
    list1 = handID(hand1)
    list2 = handID(hand2)
    # P1s hand type (ex flush) is better -> they win
    if list1[0] > list2[0]:
        return True
    elif list1[0] < list2[0]:
        return False
	# Hand types are the same. Look through high cards that make up rest of
	# the hand to find first difference
    else:
        for n in range(1, min(len(list1), len(list2))):
            if list1[n] > list2[n]:
                return True
            elif list1[n] < list2[n]:
                return False

"""
body - check all the hands and keep track of who wins
"""
p1_wins = 0
p2_wins = 0
for n in splitset:
    if p1wins(n[:5], n[5:]):
        p1_wins += 1
    else:
        p2_wins += 1

end = time.time()
print("Problem Solution: {}".format(p1_wins))
print("Problem Solved In {} seconds".format(end - start))
