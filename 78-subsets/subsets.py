class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backTrack(i, subset):
            print("BT called i, subset",i, subset)
            #bu son index ise, leaf node, subsete kendin ekle ve sonuca ekle ve return
            if i == len(nums)-1:
                s = subset.copy()
                ans.append(s.copy())
                s.append(nums[i])
                ans.append(s.copy())
                print("leaf node returning", ans)
                return

            subset.append(nums[i])
            backTrack(i+1, subset)
            subset.pop()
            backTrack(i+1, subset)

        
        backTrack(0,[])

        return ans
        