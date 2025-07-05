'''Given the computational power of all the n servers as an array of integers powers, find the maximum number of servers that the client can buy such that the selected set of servers can be rearranged in a way that the absolute difference between the computational power of two adjacent servers is less than or equal to 1. The client wants to create a circular network so the first and last servers in the sequence are also considered adjacent.

More formally, a sequence candidate[] of length m is classified as a candidate for selection by the client if it can be rearranged in a way such that abs(candidate[i] - candidate[i+1]) <= 1 for 0 <= i < m - 1 and abs (candidate[m-1] - candidate[0]) <= 1. (Yus, I double checked it is called "candidate".. no typo here :)

Find the maximum number of servers the client can buy from the n avalable servers.
'''

def getMaxServers(powers):
    if not powers:
        return 0
    
    def is_valid_subarray(arr):
        zeros = [i for i, x in enumerate(arr) if x == 0]
        if zeros:
            return False

        ones = [i for i, x in enumerate(arr) if x == 1]
        if not ones:
            return True
        if len(arr) == 1:
            return True
        if len(ones) == 1:
            return ones[0] == 0 or ones[0] == len(arr)-1
        if len(ones) == 2:
            return ones[0] == 0 and ones[1] == len(arr)-1
        return False
    
    # Count the frequency of each power level
    power_count = {}
    for power in powers:
        if power in power_count:
            power_count[power] += 1
        else:
            power_count[power] = 1
    
    # Bucket sort the powers, from min to max
    min_power = min(power_count.keys())
    max_power = max(power_count.keys())
    buckets = [0] * (max_power - min_power + 1)
    for power, count in power_count.items():
        buckets[power - min_power] = count
    print(f"Buckets: {buckets}")

    # Sliding window, expand using is_valid_subarray helper function
    max_servers = 0
    left = 0
    for right in range(len(buckets)):
        while left < right and not is_valid_subarray(buckets[left:right+1]):
            left += 1
        max_servers = max(max_servers, sum(buckets[left:right+1])) 

    return max_servers



# Test cases
if __name__ == "__main__":
    assert getMaxServers([1, 2, 3, 4, 5]) == 2
    assert getMaxServers([1, 2, 2, 3, 4]) == 4
    assert getMaxServers([1, 3, 5, 7]) == 1
    assert getMaxServers([1,1,2,2,3,4,6,7,7,8]) == 5
    print(" 😎 All test cases passed ")