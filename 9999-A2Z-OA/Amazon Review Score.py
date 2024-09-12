'''
https://www.fastprep.io/problems/amazon-review-score
Amazon allows customers to add reviews for the products they bought from their store. The review must follow Amazon's community guidelines in order to be published.

Suppose that Amazon has marked n strings that are prohibited in reviews. 
They assign a score to each review that denotes how well it follows the guidelines. 
The score of a review is defined as the longest contiguous substring of the review which does not contain any string among the list of words from the prohibited list, 
ignoring the case.

Given a review and a list of prohibited string, calculate the review score.

Function Description

Complete the function findReviewScore in the editor.

findReviewScore has the following parameters:

review: a string
string prohibitedWords[n]: the prohibited words
Returns

int: the score of the review
Example 1:

Input:  review = "GoodProductButScrapAfterWash", prohibitedWords = ["crap", "odpro"]
Output: 15 
Explanation:

Some of the substrings that do not contain a prohibited word are:
      
- ProductBut
      
- rapAfterWash
      
- dProductButScu
      
- Wash

The longest substring is "dProductButScra", return its length, 15.
Example 2:


Input:  review = "FastDeliveryOkayProduct", prohibitedWords = ["eryoka", "yo", "eli"]
Output: 11 
Explanation:

The substring "OkayProduct" is the longest substring which does not contain a prohibited word.

Its length is 11.
      
Example 3:

Input:  review = "ExtremeValueForMoney", prohibitedWords = ["tuper", "douche"]
Output: 20 
Explanation:

The review does not contain any prohibited word, so the longest substring is "ExtremeValueForMoney", length 20.
      
Constraints:
1 <= |review| <= 105
1 <= n <= 10
1 <= prohibitedWords[i] <= 10
review consists of English letters, both lowercase and uppercase
prohibitedWords[i] consists of lowercase English letters
'''
from typing import List
from collections import defaultdict

power = 31
MOD = 109001  # prime num
def hashFun(s:str) -> int:
    N = len(s)
    h = 0
    for i in range(N):
        digitValue = (ord(s[i]) * pow(power, N - i - 1, MOD)) % MOD
        h += digitValue
    return h % MOD


# Take the current hash and roll it
# b: char to be removed from hash, e: char to be added to the hash, n: length of pattern hashed
def rollHash(b: str, e: str, n: int, curHash: int) -> int:
    toRemoveValue = (ord(b) * pow(power, n - 1, MOD)) % MOD
    curHash = (curHash - toRemoveValue + MOD) % MOD
    curHash = (curHash * power) % MOD
    curHash = (curHash + ord(e) * pow(power, 0, MOD)) % MOD

    return curHash % MOD


# print(hashFun("abcd"))
# print(hashFun("bcde"))
# print(rollHash("a","e",4,hashFun("abcd")))

def findMaxSubarray(review: str, found: List) -> int:
    maxSub = 0
    starts = [0] + sorted([s for s, e in found])
    ends = sorted([e for s, e in found]) + [len(review)]

    for i in range(len(starts)):
        maxSub = max(maxSub, ends[i] - starts[i] - 1)

    return maxSub


def findReviewScore(review: str, prohibitedWords: List[str]) -> int:
    review = review.lower()
    # Holds starting indexes of prohibitedWord in review
    found = []

    for word in prohibitedWords:
        targetHash = hashFun(word)
        curHash = 0

        # search for word in review, in chunks of len(word)
        l, r = 0, len(word)
        while r < len(review):
            if l == 0:
                curHash = hashFun(review[l:r])
            else:
                curHash = rollHash(review[l - 1], review[r - 1], len(word), curHash)

            # This prohibited word is found in review in the range [l, r)
            if curHash == targetHash:
                found.append((l, r - 1))

            l += 1
            r += 1

    # Check for the longest substring
    return findMaxSubarray(review, found)


print(findReviewScore("GoodProductButScrapAfterWash", ["crap", "odpro"]))
print(findReviewScore("FastDeliveryOkayProduct", ["eryoka", "yo", "eli"]))
