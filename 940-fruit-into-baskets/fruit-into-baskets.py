class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        ans = 0
        l = r = 0

        while r < len(fruits):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0: del basket[fruits[l]]
                l += 1
            ans = max (ans, r-l+1)
            r += 1

        return ans


        