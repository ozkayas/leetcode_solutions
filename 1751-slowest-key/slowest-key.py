class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        prevReleaseTime = 0
        # hold max value and key
        maxSoFar = (0,"")

        for i, time in enumerate(releaseTimes):
            duration = time - prevReleaseTime
            prevReleaseTime = time
            # print(f"duration: {duration}")
            # print(f"maxSoFar: {maxSoFar}")

            # We found a longer time with largest key
            if duration > maxSoFar[0]:
                maxSoFar = (duration, keysPressed[i])
            elif duration == maxSoFar[0] and keysPressed[i]> maxSoFar[1]:
                maxSoFar = (duration, keysPressed[i])



        return maxSoFar[1]




        