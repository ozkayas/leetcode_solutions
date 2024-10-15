class Solution:
    def minimumSteps(self, s: str) -> int:
        onesOnLeft = []
        preFixSum = 0
        for ch in s:
            if ch == "1":
                preFixSum += 1
            onesOnLeft.append(preFixSum)

        # Count 1s for each 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += onesOnLeft[i]

        return ans
            










"""
# For each 0 , how many 1s on the left of it, so it will jump over them to the leftpart
101 -> from left: 00, 01, 11 continue, 10,swap and continue
l
011
  l 

0111
0101
 l
0011
  l

112222
101011 -> adj pointers
l    
011011
  l
010111
   l
"""