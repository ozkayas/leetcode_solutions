class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda i:i[1]) 
        
        chain = [pairs[0]]

        for pair in pairs[1:]:
            if pair[0] > chain[-1][1]:
                chain.append(pair)

        return len(chain)