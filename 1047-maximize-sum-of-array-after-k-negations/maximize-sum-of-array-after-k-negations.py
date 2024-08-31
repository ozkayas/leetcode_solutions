class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        minHeap = nums[:]
        heapq.heapify(minHeap)

        for i in range(k):
            cur = heapq.heappop(minHeap)
            if cur < 0:
                heapq.heappush(minHeap, -cur)
            elif cur == 0:
                break
            else:
                # print(f"{minHeap} - {cur} - i:{i}")
                heapq.heappush(minHeap, -cur)
                if (k-i) % 2 != 0:
                    break
                    
        return sum(minHeap)


"""
-4 -3 -1 2 4 5
 ^

"""
        