'''
https://www.fastprep.io/problems/get-min-time
Developers at Amazon have deployed an application with a distributed database. It is stored on total_servers different servers numbered from 1 to total_servers that are connected in a circular fashion, i.e. 1 is connected to 2, 2 is connected to 3, and so on until total_servers connects back to 1.

There is a subset of servers represented by an array servers of integers. They need to transfer the data to each other to be synchronized. Data transfer from one server to one it is directly connected to takes 1 unit of time. Starting from any server, find the minimum amount of time to transfer the data to all the other servers.

Function Description

Complete the function getMinTime in the editor.

getMinTime takes the following arguments:

int total_servers: The number of servers in the system
int servers[n]: The servers to share the data with
Returns

int: The minimum time required to transfer the data on all the servers

Example 1:

Input:  total_servers = 8, servers = [2, 6, 8]
Output: 4 
Example 2:

Input:  total_servers = 5, servers = [1, 5]
Output: 1 
Explanation:

The two servers are directly connected so it will take only 1 unit of time to share the data.
      
Example 3:

Input:  total_servers = 10, servers = [4, 6, 2, 9]
Output: 7 
'''

## Surada anlatildigi sekilde 2 cozum var
## Spanning Tree kullanimi ve lineear sekilde array uzerinde hesaplama
'''
Solution 1: create clockwise edges and build a minimum spanning tree to connect all servers.
n = 10, servers = [2,4,6,9]
edges in [u, v, w] format: [ [2, 4, 2], [4, 6, 2], [6, 9, 3], [9, 2, 3] ]
minimum spanning tree will contain edges [ [2, 4, 2], [4, 6, 2], [6, 9, 3] ] or [ [2, 4, 2], [4, 6, 2], [9, 2, 3] ]

Solution 2: clockwisely check the fully connected distance starting from each server and track the minimum value.
n = 10, servers = [2,4,6,9]
distance start from 2 to 9 is 7
distance start from 4 to 2 is 8
distance start from 6 to 4 is 8
distance start from 9 to 6 is 7
so the minimum distance is 7'''

from typing import List

## INPUT
total_servers = 8
servers = [2, 6, 8]

total_servers = 5
servers = [1, 5]

total_servers = 10
servers = [4, 6, 2, 9]

## Calculates distance in clockwise direction
def calculateDist(a:int, b:int, total:int)->int:
    if a < b:
        return b-a
    else:
        return (total-b) + (a)


def getMinTime(total_servers:List[int], servers:List[int]) -> int:
    servers.sort()
    min_dist = 0

    s, e = 0 , len(servers)-1

    while s < len(servers):
        a, b = servers[s], servers[e]
        min_dist = min(min_dist, calculateDist(a,b))
        s += 1
        e += 1
        e = e % len(servers)
    return min_dist


print(getMinTime(total_servers,servers))