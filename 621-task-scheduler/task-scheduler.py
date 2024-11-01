class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [(-f, ch) for ch,f in freq.items()]
        heapq.heapify(maxHeap)

        output = []
        # fill output while still tasks in the heap. Process cycle by cycle
        while maxHeap:
            cycle = n+1
            tempNodes = [] # will push these into heap with updates frequencies
            for _ in range(cycle):
                if maxHeap:
                    f, ch = heapq.heappop(maxHeap)
                    output.append(ch)
                    # reduce freq and save in tempNodes if still exists
                    if f+1 < 0:
                        tempNodes.append((f+1, ch))
                elif tempNodes: # tempnode is not empty but heap is empty meand we need to add idle chars
                    output.append("#")
                elif not tempNodes and not maxHeap: # nothing left, just break
                    break

            # After a cycle is filled, put tmpNodes back into the heap for next cycle
            for node in tempNodes:
                heapq.heappush(maxHeap, node)

        return len(output)





        