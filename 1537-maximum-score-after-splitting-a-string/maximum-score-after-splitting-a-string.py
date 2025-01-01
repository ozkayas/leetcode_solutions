class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = -inf

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            
            print(f"best:{best}, zeros:{zeros}, ones:{ones}")
            best = max(best, zeros - ones)
            print(best)
            
        if s[-1] == "1":
            ones += 1
        
        return best + ones