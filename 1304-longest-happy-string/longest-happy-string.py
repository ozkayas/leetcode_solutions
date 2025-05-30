class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mxHeap = [] 
        for f, ch in zip([a,b,c],"abc"):
            if f: heapq.heappush(mxHeap, (-f, ch))

        ans = []
        while mxHeap:
            f, c = heapq.heappop(mxHeap)
            if ans[-2:] == [c,c]:
                if not mxHeap:
                    break
                # try the second most
                ff, cc = heapq.heappop(mxHeap)
                ans.append(cc)
                if -ff-1 > 0:
                    heapq.heappush(mxHeap, (ff+1, cc))

                # Put unused ch back in the heap
                heapq.heappush(mxHeap, (f,c))
            else:
                ans.append(c)
                if -f-1 > 0:
                    heapq.heappush(mxHeap, (f+1,c))

        return "".join(ans)