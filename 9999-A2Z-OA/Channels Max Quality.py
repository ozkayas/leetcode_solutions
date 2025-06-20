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


## INPUTS
packets = [1, 2, 3 , 4 , 5] 
n = 2
print(calculateMedianSum(packets, n))
packets = [2, 2, 1, 5, 3]
n = 2
print(calculateMedianSum(packets, n))
#
#
# ### Another solution:
# def solution(packets, channels):
#     if len(packets) < 1 or len(packets) > 500000:
#         return
#     for i in range(len(packets)):
#         if packets[i] < 1 or packets[i] > 1000000000:
#             return
#     if channels < 1 or channels > len(packets):
#         return
#     if channels == 1:
#         result = sum(packets)
#         print(result)
#     packets_sorted = sorted(packets, reverse=True)
#     result = 0
#     for i in range(channels - 1):
#         result += packets_sorted[i]
#     median_temp = packets_sorted[channels - 1:len(packets_sorted)]
#     print(median_temp)
#     temp = 0
#     if len(median_temp) % 2 == 0:
#         temp = (median_temp[len(median_temp) // 2] + median_temp[len(median_temp) // 2 - 1]) / 2
#     else:
#         temp = (median_temp[len(median_temp) // 2])
#
#     result += temp
#
#     print(math.ceil(result))


### Approach 3 ; quick select for better performance
import math
import random

def quick_select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot_index = random.randint(left, right)
    pivot_index = partition(arr, left, right, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, right, k)


def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left

    for i in range(left, right):
        if arr[i] > pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    arr[right], arr[store_index] = arr[store_index], arr[right]

    return store_index

def top_k_minus_one_sum(arr, k):
    if k <= 1:
        return []

    quick_select(arr, 0, len(arr) - 1, k - 1)

    return sum(arr[:k-1])

def last_channel_median(arr, k):
    remain_arr = arr[k - 1:]
    n = len(remain_arr)
    if n % 2 == 1:
        return remain_arr[n // 2]
    else:
        a = float(remain_arr[n // 2 - 1])
        b = float(remain_arr[n // 2])
        return (a + b) / 2


def max_median_distribute_channels(nums, k):
    res = 0
    res += top_k_minus_one_sum(nums, k)
    res += last_channel_median(arr, k)
    return res


# arr = [1, 2, 3, 2, 1, 5]
arr = [2, 2, 1, 5, 3]
k = 2
result = max_median_distribute_channels(arr, k)
print(result)