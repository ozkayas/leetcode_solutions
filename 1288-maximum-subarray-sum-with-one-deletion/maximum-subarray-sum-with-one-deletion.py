class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # If there is only 1 element, we can not delete anything and no subarray, just return it
        if len(arr) == 1: return arr[0]

        # explanation https://www.youtube.com/watch?v=AxkYOnS-hjs
        # Kadane's algo from both sides
        N = len(arr)
        max_left, max_right = [], []

        # Fill max_left
        max_so_far = float("-inf")
        for n in arr:
            max_so_far = max(max_so_far + n, n)
            max_left.append(max_so_far)
        # print(max_left)

        # Fill max_right
        max_so_far = float("-inf")
        for n in reversed(arr):
            max_so_far = max(max_so_far + n, n)
            max_right.append(max_so_far)
        max_right.reverse()
        # print(max_right)

        # Look for negatives and check what happens if we delete it. by looking leftpart and rightpart 
        max_after_deletion = float("-inf")
        for i,n in enumerate(arr):
            if n < 0:
                left_part_max = max_left[i-1] if (i-1) >= 0 else 0
                right_part_max = max_right[i+1] if (i+1) < N else 0
                max_after_deletion = max(max_after_deletion, left_part_max + right_part_max)


        max_of_sub_without_deletion = max(max_right)
        return max(max_after_deletion, max_of_sub_without_deletion)
            


            


        