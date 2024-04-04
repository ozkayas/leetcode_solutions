class Solution:
    def maxDepth(self, s: str) -> int:
        # if s == "()": return 1
        # if not s : return 0

        o , c , ans = 0 , 0, 0

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


      ( ) ( ( ) ) ( ( ( ) ) )
a:1   o                     c   
a:2       o               c   
a:3         o           c   
a:3               o c   
'''