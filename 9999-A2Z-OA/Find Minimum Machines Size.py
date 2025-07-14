'''
An analyst in the logistics team of Amazon e-commerce was reviewing the efficiency metrics of the new automated stocking and retrieval machines. They went about their calculations in the following manner:

A sequence of n machines is tasked with stocking or retrieving items. Given the individual stocking/retrieving capacity values of each machine as an integer array, machineCapacity.

The Efficiency of this sequence is evaluated using a comparison metric: the sum of the absolute difference between consecutive machine capacities.

The task is to determine whether achieving the same sum of the absolute difference is possible by removing some machines from the sequence to streamline the operations. If it is possible, return the minimum number of machines required in the sequence to attain the same sum of the absolute difference between consecutive machine capacities.

It's important to note that the number of machines in the sequence must always be greater than 0. If achieving the same sum is impossible on removal, return n, which is the original number of machines in the sequence.

Note: The efficiency score of a sequence consisting of only one machine is 0.

Function Description

findMinimumMachinesSize() has the following parameter(s):


int machineCapacity[n]: the stocking/retrieval capacity of each machine
Returns

int: the minimum number of machines in the sequence required to achieve the same performance score'''

from typing import List


class Solution:
    def findMinimumMachinesSize(self, machineCapacity: List[int]) -> int:
        n = len(machineCapacity)
        if n == 0:
            return 0  # 约束里不会出现，但以防万一

        # 1. 压缩相邻重复
        comp = []
        for v in machineCapacity:
            if not comp or v != comp[-1]:
                comp.append(v)

        if len(comp) == 1:  # 全相同 → 分数为 0
            return 1

        # 2. 保留拐点
        st = [comp[0], comp[1]]
        for x in comp[2:]:
            while (len(st) >= 2 and
                   (st[-1] - st[-2]) * (x - st[-1]) > 0):
                st.pop()  # 删除中间点
            st.append(x)

        return len(st)
    

# TEST CASES
if __name__ == "__main__":
    assert Solution().findMinimumMachinesSize([5,4,0,3,3,1]) == 4
    assert Solution().findMinimumMachinesSize([6,4,4,3,3,2]) == 2
    assert Solution().findMinimumMachinesSize([1,2,2,1,1]) == 3
    print("\n 😎 All test cases passed!")