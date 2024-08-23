class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        ans = 0
        def smallerThan(n:int, arr:List[int]) -> int:
            count = 0
            for x in arr:
                if x < n: count += 1
            return count
        
        def largerThan(n:int, arr:List[int]) -> int:
            count = 0
            for x in arr:
                if x > n: count += 1
            return count

        for i in range(1, N-1):
            #increasing
            left = smallerThan(rating[i], rating[:i])
            right = largerThan(rating[i], rating[i+1:])
            ans += left * right
            #decresing
            left = largerThan(rating[i], rating[:i])
            right = smallerThan(rating[i], rating[i+1:])
            ans += left * right
            # print(rating[i], sm, lg)

        return ans


        