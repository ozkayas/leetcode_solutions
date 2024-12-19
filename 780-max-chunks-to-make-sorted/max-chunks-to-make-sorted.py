class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx, count = 0 , 0
        for i in range(len(arr)):
            mx = max(mx,arr[i])
            if i == mx:
                count += 1

        return count

        