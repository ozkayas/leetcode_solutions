'''Given the computational power of all the n servers as an array of integers powers, find the maximum number of servers that the client can buy such that the selected set of servers can be rearranged in a way that the absolute difference between the computational power of two adjacent servers is less than or equal to 1. The client wants to create a circular network so the first and last servers in the sequence are also considered adjacent.

More formally, a sequence candidate[] of length m is classified as a candidate for selection by the client if it can be rearranged in a way such that abs(candidate[i] - candidate[i+1]) <= 1 for 0 <= i < m - 1 and abs (candidate[m-1] - candidate[0]) <= 1. (Yus, I double checked it is called "candidate".. no typo here :)

Find the maximum number of servers the client can buy from the n avalable servers.
'''

def getMaxServers(powers):
    if not powers:
        return 0
    
    # Count the frequency of each power level
    power_count = {}
    for power in powers:
        power_count[power] = power_count.get(power, 0) + 1
    
    # Bucket sort the powers, from min to max
    if not power_count:
        return 0
    min_power = min(power_count.keys())
    max_power = max(power_count.keys())
    buckets = [0] * (max_power - min_power + 1)
    for power, count in power_count.items():
        buckets[power - min_power] = count

    # Optimized O(R) sliding window
    max_servers = 0
    left = 0
    current_sum = 0
    zeros = 0
    ones = 0

    for right in range(len(buckets)):
        # Add the right element to the window
        count = buckets[right]
        current_sum += count
        if count == 0:
            zeros += 1
        elif count == 1:
            ones += 1

        # Shrink the window from the left until it's valid
        # A window is invalid if:
        # 1. It contains a gap (a power with 0 servers).
        # 2. It contains more than 2 powers with only 1 server.
        while zeros > 0 or ones > 2:
            # Remove the left element from the window
            left_count = buckets[left]
            current_sum -= left_count
            if left_count == 0:
                zeros -= 1
            elif left_count == 1:
                ones -= 1
            left += 1
        
        # A special case for validity: if there are 2 'ones',
        # they must be at the ends of the current window.
        # If not, shrink the window.
        if ones == 2 and buckets[left] != 1:
             # The left element must be a '1', but it isn't.
             # This is an invalid state, so we subtract the left element
             # and continue to the next iteration without updating max_servers.
             current_sum -= buckets[left]
             if buckets[left] == 1: # This condition will not be met here, but good for correctness
                 ones -= 1
             left += 1
             continue

        max_servers = max(max_servers, current_sum)

    return max_servers



# Test cases
if __name__ == "__main__":
    assert getMaxServers([1, 2, 3, 4, 5]) == 2
    assert getMaxServers([1, 2, 2, 3, 4]) == 4
    assert getMaxServers([1, 3, 5, 7]) == 1
    assert getMaxServers([1,1,2,2,3,4,6,7,7,8]) == 5
    print(" 😎 All test cases passed ")