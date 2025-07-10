'''
Imagine you're working with Amazon's data analysis team, specifically focusing on analyzing customer behavior through clickstream data. This data consists of sequences of user actions on the website, represented as binary strings. A '1' could represent a significant action (like adding an item to the cart of making a purchase), and a 'O' could represent a less significant action (like browsing or viewing a product).

You are given a binary string s that represents a user's interaction history. A behavior pattern (substring) is considered "special" if the number of insignificant actions ('O's) equals the square of the number of significant actions ('1's) within that pattern.

The challenge is to identify and count all "special" behavior patterns in the user's interaction history. These patterns might indicate critical points in the user's journey where their browsing behavior was well-balanced with key actions, which could be important for understanding user engagement or predicting future purchases.

Function Description

Complete the function countSpecialSubstrings in the editor.

countSpecialSubstrings has the following parameter:

String s: a binary string representing user interaction history
Returns

int: the count of special behavior patterns

Example 1:

Input: s = "010001"
Output: 4
Explanation:

s[0,1] ("01") and s[4,5] ("01") are special because they have 1 significant action ('1') and 1 insignificant
action ('0'), satisfying the condition cnto = cnt, * cnt.

s[0,5] ("010001") is special because it has 2 significant actions ('1') and 4 insignificant actions ('O), also
satisfying the condition cnto = cnt, * cnty.

s[1,2] ("10") is special as it has 1 significant action and 1 insignificant action.

In total, the string "010001" contains 4 special substrings, indicating balanced periods of interaction in the user's journey.

      
Example 2:

Input: s = "10010"
Output: 3
Explanation:

The special binary strings are s[0, 1] ("10"), s[2, 3]("01"), and s[3, 4]("10").

This test case was added on 06-13-2025. Relevant source image was included in the Problem Source section below.
'''
def countSpecialSubstrings(s: str) -> int:
    n = len(s)
    s_bits = [1 if ch == '1' else 0 for ch in s]
    result = 0

    # k_max: k^2 + k <= n koşulunu sağlayan en büyük k
    import math
    k_max = int((math.isqrt(4*n + 1) - 1) // 2)

    # Her k için kayar pencere
    for k in range(1, k_max + 1):
        L = k*k + k
        if L > n:
            break

        # İlk pencere
        curr = sum(s_bits[0:L])
        if curr == k:
            result += 1

        # Pencereyi kaydır
        for i in range(L, n):
            curr += s_bits[i]
            curr -= s_bits[i - L]
            if curr == k:
                result += 1

    return result



# TEST CASES
if __name__ == "__main__":
    assert countSpecialSubstrings("010001") == 4, "Test Case 1 Failed"
    assert countSpecialSubstrings("10010") == 3, "Test Case 2 Failed"
    assert countSpecialSubstrings("0000") == 0, "Test Case 3 Failed"  # hiç '1' olmadığından
    assert countSpecialSubstrings("111") == 0, "Test Case 4 Failed"  # hiç '0' olmadığından
    assert countSpecialSubstrings("1010001") == 6, "Test Case 5 Failed" 
    print("\n 😎 All test cases passed!")
