class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(s: str) -> bool:
            # print(f"isPal ? {s}")
            return s == s[::-1]
        
        res = []
        
        def backT(s, sub):
            # print(f"s: {s}, sub: {sub}")
            N = len(s)
            if N == 0:
                # print("appending to res", sub)
                res.append(sub.copy())
                return

            for i in range(N):
                cur = s[0:i+1]
                if isPal(cur):
                    sub.append(cur)
                    remaining = s[i+1:]
                    backT(remaining, sub)
                    sub.pop()

        backT(s, [])
        return res
        