class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hMap = {}
        count = 0

        #fill hash map , hMap = Counter(nums) da bu kod ile ayni 
        for num in nums:
            if num in hMap.keys():
                hMap[num] += 1
            else:
                hMap[num] = 1
        
        # frekansi 1 olanlari topla
        #for num in hMap.keys():
        #    if hMap[num] == 1:
        #        count += num
        for k, v in hMap.items(): # k: key,
            if v == 1:
                count += k

        return count

        '''
        freq = Counter(nums)
        return sum(k for k, v in freq.items() if v == 1)
        '''


        '''
        add each to hashMap, 
        then iterate over hashMap

        time = O(2n)

        '''   