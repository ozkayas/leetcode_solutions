class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        ans = 0
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                if b_count > 0:
                    b_count -= 1
                    ans += 1
        return ans
            