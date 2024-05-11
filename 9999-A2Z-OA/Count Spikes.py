import heapq

def k_spikes(prices, k):
    if k <= 0:
        return 0
    n = len(prices)
    minHeap = []
    for i in range(k):
        heapq.heappush(minHeap, prices[i])

    ## Helper Method return if k element smaller than target exists in the heap
    def hasKMinInHeap(heap, k, target):
        i = 0
        counter = 0
        temp = [] 
        while counter < k and heap:
            if heap[0] < target:
                num = heapq.heappop(heap)
                temp.append(num)
                counter += 1
            else:
                break
        for num in temp:
            heapq.heappush(heap, num)
        if counter == k:
            return True
        else:
            return False


    left_candidates = set()

    for i in range(k, n - k):
        if hasKMinInHeap(minHeap, k, prices[i]):
            left_candidates.add(i)
        heapq.heappush(minHeap, prices[i])

    # Early Quit
    if len(left_candidates) == 0:
        return 0


    minHeap = []
    for i in range(k):
        heapq.heappush(minHeap, prices[-1-i])

    right_candidates = set()
    for i in range(n - 1 - k, k - 1, -1):
        if hasKMinInHeap(minHeap, k, prices[i]):
            right_candidates.add(i)
        heapq.heappush(minHeap, prices[i])

    return len(left_candidates & right_candidates)


print(k_spikes([1, 1, 8, 5, 3, 4], 2))
print(k_spikes([4,10,6,10,4], 2))