from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1

        def isAlone(i: int) -> bool:
            if i == 0 and nums[i] != nums[i + 1]:
                return True
            if i == len(nums) - 1 and nums[i] != nums[i - 1]:
                return True
            return nums[i] != nums[i - 1] and nums[i] != nums[i + 1]

        while l <= r:
            mid = l + (r - l) // 2

            if isAlone(mid):
                return nums[mid]

            # Eğer mid ve bir sonraki eleman aynıysa, tekil eleman sağda demektir
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 2
                else:
                    r = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
