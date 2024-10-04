class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = 0
        basket = defaultdict(int)
        maxSoFar = 0

        while r < len(fruits):
            cur_fruit = fruits[r]
            basket[cur_fruit] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            maxSoFar = max(maxSoFar, (r-l+1))
            # print(f"maxSF: {maxSoFar}, {l}-{r}")
            r += 1

        return maxSoFar

        