"""
https://www.fastprep.io/problems/amazon-count-faults
Implement a prototype service to automate the detection and replacement of faulty servers to improve the availabity of an application.

There are n servers with its s1, s2,...,sn, and an array of strings, logs, of size m. Log format is "<server_id> <success/error>", the id of the server and the status of the processed request. If a perticular server id logs an error for three consecutive requests, it is considered faulty and is replaced with a new server with the same id.

Given n and athe array logs, find the number of times a faulty server was replace.

Function Description

Complete the function countFaults in the editor 👉.

countFaults has the following parameter:

int n: the number of servers
String logs[m]: the application logs
Returns

int: the number of times servers were replaced

Example 1:

Input:  n = 2, logs = ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]
Output: 1
Explanation:



s1 was replaced one time. So output should be 1.

Constraints:
1 <= n <= 200
1 <= m <= 2 * 104 (The source image is too blurry. It looked like 104 to me. If you find it incorrect, please let me know! Many thanks in advance 💛💚🧡💖)
"""
from typing import List
from collections import defaultdict


def countFaults(logs) -> int:
    replacements = 0
    freq = defaultdict(int)
    for log in logs:
        serverId, status = log.split(" ")
        if status == 'success':
            freq[serverId] = 0
        else:
            freq[serverId] += 1
        if freq[serverId] == 3:
            replacements += 1
            freq[serverId] = 0

    return replacements


print(countFaults(["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]))
print(countFaults(["s1 error", "s1 error", "s1 error", "s2 success", "s3 error", "s3 error", "s3 error"]))
print(countFaults(["s1 success", "s1 error", "s2 success", "s1 success", "s2 error", "s2 success"]))
print(countFaults(["s1 error", "s1 error", "s1 error"]))