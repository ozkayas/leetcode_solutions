# Python3 program to sort an array
# of strings based on the given order
from functools import cmp_to_key

# For storing priority of each character
mp = {}

# Custom comparator function for sort
def comp(a, b):
	
	# Loop through the minimum size
	# between two words
	for i in range( min(len(a), len(b))):
		
		# Check if the characters
		# at position i are different,
		# then the word containing lower
		# valued character is smaller
		if (mp[a[i]] != mp[b[i]]):
			if mp[a[i]] < mp[b[i]]:
				return -1
			else: 
				return 1
	
	'''When loop breaks without returning, it
	means the prefix of both words were same
	till the execution of the loop.
	Now, the word with the smaller size will
	occur before in sorted order'''
	if (len(a) < len(b)):
		return -1
	else: 
		return 1

# Function to print the
# new sorted array of strings
def printSorted(words, order):
	
	# Mapping each character
	# to its occurrence position
	for i in range(len(order)):
		mp[order[i]] = i
	
	# Sorting with custom sort function
	words = sorted(words, key = cmp_to_key(comp))
	
	# Printing the sorted order of words
	for x in words:
		print(x, end = " ")

# Driver code
words = [ "word", "world", "row" ]
order = "worldabcefghijkmnpqstuvxyz"

printSorted(words, order)

# This code is contributed by Shivani
