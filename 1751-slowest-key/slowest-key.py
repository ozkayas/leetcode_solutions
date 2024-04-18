class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = [releaseTimes[0],keysPressed[0]]

        for i in range(1,len(keysPressed)):
            cur_time = releaseTimes[i] - releaseTimes[i-1]
            cur_key = keysPressed[i]

            if cur_time > res[0]:
                res = [cur_time, cur_key]
            elif cur_time == res[0]:
                res = [cur_time, max(res[1],cur_key)]

        return res[1]