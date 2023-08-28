class Solution:
    ####################
    ### ye15 solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in nums]
        for x, v in freq.items(): bucket[-v].append(x)
        print('bucket :  ', bucket)

        ans = []
        for x in bucket: 
            ans.extend(x)
            print(x, ' ', ans)
            if len(ans) >= k: break
        return ans
        
        
        
'''    
my original solution    
        counter = Counter(nums)
        commons = counter.most_common(k)
        ans = [obj[0] for obj in commons]

        return ans
'''