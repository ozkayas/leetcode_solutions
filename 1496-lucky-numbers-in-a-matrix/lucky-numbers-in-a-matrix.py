class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        rowMin = [10**5 for _ in range(m)]
        colMax = [0 for _ in range(n)]

        for i in range(m):
            rowMin[i] = min(matrix[i])
            for j in range(n):
                colMax[j] = max(colMax[j], matrix[i][j])

        # print(rowMin)
        # print(colMax)
        luckyNums = []

        for i in range(m):
            for j in range(n):
                cur = matrix[i][j]
                if cur == rowMin[i] and rowMin[i] == colMax[j]:
                    luckyNums.append(cur)

        return luckyNums

        