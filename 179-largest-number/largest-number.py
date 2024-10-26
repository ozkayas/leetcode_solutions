class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a:int, b:int) -> int:
            if a == b: return 0
            return -1 if str(a)+str(b) < str(b)+str(a) else 1

        
        nums.sort(key = cmp_to_key(compare),reverse = True)
        # print(nums)
        if nums[0] == 0: return "0"

        return "".join([str(n) for n in nums])
        