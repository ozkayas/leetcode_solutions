"""
Amazon is developing a string matching library. You are to develop a service that finds the longest substring that matches a given regex.

More formally, you are given two strings, a text string text, and a regex expression regex. The string regex contains exactly one wildcard character(*). A wildcard character (*) matches any sequence of zero or more lowercase English characters. A regex matches some string if it is possible to replace the wildcard character with some sequence of characters such that the regex expression becomes equal to the string. No other character can be changed. For example, regex "abc*bcd" matches "abcbcd", "abcefgbcd" and "abccbcd", whereas it does not match the strings "abcbd", "abzbcd", "abcd".

Return the length of the longest substring of text that matches the expression regex. Return -1 if there is no such substring.

Note: A substring is a contiguous sequence of characters within a string.

Function Description

Complete the function getLongestMatch in the editor below.

getLongestMatch has the following parameters:

1. STRING text: a string
2. STRING regex: a string
Returns

int: the length of the longest substring that matches the regex, or -1 if there is no such substring.

𓍢ִ໋🌷͙֒ 🌿 Credit to Jane and txr 🌿 𓍢ִ໋🌷͙֒

Example 1:

Input:  text = "hackerrank", regex = "ack*r"
Output: 6
Explanation:

The following substrings match regex:
"acker", we can replace * with "e" and regex becomes equal to "acker". length = 5

"ackerr", we can replace * with "er" and regex becomes equal to "ackerr". length = 6


Return the length of the longest matching substring, 6.
Example 2:

Input:  text = "programming", regex = "r*in"
Output: 9
Explanation:

"rammin", len = 6. We can replace * with "amm"

"rogrammin" len = 9. We can replace * with "ogramm"
Example 3:

Input:  text = "debug", regex = "ug*eb"
Output: -1
Explanation:

No substring of text begins with 'u' and ends with 'eb'
Constraints:
1 <= |text|, |regex| <= 106
text contains lowercase English letters only
regex contains lowercase English letters and exactly one wildcard(*) characterj
"""
from typing import List
def getLongestMatch(s:str, p:str) -> int:

    power = 31
    MOD = 109001  # prime num
    def hashFun(s:str) -> int:
        N = len(s)
        h = 0
        for i in range(N):
            digitValue = (ord(s[i])*pow(power, N-i-1,MOD)) % MOD
            h += digitValue
        return h % MOD

    # Take the current hash and roll it
    # b: char to be removed from hash, e: char to be added to the hash, n: length of pattern hashed
    def rollHash(b:str, e:str, n:int, curHash:int) -> int:
        # print("removing {}, adding {}".format(b,e))
        toRemoveValue = (ord(b) * pow(power, n-1, MOD)) % MOD
        curHash = (curHash - toRemoveValue + MOD) % MOD
        curHash = (curHash * power) % MOD
        curHash = (curHash + ord(e)*pow(power, 0, MOD)) % MOD

        return curHash % MOD


    prefix, suffix = p.split("*")
    N = len(prefix)
    #Find the first index in s where p exists
    prefixHash = hashFun(prefix)
    subHash = 0
    # Init subHash for first n letters of s
    i = 0
    for i in range(len(s)-N+1):
        if i == 0:
            subHash = hashFun(s[i:N])
        else: 
            subHash = rollHash(s[i-1], s[i+N-1], N, subHash)
        
        if subHash == prefixHash:
            break

    print('found i',i, s[i:i+N])

    # Find the last index in s where suffix exists, 
    # Doing the same operations in reverse orders
    N = len(suffix)
    suffixHash = hashFun("".join(reversed(suffix)))
    subHash = 0
    for j in range(len(s)-1, N -1, -1):
        if j == len(s)-1:
            subHash = hashFun("".join(reversed(s[len(s)-N:len(s)]))) 
        else:
            subHash = rollHash(s[j+1], s[j-N+1], N, subHash)
        
        if subHash == suffixHash:
            break

    print('found j',j, s[j-N:j])

    if i > j:
        return -1

    return j-i+1

print(getLongestMatch("hackerrank",  "ack*r"))
print(getLongestMatch("programming",  "r*in"))
print(getLongestMatch("debug",  "ug*eb"))