class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mostUsedKey = Counter(nums).most_common(1)[0][0]
        return mostUsedKey
        
'''        
        hMap = {}

        for num in nums:
          if num in hMap:
            hMap[num] += 1
          else:
            hMap[num] = 1
          if hMap[num] > len(nums) // 2:
              return num
'''