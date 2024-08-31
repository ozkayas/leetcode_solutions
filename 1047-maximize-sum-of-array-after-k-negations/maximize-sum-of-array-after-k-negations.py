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
                heapq.heappush(minHeap, -cur)
                # print(f"{minHeap} - {cur}")
                # if i % 2 != 0:
                #     heapq.heappush(minHeap, -cur)
                # else:
                #     heapq.heappush(minHeap, cur)
        return sum(minHeap)


"""
-4 -3 -1 2 4 5
 ^

"""
        