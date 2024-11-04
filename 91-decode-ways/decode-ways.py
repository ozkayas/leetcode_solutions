class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def explore(s: str) -> int:
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

            return takeOne + takeTwo
        
        return explore(s)

        