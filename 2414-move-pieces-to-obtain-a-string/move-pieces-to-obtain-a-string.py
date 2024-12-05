class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s, t = 0, 0
        S = len(start)  # We only need one length variable since they must be equal

        while s < S or t < S:  # Changed to OR instead of AND
            while s < S and start[s] == "_":
                s += 1
            while t < S and target[t] == "_":
                t += 1

            # If one string exhausted, both strings should be exhausted
            if s == S or t == S:
                return s == S and t == S  # Simplified condition
               
            if (start[s] != target[t] or 
                (start[s] == "L" and s < t) or 
                (start[s] == "R" and s > t)):
                return False

            s += 1
            t += 1
        
        return True