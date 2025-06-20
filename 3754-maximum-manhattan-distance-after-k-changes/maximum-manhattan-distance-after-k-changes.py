class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x = y = 0
        max_dist = 0
        # For each step, we find the manhattan & manhattan + switching effect
        for i, ch in enumerate(s):
            if ch == "N":
                y += 1
            elif ch == "S":
                y -= 1
            elif ch == "E":
                x += 1
            elif ch == "W":
                x -= 1
            # At this step, you can change up to k moves so far
            max_dist = max(max_dist, min(i+1, abs(x) + abs(y) + k*2))
        return max_dist


'''
From the analysis in Approach 1, we can observe that the optimal strategy is to modify the less frequent letters in both directions whenever possible.

Therefore, if we treat the less frequent letters in both the vertical and horizontal directions as a single group, we can reason as follows:

If the total number of such letters is greater than k, then modifying any k of them increases the Manhattan distance by 2×k.
If the total number is less than or equal to k, then all the less frequent letters in both directions will be modified, and no further modifications are necessary. In this case, the Manhattan distance becomes equal to the length of the string.

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans
'''



        
        