class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        Data = namedtuple("Data", ["val","bucketId"])
        numOfBuckets = len(nums)
        # Sliding Window:
        # Validity of the window => len(bucketMapInWindow) == numOfBuckets


        # put all in a sorted list as tuples Data(val, bucketId)
        all = []
        for i in range(len(nums)):
            for n in nums[i]:
                all.append(Data(n,i))

        all.sort()

        # print(all)
        # buckets that exist in the current window
        bucketMap = defaultdict(int)
        minRange = [all[0], all[-1]]


        l, r = 0, 0
        while r < len(all):
            right = all[r]
            bucketMap[right.bucketId] += 1
            while len(bucketMap) >= numOfBuckets: # Found a valid window, process it, then shrink window
                left = all[l]
                # If a smaller range is found:
                if (right.val - left.val) < (minRange[1].val - minRange[0].val):
                    minRange = [left, right]
                # Process bucketMap    
                bucketMap[left.bucketId] -= 1
                if bucketMap[left.bucketId] == 0:
                    del bucketMap[left.bucketId] 

                l += 1
            r += 1
        return [minRange[1][0], minRange[0][0]]