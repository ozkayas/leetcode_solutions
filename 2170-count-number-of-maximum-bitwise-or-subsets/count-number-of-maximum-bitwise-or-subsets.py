class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Calculate the maximum possible OR value
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Printing max_or for understanding
        print(f"Maximum possible OR value: {max_or}")

        ans = 0
        # Iterate over all possible subset lengths (from 1 to len(nums))
        for length in range(1, len(nums) + 1):
            for combi in itertools.combinations(nums, length):
                cur_or = 0
                for num in combi:
                    cur_or |= num
                if cur_or == max_or:
                    ans += 1

        return ans