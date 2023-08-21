class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1, set2,set3 = set(nums1), set(nums2), set(nums3)

        return set1&set2 | set1&set3 | set2&set3



        '''
        hMap = {}
        for num in set(nums1):
            if num in hMap:
                hMap[num] += 1
            else:
                hMap[num] = 1

        for num in set(nums2):
            if num in hMap:
                hMap[num] += 1
            else:
                hMap[num] = 1

        for num in set(nums3):
            if num in hMap:
                hMap[num] += 1
            else:
                hMap[num] = 1

        res = []
        for num in hMap.keys():
            if hMap[num] > 1:
                res.append(num)
        
        return res
        '''