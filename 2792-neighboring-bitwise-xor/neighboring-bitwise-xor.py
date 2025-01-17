class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = 0
        for d in derived:
            res ^= d
        return res == 0
            
        