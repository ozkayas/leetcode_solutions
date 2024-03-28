class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sl = s.split(" ")
        if len(sl) != len(pattern): return False
        pSet = set()
        sSet = set()
        combiSet = set()
        
        for i in range(len(pattern)):
            pSet.add(pattern[i])
            sSet.add(sl[i])
            combiSet.add(pattern[i]+sl[i])
            if len(pSet) != len(sSet) or len(pSet) != len(combiSet):
                return False
        
        return True

        