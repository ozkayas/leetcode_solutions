class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        preFixSum = 0
        for ch in s:
            if ch == "1":
                preFixSum += 1
            else:
                ans += preFixSum
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