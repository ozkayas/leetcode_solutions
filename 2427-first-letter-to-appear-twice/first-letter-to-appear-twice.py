class Solution:
    def repeatedCharacter(self, s: str) -> str:
        setOfOccurance = set()

        for ch in s:
            if ch in setOfOccurance:
                return ch
            else:
                setOfOccurance.add(ch)
        