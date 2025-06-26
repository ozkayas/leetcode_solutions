from typing import List

## Heap ile de cozulebilir. Ama bu daha kolay ve daha az kod ile cozuluyor.
def findMaximumWeights(k: int, weights: List[int]):
    index_weight = list(enumerate(weights))
    index_weight.sort(key = lambda x: (-x[1], x[0]))
    min_index = 0
    res = []
    for index, weight in index_weight:
        if index >= min_index:
            res.append(weight)
            min_index = index + k + 1
    return res


if __name__ == "__main__":
    # Test cases
    assert findMaximumWeights(1, [4, 3, 5, 5, 3]) == [5, 3], "Test Case 1 Failed"
    assert findMaximumWeights(2, [10, 20, 30, 40, 50]) == [50], "Test Case 2 Failed"
    assert findMaximumWeights(0, [1, 2, 3]) == [3], "Test Case 3 Failed"
    assert findMaximumWeights(3, [5, 4, 3, 2, 1]) == [5, 1], "Test Case 4 Failed"
    print("\n 😎 All test cases passed!")


'''Given an array weight which denotes the weights of n packages, the goal is to create the lexicographically maximal resulting array sorted by non-increasing order of weight using the following operations:


Discard the first package from the current weight array

Add the first element to the resulting array, then remove it along with the next k (a fixed constant) elements from the current array

Note that Operation 2 can also be applied when fewer than k elements remain after the current element; in that case, the entire remaining array is removed.

The resulting array must have packages arranged in non-increasing weight order.

Given an array weight of size n and an integer k, find the lexicographically maximal resulting array sorted by non-increasing order of weight that can be obtained.

Note: An array x is lexicographically greater than an array y if:

x[i] > y[i], where i is the first position where x and y differ, or

|x| > |y| and y is a prefix of x (where |x| denotes the size of array x)

Example:
k = 1
n = 5
weight = [4, 3, 5, 5, 3]

To obtain the lexicographically maximal resulting array sorted in non-increasing order, we will perform the following operations:

📄 Görsel 2 – Adım Adım İşlem Tablosu
Current Array	Operation Applied	Modified Current Array	Resulting Array
[4, 3, 5, 5, 3]	1) Discard the first element	[3, 5, 5, 3]	[]
[3, 5, 5, 3]	1) Discard the first element	[5, 5, 3]	[]
[5, 5, 3]	2) Discard first k+1 and add first discarded element in resulting array	[3]	[5]
[3]	2) Discard first k+1 and add first discarded element in resulting array	[]	[5, 3]

After performing the above operations, the resulting array is [5, 3]. It is guaranteed that no other resulting array sorted in non-increasing order can be formed that is lexicographically larger than [5, 3].

Therefore, the final array is [5, 3].

Function Description
Complete the function findMaximumWeights in the editor below.

'''