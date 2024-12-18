from collections import Counter, namedtuple
import heapq

class Solution:
    Char = namedtuple("Char", ["ord","val","freq"])
    
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        maxHeap = []
        for ch, f in freq.items():
            order = ord(ch)-ord("a")
            maxHeap.append(Solution.Char(-order, ch, f))
        heapq.heapify(maxHeap)

        output = []
        while maxHeap:
            cur = heapq.heappop(maxHeap)
            used = 0
            while used < cur.freq:
                output.append(cur.val)
                used += 1
                if used == repeatLimit and used < cur.freq:  # Check if we still have chars to use
                    if not maxHeap:
                        break
                    nextChar = heapq.heappop(maxHeap)
                    output.append(nextChar.val)
                    if nextChar.freq > 1:
                        heapq.heappush(maxHeap, Solution.Char(nextChar.ord, nextChar.val, nextChar.freq-1))
                    # Push back the current char with remaining frequency
                    heapq.heappush(maxHeap, Solution.Char(cur.ord, cur.val, cur.freq-used))
                    break

        return "".join(output)