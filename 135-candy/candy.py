class Solution:
    def candy(self, ratings: List[int]) -> int:

        def passOverCandies(candies: List[int], ratings: List[int]) -> List[int]:
            for i, r in enumerate(ratings):
                if i == 0:
                    continue
                if r > ratings[i-1] and candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1]+1
            return candies


        N = len(ratings)
        candies = [1 for _ in range(N)]
        candies = passOverCandies(candies, ratings)
        candies = passOverCandies(candies[::-1], ratings[::-1])
        
        return sum(candies)


        """
        5 4 3 5 6 2
        1 1 1 1 1 1
        1 1 1 2 3 1
        3 2 1 2 3 1
        
        """

    
        