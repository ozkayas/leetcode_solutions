class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0
        ans = 0
        # charSet = set()

        while r < len(s):
            size = r - l + 1

            charSet = set(s[l:r+1])
            if len(charSet) == size:
                ans = max(ans, size)
                r += 1
            else:
                charSet.remove(s[l])
                l += 1
            

        return ans






        '''
        l, r = 0, 0
        ans = 0

        chars = set()

        while r < len(s):
            lenOfWindow =  r - l +1
            chars.add(s[r])

            if len(chars) == lenOfWindow:
                r += 1
            else:
                chars.remove(s[l])
                l += 1

            ans = max(ans, len(chars))



        return ans

'''