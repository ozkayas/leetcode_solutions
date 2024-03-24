from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        sl = SortedList(nums)

        for n in nums:
            i = sl.bisect_left(n)
            res.append(i)
            sl.remove(n)


        return res


