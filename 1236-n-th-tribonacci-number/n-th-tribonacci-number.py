class Solution:
    def tribonacci(self, n: int) -> int:        
        if n == 0: return 0
        if n <= 2: return 1
        tabular = [0 for _ in range(n+1)]
        tabular[0], tabular[1], tabular[2] = 0, 1, 1


        
        sumOfLastThree = 2

        for i in range(3,n+1):
            tabular[i] = sumOfLastThree
            sumOfLastThree += tabular[i]
            sumOfLastThree -= tabular[i-3]

        return tabular[n]  