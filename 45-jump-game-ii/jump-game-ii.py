class Solution:
    def jump(self, nums: List[int]) -> int:
        
        hMap = {0:[0]} # Holds the steps until this index


        for i,n in enumerate(nums):
            stepTillThis = min(hMap[i]) if hMap[i] else float('inf')
            # print(i,hMap)
            if (i == len(nums)-1):
                return min(hMap[i])

            for j in range(n):
                ind = i + j + 1 # looked index to add steps
                if (ind) in hMap:
                    hMap[ind].append(stepTillThis+1)
                else:
                    hMap[ind] = [stepTillThis+1]

        # print(hMap)

        # return 0




'''
[2,3,1,1,4]
   1 1
     2 2 2
       2 3

her satir kac farkli yoldan gelinebilecegini ve kac adimda gelinecegini gosterir           

'''