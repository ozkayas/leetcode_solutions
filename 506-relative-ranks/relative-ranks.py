class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Use a max heap, with elements (score, index)
        max_heap, output = [], [0 for _ in score]
        heapq.heapify(max_heap)

        for i,s in enumerate(score):
            heapq.heappush(max_heap, (-s, i))


        rank = 0
        while max_heap:
            score, index = heapq.heappop(max_heap)
            rank += 1
            # print(score, index)

            if rank == 1:
                output[index] = 'Gold Medal'
            elif rank == 2:
                output[index] = 'Silver Medal'
            elif rank == 3:
                output[index] = 'Bronze Medal'
            else:
                output[index] = str(rank)
        
        return output



        