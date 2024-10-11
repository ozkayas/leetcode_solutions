class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        Chair = namedtuple("Chair", ["available_at","id"])
        Friend = namedtuple("Friend", ["arrival","leave","id"])

        # available chairs in a minHeap, just with their ids starting from 0 to inf
        availables = []
        heapq.heapify(availables)

        # Will hold Chair models
        occupiedChairs = []
        heapq.heapify(occupiedChairs)

        def totalChairsInSystem() -> int:
            return len(availables) + len(occupiedChairs)

        friends = [Friend(times[i][0], times[i][1], i) for i in range(len(times))]
        friends.sort(key=lambda x: x.arrival)  # Sort friends by arrival time

        for f in friends:
            # Unoccupy chairs at this time and insert into availables list
            while occupiedChairs and occupiedChairs[0].available_at <= f.arrival:
                chair = heapq.heappop(occupiedChairs)
                heapq.heappush(availables, chair.id)
            # if still not available chairs, then create a new chair
            if not availables:
                newChairId = totalChairsInSystem()
                heapq.heappush(availables, newChairId)
            
            # Fill first available chair and insert into occupiedList
            firstAvChairId = heapq.heappop(availables)
            if f.id == targetFriend:
                return firstAvChairId
            else:
                heapq.heappush(occupiedChairs, Chair(f.leave, firstAvChairId))
