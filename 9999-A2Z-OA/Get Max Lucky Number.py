'''
Amazon.com is distributing coupons in the form of a lottery system for loyal customers. The coupons are called "lucky numbers" and the customer with the largest lucky number gets the best discount. Devise a method to determine the maximum possible lucky number. A positive integer is a lucky number if its decimal representation contains only digits x and y. For example, if x=2 and y=5, then 2, 552, and 5225 are lucky numbers, and 3, 24, 57 and 389 are not.

For example, if x=2 and y=5, then 2, 552, and 5225 are lucky numbers, and 3, 24, 57 and 389 are not.

Given two different digits x and y and a positive integer n, determine the maximum possible lucky number, the sum of whose digits is n. It is guaranteed that at least one lucky number exists for the given x, y, and n.

Function Description

Complete the function getMaxLuckyNumber in the editor.

getMaxLuckyNumber has the following parameters:

x: an integer
y: an integer
n: the sum of the digits of the lucky number
Returns

int: the maximum possible lucky number

Example 1:

Input:  x = 3, y = 4, n = 13
Output: 4333 
Explanation:
If the two digits that make up the number are x = 3 and y = 4, and the sum of the digits must be n = 13, then the lucky numbers are:
3334
3343
3433
4333
The maximum lucky number is 4333.
'''

x = 3
y = 4 
n = 13

ans = []

def dfs(target, subset):
    if target < min(x,y):
        return
    if target == x:
        copy = subset[:]+[x]
        ans.append(copy)
        # print(copy, ans)
        return
    if target == y:
        
        copy = subset[:]+[y]
        ans.append(copy)
        # print(copy, ans)
        return
    
    subset.append(x)
    dfs(target-x, subset)
    subset.pop()
    subset.append(y)
    dfs(target-y, subset)
    subset.pop()
    
dfs(n, [])
# print(ans)

ans_numbers = []
for subset in ans:
    s = [str(i) for i in subset]
    st = "".join(s)
    ans_numbers.append(int(st))
print(ans_numbers)
print("RESULT: ", max(ans_numbers))