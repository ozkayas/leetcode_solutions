class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mxHeap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(mxHeap)
        ans = []

        while True:
            chFreq, ch = heapq.heappop(mxHeap)

            if chFreq == 0:
                break

            # Lets see if we can add this letter
            if len(ans) < 2 or not(ans[-1] == ch and ans[-2] == ch):
                ans.append(ch)
                # decrese freq and push to heap again, +1 because it s already negative
                heapq.heappush(mxHeap, (chFreq+1, ch))

            else:
                # try the second most
                secondMostFreq, secondCh = heapq.heappop(mxHeap)
                # If no second, not third also, just stop here
                if secondMostFreq == 0:
                    break
                
                ans.append(secondCh)

                # and most and second most back to heap
                heapq.heappush(mxHeap, (chFreq, ch))
                heapq.heappush(mxHeap, (secondMostFreq + 1, secondCh))


        return "".join(ans)
        