'''Amazon Books is a retail store that sells the newly launched novel "The Story of Amazon". The novel is divided into volumes numbered from 1 to n and unfortunately, all the volumes are currently out of stock.

The Amazon team announced that starting today, they will bring exactly one volume of "The Story of Amazon" in stock each of the next n days. On the nth day, all volumes will be there. Being an impatient bookworm, each day you will purchase the maximum number of volumes you can such that:

You have not purchased the volume before.
You already own all its direct prior volumes.
Note: For the ith volume of the novel, all the volumes such that j < i are its prequels.

Determine the volumes you would purchase each day. You should return an array of n arrays where the ith array contains:

the volume numbers in ascending order if you purchased some volumes on the ith day
the single element -1 if you did not purchase any book
Function Description

Complete the function buyVolumes in the editor below.

buyVolumes has the following parameter:

int volumes[n]: an array of integers where the ith integer denotes the volume that is in stock on the ith day

Returns

int[n][n]: a 2d array of integers where the ith array denotes the volumes purchased on the ith day

𓈒𓇼 ࣪ 𓈒 Manyy Manyyy thanks to da best aikay and kl~~!⭒𓆡 ⭒ 🫧

Example 1:

Input: volumes = [2, 1, 4, 3]
Output: [[-1], [1, 2], [-1], [3, 4]]
'''

def buyVolumes(volumes):
    n = len(volumes)
    if n == 0:
        return [[-1]]

    # Initialize a set to keep track of purchased volumes
    result = []
    bucket = [0 for _ in range(n + 1)]
    p = 1

    for i in range(n):
        bucket[volumes[i]] = 1
        temp = []
        while p < n+1 and bucket[p] == 1:
            temp.append(p)
            p += 1
        if temp:
            result.append(temp)
        else:
            result.append([-1])

    return result


# Test Cases
if __name__ == "__main__":
    assert buyVolumes([2, 1, 4, 3]) == [[-1], [1, 2], [-1], [3, 4]]
    assert buyVolumes([1, 4, 3, 2, 5]) == [[1], [-1], [-1], [2, 3, 4], [5]]
    print("😎 \nAll test cases passed!\n")