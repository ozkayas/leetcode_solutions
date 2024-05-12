class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(quality)
        worker=[[w/q, q] for w, q in zip(wage, quality)]

        worker.sort()
        quality_sum=0
        heap=[]

        for ratio, q in worker[:k]:
            quality_sum+=q
            heappush(heap, -q)
        pay=worker[k-1][0]*quality_sum

        for ratio, q in worker[k:n]:
            heappush(heap, -q)
            quality_sum+=q+heappop(heap)
            pay=min(pay, quality_sum*ratio)

        return pay
        