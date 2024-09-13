"""
Amazon is working on a new hashing approach that takes in the original string and a seed number.

Engineers decided that the seed can be generated from the same input string by counting the number of times a reverse of a substring of length k makes the new string lexicographically smaller. You are deployed with the task of developing a service that takes in a string s and an integer k, and returns the number of ways to reverse any substring of length k such that the resulting string is lexicographically smaller than the original string.

Note:

1. A substring is a contiguous sequence of characters within a string. For example, the string "zon" is a substring of "amazon", "zone", etc.but is not a substring of "zoin", "zozo", etc.
2. A string a is lexicographically smaller than string b if a[i] < b[i] at the first index where a and b differ. For example, "amazon" is lexicographically smaller than "amozan".
Function Description:

1. Complete the function countNumWays in the editor.
2. countNumWays has the following parameters:
a. string s:the original string
b. int k:the algorithm parameter
Returns:

int: the number of possible ways to perform the operation ensuring the given constraint

Example 1:


Input:  s = "amazon", k = 3
Output: 1
Explanation:
Consider all substrings of length k = 3. There are the possible ways to perform the given operation are showing in the above img:
Example 2:

Input:  s = "ababa", k = 2
Output: 2
Explanation:


  There are the possible ways for k = 2:

  (1) ababa --> baaba: unsuccessful, lexicographically greater thanthe original string.
  (2) ababa --> aabba: successfully, lexicographically smaller than the original string.
  (3) ababa --> abbaa: unsuccessfully, lexicographically greater.
  (4) ababa --> abaab: successfully, lexicographically smaller.

"""

def countNumWays(s:str, k:int) -> int:
    N = len(s)
    counter = 0
    for i in range(0, N-k+1):
        if s[i:i+k][::-1] < s[i:i+k]:
            counter += 1
    return counter

print(countNumWays("amazon", 3)) # 1
print(countNumWays("ababa", 2)) # 2