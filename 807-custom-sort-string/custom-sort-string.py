class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        res = ''

        for ch in order:
            if ch in cnt:
                for i in range(cnt[ch]):
                    res += ch
                del cnt[ch]
        
        for ch in cnt:
            for i in range(cnt[ch]):
                res += ch
        
        return res
