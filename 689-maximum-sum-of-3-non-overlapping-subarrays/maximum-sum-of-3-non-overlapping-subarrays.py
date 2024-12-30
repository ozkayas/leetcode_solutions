class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # preprocessing
        k_sums = [sum(nums[:k])]

        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] + nums[i] - nums[i-k])

        @cache
        def get_max_sum(i, cnt):
            if cnt == 3 or i > len(nums)-k:
                return 0
            # Include
            include = k_sums[i] + get_max_sum(i+k, cnt + 1)
            # Skip
            skip = get_max_sum(i+1, cnt)

            return max(include, skip)

        def get_indices():
            i = 0
            indices = []
            while i <= len(nums)-k and len(indices) < 3:
                include = k_sums[i] + get_max_sum(i+k, len(indices)+1)
                skip = get_max_sum(i+1, len(indices))
                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1
            return indices

        return get_indices()


        