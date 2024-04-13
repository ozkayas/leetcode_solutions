'''
You are given a list of packets of varying sizes and there are n channels.

Each of the n channel must have a single packet
Each packet can only be on a single channel
The quality of a channel is described as the median of the packet sizes on that channel. The total quality is defined as sum of the quality of all channels (round to integer in case of float).

Given the packet sizes and num of channels, find the maximum quality.

Function Description

Complete the function calculateMedianSum in the editor.

calculateMedianSum has the following parameters:

int[] packets: an array of integers
int n: the number of channels
Returns

int: the sum of the medians of each channel

Example 1:

Input:  packets = [1, 2, 3, 4, 5], n = 2
Output: 8 
If packet {1, 2, 3, 4} is sent to channel 1, the median of that channel would be 2.5
If packet {5} is sent to channel 2, its median would be 5
Max total quality is 2.5 + 5 = 7.5 ~ 8
      
Example 2:

Input:  packets = [5, 2, 2, 1, 5, 3], n = 2
Output: 7 
Explanation:
channel 1 -> {2, 2, 1, 3,}, median = 2
channel 2 -> {5, 5}, median = 5
total quality 2 + 5 = 7
'''
## INPUTS
# packets = [1, 2, 3 , 4 , 5] 
# n = 2
packets = [5, 2, 2, 1, 5, 3]
n = 2

from typing import List
import math

def medianOf(nums:List[int])->int:
    n = len(nums)
    m = int(n/2)
    if n % 2 == 0: ##  1 2 3 4 5 6 
        return math.ceil((nums[m-1] + nums[m]) / 2)
    else: ##  1 2 3 4 5 
        return (nums[(int((n-1)/2))])



def calculateMedianSum(packets:List[int], n:int) -> int:
    if n > len(packets):return -1
    if n == 0: return -1

    packet_bucket = [] # [5], [1234]

    packets.sort()

    while n > 0:
        if n > 1:
            biggest_item = packets.pop()
            packet_bucket.append([biggest_item])
        else:
            packet_bucket.append(packets)
        n -= 1


    sum_of_qualities = 0
    for p in packet_bucket:
        sum_of_qualities += medianOf(p)


    return sum_of_qualities



print(calculateMedianSum(packets, n))