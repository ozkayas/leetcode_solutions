class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Must put reversely. 9 before 5, 5 before 4,3,2... 
        # 34 before 3, 3 before 30
        def compare(a:int, b:int) -> int:
            # standard compare function -1 if a<b
            if a == b: return 0
            return -1 if str(a)+str(b) < str(b)+str(a) else 1

        nums.sort(key = cmp_to_key(compare), reverse = True)

        if nums[0] == 0: return "0"

        return "".join([str(n) for n in nums])
        