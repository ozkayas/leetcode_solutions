class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = [(-freq, ch) for ch, freq in Counter(s).items()]
        heapq.heapify(maxHeap)
        # Init ans with the most freq char, and pop it from the heap
        f , ch = heapq.heappop(maxHeap)
        ans = [ch]
        if -f > 1:
            heapq.heappush(maxHeap, (f + 1, ch))

        while maxHeap:
            most = heapq.heappop(maxHeap)

            # If last != this, append
            if ans[-1] != most[1]:
                ans.append(most[1])
                if -most[0] - 1 > 0:
                    heapq.heappush(maxHeap, (most[0]+1, most[1]))
            elif maxHeap:
                secondMost = heapq.heappop(maxHeap)
                ans.append(secondMost[1])

                # Put most back in the heap
                heapq.heappush(maxHeap, most)
                if -secondMost[0] - 1 > 0:
                    heapq.heappush(maxHeap, (secondMost[0]+1,secondMost[1]))

            # Can not add the most freq and there is no char else, then quit
            else:
                break

        return "".join(ans) if len(s) == len(ans) else ""