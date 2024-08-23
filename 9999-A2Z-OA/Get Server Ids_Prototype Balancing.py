'''
The developers of Amazon are working on a prototype for a simple load-balancing algorithm. There are num_servers servers numbered from 0 to num_servers - 1 and the initial number of requests assigned to each server is 0.

In the i-th second, a request comes from IP hash of requests[i], and it must be assigned to the server with the minimum number of requests amongst the first requests[i] servers. For example, if requests[i] = 4, the request must be assigned to the server with the minimum number of requests amongst the servers with id [0, 1, 2, 3]. If there are multiple servers with the same minimum number of requests, choose the one with the minimum id. When a request is assigned to a server, its number of requests increases by 1.

Given num_servers and the array requests, for each request, find the id of the server it is assigned to.

Function Description

Complete the function getServerIds in the editor.

getServerIds takes the following arguments:

int num_servers ; the number of servers
int requests[] ; the sizes of the requests
Returns

int[] ; the ids of the servers each request is assigned to

Credit to ˗ˏˋ✰full-stack-dev✰ ˎˊ˗° ᡣ𐭩

Example 1:

Input:  num_servers = 5, requests = [4, 0, 2, 2]
Output: [0, 0, 1, 1] 
Explanation
        After the first request, the number of requests is [1, 0, 0, 0, 0]. After the second request, the number of requests is [2, 0, 0, 0, 0]. After the third request, the number of requests is [2, 1, 0, 0, 0]. After the fourth request, the number of requests is [2, 1, 1, 0, 0].
Example 2:

Input:  num_servers = 5, requests = [0, 1, 2, 3]
Output: [0, 0, 1, 2] 
Explanation:
'''

'''
0 0 0 0 0 - 4 > 0
1 0 0 0 0 - 0 > 0
2 0 0 0 0 - 2 > 1
2 1 0 0 0 - 2 > 2

0 0 0 0 0 - 3-> 0
1 0 0 0 0 - 2 > 1
1 1 0 0 0 - 3 > 2
1 1 1 0 0 - 2 > 0
2 1 1 0 0 - 4 > 3
2 1 1 1 0
'''

from typing import List

# BS for target at the leftmost
def findServer(high: int, servers:List[int]):
    # Since this area is monotonic decresing,  2 - 2 - 1 -1 - 0 - 0 - 0
    #                                                         ^ return this index
    l  , h , target = 0, high, servers[high]
    idx = high
    while l <= h:
        mid = l + (h-l)//2
        if servers[mid] <= target:
            # hit a proper value, but maybe we can find at left, so continue
            idx = mid
            h = mid -1
        else:
            # target should be at right
            l = mid + 1
    return idx
        

def getServerIds(num_servers: int, requests: List[int]):
    servers = [0 for _ in range(num_servers)]
    id_tracker = []

    # Take each req and search for the leftmost smallest possible server
    for req in requests:
        # value_at_slot is surely the min value between 0 - req, however maybe there is
        # also same at left, so we binarysearch
        server_idx_add = findServer(req, servers )
        id_tracker.append(server_idx_add)
        servers[server_idx_add] += 1

    return id_tracker

print(getServerIds(5, [4, 0, 2, 2]))
print(getServerIds(5, [0, 1, 2, 3]))
print(getServerIds(5, [3, 2, 3, 2, 4]))


