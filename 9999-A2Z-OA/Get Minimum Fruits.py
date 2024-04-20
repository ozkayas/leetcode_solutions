

'''
########################################################################################################
########## QUESTION: 4
########################################################################################################


In this game, you are allowed to choose two dissimilar fruits and crush them. Each type of fruit is represented as an integer in an array. Formally you can choose any two unequal integers in the array and delete them.

Given an array fruits of size n, return the minimum possible number of fruits left after the given operation is performed any number of times.

Examples:

n=5

fruits [3, 3, 1, 1, 2]

Fruits 1 (banana) and 2 (pineapple) can be crushed first, followed by numbers 1 (banana) and 3 (orange). Only 3 (orange) remains in the array, hence the answer is 1.

Function Description

Complete the function getMinimumFruits in the editor below.

getMinimumFruits has the following parameter(s):

int fruits[n]: array of n fruits

Returns:

int: the minimum possible count of fruits left

ex2: [1,3,5,6]

o/p2: 0

ex3: [2,2,2,5,1,2]

o/p3: 2
'''

# fruits = [3, 3, 1, 1, 2]
# fruits = [1,3,5,6]
fruits = [2,2,2,2,5,1,1,1,]

# en fazla frekanst olanlar ile en az frekansta olanlari crash etmek gerekiyor
from collections import Counter
freq = [list(item) for item in Counter(fruits).items()]
print(freq)

freq.sort(key = lambda i:i[1]) #Value gore sirala

# print(freq) -> [[3, 2], [1, 2], [2, 1]] burada 3 meyve var, 2 veya daha fazla meyve oldugu surece crash edecegiz iki bastan

while len(freq) > 1:
#     take 1 fruit from both ends and check to delete from list
    freq[0][1] -= 1
    freq[-1][1] -= 1
    
    if freq[0][1] == 0:
        freq.pop(0) # Actullay it is better to use a deque instead of a list here
    if freq[-1][1] == 0:
        freq.pop()
        
print(len(freq))
print(freq)

