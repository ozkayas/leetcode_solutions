class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        charSet = set()

        while r < len(s):
            charSet.add(s[r])
            # Valid window
            if len(charSet) == (r-l+1):
                r += 1
            else:
                charSet.remove(s[l])
                l +=1
            longest = max(longest, len(charSet))
        return longest

        