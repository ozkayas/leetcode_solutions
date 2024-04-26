class Solution:
    def repeatedCharacter(self, s: str) -> str:
        occuranceList = [0 for _ in range(26)]

        for i in range(len(s)):
            charIndex = ord(s[i]) - ord("a")
            if occuranceList[charIndex] == 1:
                return s[i]
            else:
                occuranceList[charIndex] = 1
        