class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        l , r = 0 , R*C-1

        while l <= r:
            mid = (l+r)//2

            # row and column coordinate of mid index
            row = mid // C
            col = mid % C

            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = mid -1
            else:
                l = mid +1
        
        return False