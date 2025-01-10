class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        letters = defaultdict(int)
        for word in words2:
            freq = Counter(word)
            for k,v in freq.items():
                if v > letters[k]:
                    letters[k] = v

        result = []
        for word in words1:
            freq = Counter(word)
            isSubset = True
            for k,v in letters.items():
                if v > freq[k]:
                    isSubset = False
                    break
            if isSubset:
                result.append(word)

        return result
                


        