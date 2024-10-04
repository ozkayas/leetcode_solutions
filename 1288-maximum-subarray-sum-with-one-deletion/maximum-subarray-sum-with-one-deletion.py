class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 1: return arr[0]

        forward, backward = [0] * N, [0] * N
        forward[0] = arr[0]
        backward[-1] = arr[-1]

        for i in range(1, N): 
            forward[i] = max(forward[i-1] + arr[i], arr[i])

        for i in range(N-2, -1, -1):
            backward[i] = max(backward[i+1] + arr[i], arr[i])

        max_no_deletion = max(forward)
        # calculate with skipping for each num
        max_one_deletion = -pow(10, 5)

        for i in range(1,N-1):
            max_cur_deleted = forward[i-1] + backward[i+1]
            max_one_deletion = max(max_one_deletion, max_cur_deleted)
        
        return max(max_no_deletion, max_one_deletion)



