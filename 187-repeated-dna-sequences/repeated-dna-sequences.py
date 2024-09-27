class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N, hMap =len(s), defaultdict(int)

        for i in range(0, N-9):
            hMap[s[i:i+10]] += 1
        
        ans = []
        for k, v in hMap.items():
            if v > 1:
                ans.append(k)
        return ans


        