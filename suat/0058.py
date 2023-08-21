class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastIndex, firstIndex = 0, 0
        i = len(s)-1
        # find the last letter of the last word, set as LastIndex
        while s[i] == " ":
            i -= 1
        lastIndex = i

        # continue till the Oth index if on a letter
        while i > -1 and s[i] != " ":
            firstIndex = i
            i -= 1

        # lets see what we found
        lastWord = s[firstIndex:lastIndex+1]
        print(lastWord)

        return len(lastWord)