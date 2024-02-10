class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
 
        def rec(digit) -> List[List[int]]:
            if digit == len(nums) -1:
                return [[nums[digit]],[]]

            nextNodeRes = rec(digit+1)
            res = []
            for n in nextNodeRes: # sample [[3], []]
      
                res.append(n)
       
                a = n.copy()
                a.append(nums[digit])
    
                res.append(a)
     

            return res

        return rec(0)




















 
 
'''       
        n = len(nums)
        res = []

        for i in range(2**n):
            subItem = []

            for b in range(n):
                if i & 1 << b : subItem.append(nums[b])

            res.append(subItem)
        
        return res

        # Watch this for explanation
        # https://www.youtube.com/watch?v=b7AYbpM5YrE

'''