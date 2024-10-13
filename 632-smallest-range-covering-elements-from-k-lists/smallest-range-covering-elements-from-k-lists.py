class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        numOfBuckets = len(nums)
        # Sliding Window:
        # Validity of the window => len(set) == len(window)

        # put all in a sorted list as tuples (value, bucketNo)
        all = []
        for i in range(len(nums)):
            for n in nums[i]:
                all.append((n,i))

        all.sort()
        # print(all)
        # buckets that exist in the current window
        bucketMap = defaultdict(int)
        minRange = [all[0], all[-1]]


        l, r = 0, 0
        while r < len(all):
            bucketMap[all[r][1]] += 1
            while len(bucketMap) >= numOfBuckets: # Found a valid window, process it, then shrink window
                # print((all[l][0] , all[r][0]))
                if (all[r][0] - all[l][0]) < (minRange[1][0] - minRange[0][0]):
                    minRange = [all[l], all[r]]
                bucketMap[all[l][1]] -= 1
                if bucketMap[all[l][1]] == 0:
                    del bucketMap[all[l][1]] 
                l += 1
            r += 1
        return [minRange[1][0], minRange[0][0]]
        