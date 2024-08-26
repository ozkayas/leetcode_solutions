class Solution:
    good_arrays = None
    current_pairs = None
    count = None

    # Helper method to collapse window and return the new left pointer
    def collapseWindow(self, curLeft:int, k:int, nums: List[int]) -> int:
        while self.current_pairs >= k:
            self.count[nums[curLeft]] -= 1
            self.current_pairs -= self.count[nums[curLeft]]
            curLeft += 1
        return curLeft


    def countGood(self, nums: List[int], k: int) -> int:
        self.good_arrays = 0
        self.current_pairs = 0
        self.count = defaultdict(int)

        l = 0
        # Start expanding the window
        for r in range(len(nums)):
            curr = nums[r]
            # If we have already seen this curr number, then it will increase pairs, 
            # if first time, defaultdict will just add 0
            self.current_pairs += self.count[curr]
            self.count[curr] += 1

            # Maybe we reached current_pairs >=k , if so start collapsing until not
            l = self.collapseWindow(l, k, nums)

            self.good_arrays += l
            print(f"good arrays {self.good_arrays}")

        return self.good_arrays
        