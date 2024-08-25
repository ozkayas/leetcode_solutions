class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dp(amount) -> int:
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]
            
            # ask for each possibility and return the min result from next path
            min_of_next_path = float("inf")
            for coin in coins:
                if amount - coin < 0:
                    continue
                path_result = dp(amount - coin)
                if path_result >= 0:  # sadece geçerli yolları dikkate al
                    min_of_next_path = min(min_of_next_path, path_result)

            # no way to give a coin change
            if min_of_next_path == float("inf"):
                memo[amount] = -1
            else:
                memo[amount] = min_of_next_path + 1
            
            print("amount",amount,"returnin", memo[amount] )
            return memo[amount]

        return dp(amount)