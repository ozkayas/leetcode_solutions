class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        heapq.heapify(h)
        i = 0

        while i < len(heights)-1:
            curDif = heights[i+1] - heights[i]
            if curDif > 0:
                # print("Action: dif", curDif)
                if bricks >= curDif:  #try to user bricks GREEDY ly
                    bricks -= curDif
                    # h.append(curDif)
                    heapq.heappush(h,-1*curDif)
                    # h.sort()
                elif ladders > 0:  # bricks finished but still has ladders, time travel and swithch the biggest used gap 
                    if h and (-1 *h[0]) >= curDif:  # change ladder with a brick and remove this much brick
                        # bricks = bricks + h.pop()
                        # print("swap bricks for curDif", curDif)
                        bricks = bricks - heapq.heappop(h)
                        bricks -= curDif
                        heapq.heappush(h,-1*curDif)

                        # h.append(curDif)
                        # h.sort()
                    ladders -= 1
                else:
                    # print("returning i", i)
                    return i

            # print("end - heap:", h)
            # print("bricks remaining: ", bricks)
            i += 1

        return i
                


        