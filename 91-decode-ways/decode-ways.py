class Solution:
    def numDecodings(self, s: str) -> int:
        memo = dict()

        def explore(s: str) -> int:
            if s in memo:
                return memo[s]
            if s == "":
                return 1
            if s[0] == "0":
                return 0
            takeOne = takeTwo = 0
            # Take first char
            takeOne = explore(s[1:])

            # Take 2 digits if possible
            if len(s) >= 2 and int(s[:2]) <= 26:
                takeTwo = explore(s[2:])

            memo[s] = takeOne + takeTwo

            return memo[s]
        
        return explore(s)

        