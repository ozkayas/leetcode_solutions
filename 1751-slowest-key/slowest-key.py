class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = None # hold key;value as a tuple
        for i in range(len(keysPressed)):
            key = keysPressed[i]

            # Starting condition
            if i == 0:
                longest = (key, releaseTimes[i])
            else:
                thisVal = releaseTimes[i]-releaseTimes[i-1]
                #Found a longer value
                if thisVal > longest[1]:
                    longest = (key, thisVal)
                #Found equal, then check lexicograph. position
                elif thisVal == longest[1] and key > longest[0]:
                    longest = (key, thisVal)

        return longest[0]
        