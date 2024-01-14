class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ctr1, ctr2 = Counter(word1), Counter(word2)
        return ctr1.keys() == ctr2.keys() and sorted(ctr1.values()) == sorted(ctr2.values())
        
        