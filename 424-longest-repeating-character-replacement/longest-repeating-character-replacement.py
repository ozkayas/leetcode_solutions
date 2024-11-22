class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxCharCount = 0
        maxWindow = 0

        l = r = 0
        def changableChars() -> int:
            windowLen = r - l + 1
            return windowLen - maxCharCount

        while r < len(s):
            freq[s[r]] += 1
            maxCharCount = max(maxCharCount, freq[s[r]])
            # expand window while changableChars <= k
            # else shrink it
            while changableChars() > k:
                freq[s[l]] -= 1
                l += 1

            maxWindow = max(maxWindow, (r-l+1))
            r += 1
        
        return maxWindow

        
        