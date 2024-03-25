class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        ans = []


        for n in nums:
            if n not in visited:
                visited.add(n)
            else:
                ans.append(n)

        return ans