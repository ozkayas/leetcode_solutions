'''
Amazon games have introduced a new mathematical game for kids. You will be given n sticks and the player is required to form rectangles from those sticks.

Formally, given an array of n integers representing the lengths of the sticks, you are required to create rectangles using those sticks. Note that a particular stick can be used in at most one rectangle and in order to create a rectangle we must have exactly two pairs of sticks with the same lengths. For example, you can create a rectangle using sticks of lengths [2, 2, 5, 5] and [4, 4, 4, 4] but not with [3, 3, 5, 8]. The goal of the game is to maximize the total sum of areas of all the rectangles formed.

In order to make the game more interesting, we are allowed to reduce any integer by at most 1. Given the array sideLengths, representing the length of the sticks, find the maximum sum of areas of rectangles that can be formed such that each element of the array can be used as length or breadth of at most one rectangle and you are allowed to decrease any integer by at most 1. Since this number can be quite large, return the answer modulo 10^9+7.

Note: It is not a requirement that all side lengths be used. Also, a modulo b here represents the remainder obtained when an integer a is divided by an integer b.

Function Description

Complete the function getMaxTotalArea in the editor.

getMaxTotalArea has the following parameter(s):

int sideLengths[n]: the side lengths that can be used to form rectangles

Input:  sideLengths = [2, 6, 2, 6, 3, 5]
Output: 12 

Input:  sideLengths = [2, 3, 3, 4, 6, 8, 8, 6]
Output: 54 

Input:  sideLengths = [3, 4, 5, 5, 6]
Output: 20 

'''

s = [2, 6, 2, 6, 3, 5]
# Output = 12 

s = [2, 3, 3, 4, 6, 8, 8, 6]
# Output: 54 

s = [3, 4, 5, 5, 6]
# Output: 20 

total_area = 0
pairs = deque()
MOD = 10**9 + 7

# [2, 3, 3, 4, 6, 8, 8, 6]
# 8 8 6 6 4 3 3 2
# |
#     // next is same as cur - add cur to pairs and jump twice
#     // next is cur -1 - add cur-1 to pairs and jump twice
#     // else jump one step

# 8 6 3 2

s.sort(reverse = True)
i = 0
while i < len(s)-1:
    if s[i] == s[i+1]:
        pairs.append(s[i])
        i += 2
    elif s[i]-1 == s[i+1]:
        pairs.append(s[i]-1)
        i += 2
    else:
        i += 1


while len(pairs) > 1:
    a = pairs.popleft()
    b = pairs.popleft()
    total_area += (a*b) % MOD
    
print(total_area)