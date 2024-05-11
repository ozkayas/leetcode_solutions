from collections import defaultdict
import heapq

def find_max_count(nums):
    d = defaultdict(int)
    h = []
    heapq.heapify(h)
    ans = []
    for x in nums:
        if x > 0:
            d[x] += 1
            heapq.heappush(h, -x)
        else:
            d[-x] -= 1

        found = False
        while not found:
            if not h:
                ans.append(0)
                found = True
            else:
                largest_value = -h[0]
                if d[largest_value] != 0:
                    ans.append(d[largest_value])
                    found = True
                else:
                    del d[largest_value]
                    heapq.heappop(h)
    return ans


assert find_max_count([2, 3, 3, -3, 1]) == [1,1,2,1,1]