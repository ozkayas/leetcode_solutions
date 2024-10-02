from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        Server = namedtuple("Server", ["available_at", "id"])
        # Will hold available servers at the time. elements are id numbers.
        # Init with k servers, all available
        availables = SortedList([])

        handles = defaultdict(int)

        # Will hold (available_time, id) when the server will be available, and which
        minHeap = [Server(0, i) for i in range(k)]
        heapq.heapify(minHeap)

        for i in range(len(arrival)):
            arrivalTime = arrival[i]

            # When this request arrives, find all ServerAvailabilities,
            # pop from heap and add to the sortedList
            while minHeap and minHeap[0].available_at <= arrivalTime:
                server = heapq.heappop(minHeap)
                availables.add(server.id)

            # Find the kth or next available server using bisect_left
            if not availables: # No server available, discard this request
                continue
            suitable_server_idx = bisect_left(availables, i % k)
            suitable_server_idx = suitable_server_idx % len(availables) # looking for number 2 but not available, then look for 0, loop around
            suitable_server_id = availables[suitable_server_idx]

            # Remove this from the sorted list and add to the heap again
            availables.discard(suitable_server_id)
            heapq.heappush(minHeap, Server(arrivalTime + load[i], suitable_server_id))

            handles[suitable_server_id] += 1

        # Find the maximum number of handled requests
        if not handles:
            return []

        maxHandled = max(handles.values())

        # Collect all server IDs that have handled the maximum number of requests
        ans = [server_id for server_id, count in handles.items() if count == maxHandled]

        # Sort the answer as required (optional, depending on problem statement)
        ans.sort()

        return ans