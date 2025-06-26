'''The developers at Amazon want to perform a reliability drill on some servers. There are 
𝑛
n servers, where the 
𝑖
𝑡
ℎ
i 
th
  server can serve 
request
[
𝑖
]
request[i] number of requests and has an initial health of 
health
[
𝑖
]
health[i] units.

Each second, the developers send the maximum possible number of requests that can be served by all the available servers. With the request, the developers can also send a virus to one of the servers that can decrease the health of a particular server by 
𝑘
k units. The developers can choose the server where the virus should be sent.
A server goes down when its health is less than or equal to 0.

After all the servers are down, the developers must send one more request to conclude the failure of the application.

Find the minimum total number of requests that the developers must use to bring all the servers down.

Example
Consider:

𝑛
=
2
n=2

request
=
[
3
,
4
]
request=[3,4]

health
=
[
4
,
6
]
health=[4,6]

𝑘
=
3
k=3

The minimum number of requests required is 21.

No. of Request	Total Requests	Virus Server	Server’s New Health
7	3 + 4 = 7	1	6 - 3 = 3
7	3 + 4 = 7	1	3 - 3 = 0 → server 1 dies
3	3	0	4 - 3 = 1
3	3	0	1 - 3 = -2 → server 0 dies
1	-	-	→ conclude the failure
'''
import heapq

def getMinRequests(requests, health, k):
    total = 0
    for i, h in enumerate(health):
        health[i] = (h + k - 1) // k
        total += health[i]

    impacts = []
    for i, req in enumerate(requests):
        impact = req * (total - health[i])
        impacts.append((impact, i))
    impacts.sort()

    cumm, ans = 0, 0
    for i in reversed(range(len(impacts))):
        _, idx = impacts[i]
        ans += requests[idx] * (health[idx] + cumm)
        cumm += health[idx]

    ans += 1

    print(ans)
    return ans
'''
# Testcase 1: ans = 21
n = 2
request = [3, 4]
health = [4, 6]
k = 3

# Testcase 2: ans = 213
n = 2
request = [2, 10]
health = [1, 20]
k = 1

# Testcase 3: ans = 33
n = 3
request = [3, 4, 5]
health = [4, 6, 2]
k = 3

# Testcase 4: ans = 23
n = 2
request = [2, 10]
health = [5, 1]
k = 1
----------------------'''
# Test cases
if __name__ == "__main__":
    assert getMinRequests([3, 4], [4, 6], 3) == 21, "Test Case 1 Failed"
    assert getMinRequests([2, 10], [1, 20], 1) == 213, "Test Case 2 Failed"
    assert getMinRequests([3, 4, 5], [4, 6, 2], 3) == 33, "Test Case 3 Failed"
    assert getMinRequests([2, 10], [5, 1], 1) == 23, "Test Case 4 Failed"
    print(" 😎 All test cases passed \n")