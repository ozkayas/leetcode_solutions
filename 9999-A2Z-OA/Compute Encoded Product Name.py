'''
Amazon's software team utilizes several algorithms to maintain data integrity, one of which targets the encoding of symmetrical names. Symmetrical names are unique in that they read identically in both directions, similar to palindromes in language parlance.

The chief aim of the algorithm is to rearrange the characters in the original symmetrical name according to these criteria:

The rearranged name is a reshuffled version of the original symmetrical name.
The restructured name should be symmetrical as well.
This restructured name should be lexicographically smallest among all its symmetric permutations.
Given an initial symmetrical name that contains only lowercase English characters, compute the encoded name.

A string is considered to be lexicographically smaller than the string t of the same length if the first character in s that differs from that in t is smaller. For example, "abcd" is lexicographically smaller than "abdc" but larger than "abaa".

Note that the output encoded name could match the original name if it's already the smallest lexicographically.

Function Description

Complete the function computeEncodedProductName in the editor.

computeEncodedProductName has the following parameter:

string nameString: the initial symmetrical string name.
Returns

string: the encoded nameString

Example 1:

Input:  nameString = "yxxy"
Output: "xyyx" 
Explanation:

      

      Rearrange the original nameString to generate "xyyx",
      which is a palindrome and also the smallest possible.
      


      
Example 2:

Input:  nameString = "ded"
Output: "ded" 
Explanation:

      

      The original nameString "ded" is already the smallest lexicographical palindrome possible, so it remains unchanged.'''
from collections import Counter
from typing import List

class Solution:

    def fillPalindromeFromSortedFreqs(self, n: int, freqs: List[dict[str,int]]) -> List[str]:
        lonelyChar = ""

        dummyList = ["" for _ in range(n)]
        l, r = 0, n-1
        for ch, val in freqs:
            if val %2 != 0:
                lonelyChar = ch
                continue
            else:
                while val > 0:
                    val -= 2
                    dummyList[l] = ch
                    dummyList[r] = ch
                    l += 1
                    r -= 1
        if lonelyChar != "":
            dummyList[l] = lonelyChar
        return dummyList




    def computeEncodedProductName(self, nameString: str) -> str:
        freq = Counter(nameString)
        sortedFreqs = sorted(list(freq.items()))

        print(sortedFreqs)

        return "".join(self.fillPalindromeFromSortedFreqs(len(nameString), sortedFreqs))


print("RESULT", Solution().computeEncodedProductName("bbaxabb"))
print("RESULT", Solution().computeEncodedProductName("yxxy"))
