# Python Program for the above approach
from typing import List

# Function to count subarray having average exactly equal to K
def countKAverageSubarrays(arr: List[int], k) -> tuple:
    N = len(arr)
    result = 0
    curSum = 0
    subarrays = []

    # Store the frequency of prefix sum of the array arr[]
    mp = dict()

    for i in range(-1, N):

        # Subtract k from each element, then add it to curSum
        curSum += (arr[i] - k)

        # If curSum is 0 that means sum[0...i] is 0 so increment  res
        if curSum == 0:
            result += 1

        # Check if curSum has occurred before and if it has occurred before, add it's frequency to res
        if curSum in mp:
            result += mp[curSum][0]
            # print(f"i: {i}, curSum: {curSum} mp: {mp}")
            for j in mp[curSum][1]:
                subarrays.append(arr[j+1:i+1])
                # print(f"subarrays: {subarrays}")

        # Increment the frequency of curSum
        if curSum in mp:
            mp[curSum][0] += 1
            mp[curSum][1].append(i)
        else:
            mp[curSum] = [1, [i]]

    # Return result
    return result, subarrays

print(countKAverageSubarrays([12, 5, 3, 10, 4, 8, 10, 12, -6, -1],  6))
print(countKAverageSubarrays([6], 6))
print(countKAverageSubarrays([6, 6], 6))
print(countKAverageSubarrays([1, 2, 3, 4, 5], 1))
print(countKAverageSubarrays([1, 2, 3, 4, 5], 2))
print(countKAverageSubarrays([1, 2, 3, 4, 5], 3))
print(countKAverageSubarrays([1, 2, 3, 4, 5], 4))
print(countKAverageSubarrays([1, 2, 3, 4, 5], 5))
print(countKAverageSubarrays([1, 2, 3], 2))