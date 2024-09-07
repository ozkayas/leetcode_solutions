class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        matrix = [[0 for _ in range(N2)] for _ in range(N1)]
        maxSoFar = 0

        for i in range(N1):
            for j in range(N2):
                if nums1[i] == nums2[j]:
                    if i == 0 or j ==0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = matrix[i-1][j-1] +1
                maxSoFar = max(maxSoFar, matrix[i][j])
        
        return maxSoFar