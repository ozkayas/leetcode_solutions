class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Returns the next nonHash, may also return the given index if it is already valid
        def nextNonHashPos(i, word):
            skip = 0
            while i >= 0 and (word[i] == '#' or skip > 0):
                if word[i] == '#':
                    skip += 1
                else:
                    skip -= 1
                i -= 1
            return i

        s_pt, t_pt = len(s) - 1, len(t) - 1

        while s_pt >= 0 and t_pt >= 0:
            s_pt = nextNonHashPos(s_pt, s)
            t_pt = nextNonHashPos(t_pt, t)

            # If there is no char to compare, just quit
            if s_pt < 0 or t_pt < 0:
                break
            
            # If next chars do not match, just return False
            if s[s_pt] != t[t_pt]:
                return False
            # next chars after backspace deleting matches, so shift index for the following left
            # part of the strings
            else:
                s_pt -= 1
                t_pt -= 1

        if nextNonHashPos(s_pt, s) >= 0 or nextNonHashPos(t_pt, t) >= 0:
            return False
        else:
            return True