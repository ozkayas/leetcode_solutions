'''
https://www.fastprep.io/problems/amazon-find-encrypted-password
The developers at Amazon employ several algorithms for encrypting passwords. In one algorithm, the developers aim to encrypt palindromic passwords. Palindromic passwords are ones that read the same forward and backward.

The algorithm rearranges the characters to have the following characteristics:

It is a rearrangement of the original palindromic password.
It is also a palindrome.
Among all such palindromic rearrangements, it is the lexicographically smallest.
Given the original palindromic password that consists of lowercase English characters only, find the lexicographically smallest palindrome.

A string s is considered to be lexicographically smaller than the string t of the same length if the first character in s that differs from that in t is smaller. For example, "abcd" is lexicographically smaller than "abdc" but larger than "abad"

Note that the encrypted password might be the same as the original password if it is already lexicographically smallest.

Function Description

Complete the function findEncryptedPassword in the editor.

findEncryptedPassword has the following parameter:

string password: the original palindromic password
Returns

string: the encrypted password

Example 1:

Input:  password = "babab"
Output: "abbba" 
Explanation:

It can be rearranged to form abbba, which is both a rearrangement of the original password and the lexicographically smallest palindrome.

abbba satisfies all the requirements so we can boldly abbba. 
      
Example 2:

Input:  password = "yxxy"
Output: "xyyx" 
Explanation:

Rearrange the original password to form "xyyx", which is also a palindrome and is the smallest possible rearrangement.
  
      
Example 3:

Input:  password = "ded"
Output: "ded" 
Explanation:

Explanation not found..
  
      
Constraints:
1 ≤ |password| ≤ 105
password consists of lowercase English letters only.
password is a palindrome.

'''
from collections import Counter
    
password = "baxbxab"

freq = Counter(password)


ans_list = ["_" for i in range(len(password))]

#we have 2 pointers to fill in ans_list
l, r = 0, len(ans_list)-1
remainder_char = None
char = "a" # lets start with a and continue b,c,de...

#This while loop swipes all even appearing numbers, > 1
while len(freq) > 0:
    if char in freq:
        while freq[char] > 1:
            ans_list[l], ans_list[r] =  char, char
            freq[char] -= 2
            l += 1
            r -= 1
        # Clear this from hashmap
        if freq[char] == 0:
            del freq[char]
        # if 1, then this is the center of an odd palindrome, save it for later
        if freq[char] == 1:
            remainder_char = char
            del freq[char]
    # Next character, char++
    char = chr(ord(char) + 1)

# If a remainder_char detected, it should be inserted in the middle after loop execution
if remainder_char:
    ans_list[l] = remainder_char

print("".join(ans_list))
    




