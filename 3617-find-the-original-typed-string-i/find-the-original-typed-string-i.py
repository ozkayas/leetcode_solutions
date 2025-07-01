class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1 # flawless case
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                ans += 1
        return ans


'''
Input: word = "abbcccc"

flawless case: abbcccc, this is the right word
potentialflaws:
b: a b cccc -> 1 extra  (len(bWindow)-1)
c: a bb c / a bb cc / a bb ccc -> 3 extra (len(cWindow)-1)
Total = flawless case + 1 + 3 = 5
''' 