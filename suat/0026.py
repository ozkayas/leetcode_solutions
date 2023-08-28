class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head, end = 0, 0

        while end < len(nums):
            if nums[head] == nums[end]:
                end += 1
            else:
                head += 1
                nums[head], nums[end] = nums[end], nums[head]
                end += 1

        return head +1




'''
R
0,0,1,1,1,2,2,3,3,4
L

    R
0,0,1,1,1,2,2,3,3,4
L

shift L, change numbers, shift R
      R
0,1,0,1,1,2,2,3,3,4
  L

          R
0,1,0,1,1,2,2,3,3,4
  L  

            R
0,1,2,1,1,0,2,3,3,4
    L 


'''