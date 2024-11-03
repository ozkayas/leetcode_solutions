class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = len(s1)
        S2 = len(s2)

        def canonical(s:str) -> tuple:
            arr = [0 for _ in range(26)]
            for ch in s:
                id = ord(ch) - ord("a")
                arr[id] += 1
            return tuple(arr)


        s1Canonical = canonical(s1)

        for i in range(S2-S1+1):
            sub = s2[i:i+S1]
            if s1Canonical == canonical(sub):
                return True

        return False



        