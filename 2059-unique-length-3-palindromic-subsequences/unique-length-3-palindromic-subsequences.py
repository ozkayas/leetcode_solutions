class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first, last = [-1 for _ in range(26)],[-1 for _ in range(26)]
        def idx(ch:str) -> int:
            return ord(ch)-ord("a")

        def countBetween(st:int, end:int) -> int:
            if st == end: return 0
            count = 0
            for ch in set(s[st+1:end]):
                if first[idx(ch)] != -1: # if this char between a pair exists
                    count += 1
            return count

        for i,ch in enumerate(s):
            if first[idx(ch)] == -1:
                first[idx(ch)] = i
                last[idx(ch)] = i
            else:
                last[idx(ch)] = i

        totalCount = 0
        for i in range(26):
            totalCount += countBetween(first[i], last[i])
        return totalCount


'''
Let first be an array of length 26, where first[c] represents the first index the character c appears in s. Similarly, let last be an array of length 26, where last[c] represents the last index the character c appears in s. Because we need integer indices, we will map each character to its position in the alphabet.

'a' = 0.
'b' = 1.
...
'z' = 25.
We will calculate the arrays first and last prior to calculating the answer. To indicate if a letter appears in s at all, we will initialize first to have values of -1, which would be overridden if a letter appears in s.

To calculate first and last, we use a similar process from the previous approach. We iterate over s and for each s[i], if first[s[i]] = -1, we set first[s[i]] = i. We always set last[s[i]] = i.

Once we have first and last, we can iterate over each position in the alphabet i. We first check if this character appears in s at all, which we can do by checking if first[i] = -1. If i appears in s, we reference first[i] and last[i] to get the first and last indices.

We then perform the same process from the previous approach - declare a hash set between, iterate between the first and last indices, add each character to between, and finally add the length of between to our answer.

We repeat this process for each position i in the alphabet from 0 until 26.
'''