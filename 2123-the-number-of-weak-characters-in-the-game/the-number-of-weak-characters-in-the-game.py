class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda i: (i[0], -i[1]))

        stack = []
        weaks = 0
        
        # this is told in the hints, we pop since this is a weak player and count
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                weaks += 1
            stack.append(d)
        return weaks 



        
"""
[5,5],[6,3],[3,6],[6,8],[5,7]

36
57
55
68
63

"""