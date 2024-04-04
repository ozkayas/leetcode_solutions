class Solution:
    def maxDepth(self, s: str) -> int:
        o , c , ans = 0, 0, 0

        for char in s:
            if char == "(":
                o += 1
            elif char == ")":
                c += 1
        
            ans = max(ans, (o-c))
        return ans

'''
    o: 1 2.  3.    4
    c:     1   2 3   4 
       ( ( ) ( ) ) ( )
       1 2 1 2 1 0 1 0


    o: 1 2   3 4
    c:     1.    2 3 4
       ( ( ) ( ( ) ) ) - vps
       1 2 1 2 3 2 1 0


'''