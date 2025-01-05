class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        diffArr = [0 for _ in range(N)]

        for shift in shifts:
            st = shift[0]
            e = shift[1]+1
            if shift[-1] == 1:
                diffArr[st] += 1
                if e < N:
                    diffArr[e] -= 1
            else:
                diffArr[st] -= 1
                if e < N:
                    diffArr[e] += 1

        def shiftChar(word, i, shift) -> str:
            cur = word[i]
            new = chr(ord("a") + (ord(cur)-ord("a")+shift)%26)
            word[i] = new


        word = list(s)
        shiftCount = 0
        for i,diff in enumerate(diffArr):
            shiftCount += diff
            shiftChar(word, i, shiftCount)

        return "".join(word)





'''

Approach: Difference Array
Intuition
Building on the idea of cumulative sums, we can use a difference array to handle range updates more efficiently. A difference array helps us record changes in values between consecutive elements rather than updating every element in a range directly.

Instead of keeping track of how many shifts should be applied to each character in the alphabet, we’ll use the difference array to store how many more shifts should be applied to the current character compared to the previous one. This allows us to record changes only at the starting and ending points of shifts, rather than updating each character in the range.

For convenience, a positive shift means that the character must move forward in the alphabet, and a negative shift means that it must move backward.
'''