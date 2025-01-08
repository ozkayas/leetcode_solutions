class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        N = len(words)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                lenW1 = len(words[i])
                lenW2 = len(words[j])
                if lenW1 > lenW2:
                    continue
                
                if words[j][:lenW1] == words[i] and words[j][-lenW1:] == words[i]:
                    count += 1
        return count