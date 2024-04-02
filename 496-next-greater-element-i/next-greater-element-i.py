class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hMap = dict()
        stack = []
        ans = []

        for i in range(len(nums2)-1, -1, -1):
            curr = nums2[i]    
            while stack and stack[-1] < curr:
                stack.pop()

            if not stack:
                hMap[curr] = -1
            else:
                hMap[curr] = stack[-1]
            stack.append(curr)
        
        for n in nums1:
            ans.append(hMap[n])

        return ans

                


  
'''  s: 4 ,3 

   [1, 3, 4, 2]
    3  4  -1 -1



    map: 
    2: -1
    4: -1
    3:  4'''
