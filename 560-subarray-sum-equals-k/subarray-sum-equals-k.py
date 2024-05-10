class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ###  This is the solution on Editorial

        # Will hold prefixSum frequencies 
        # {4:1, 6:2} 4 is seen 1 time in prefix, 6 is seen 2 times
        # we need this to find pairs summing to k
        prefixMap = defaultdict(int)
        prefixMap[0] = 1 # Adding 0 to calculate the num itself, because 0 is pair for itself

        counter = 0
        preFixSum = 0
        for num in nums:
            preFixSum += num
            pairOfThis = preFixSum - k
            counter += prefixMap[pairOfThis]
            
            prefixMap[preFixSum] += 1
        return counter


"""        k = 7

        3  4  7  2  -3  1  4  2   => count: 4
        3. 7 14. 16 13. 14 18 20




     0:1
     3:1
     7:1
     14:2
     16:1
     13:1
     18:1
     20:1"""

        