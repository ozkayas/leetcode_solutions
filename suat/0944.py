class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rowRange = len(strs[0])
        colRange = len(strs)
        count = 0

        for i in range(rowRange):
            for j in range (colRange-1):
                if (strs[j][i]) > (strs[j+1][i]):
                    count += 1
                    break

        return count
