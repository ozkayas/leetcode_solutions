class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        # Will return (value, index) for each index. Smaller or equal, not strictly smaller.
        # [(1, 1), (inf, 4), (inf, 4), (inf, 4)]
        def smallerOrEqualOnRight(arr:List[int]) -> List[int]:
            N = len(arr)
            sor = [(float("inf"), N) for _ in range(N)]
            st = []
            for i in range(N-1,-1,-1):
                cur = arr[i]
                while st and cur <= st[-1][0]:
                    st.pop()
                
                if st:
                    sor[i] = st[-1]

                st.append((cur, i))

            return sor

        # Will return (value, index) for each index. Smaller.
        # [(inf, -1),(inf, -1),(1,1), (2, 2)
        def smallerOnLeft(arr:List[int]) -> List[int]:
            N = len(arr)
            sor = [(float("inf"), -1) for _ in range(N)]
            st = []
            for i in range(N):
                cur = arr[i]
                while st and cur < st[-1][0]:
                    st.pop()
                
                if st:
                    sor[i] = st[-1]

                st.append((cur, i))

            return sor

        # print(smallerOrEqualOnRight(arr))
        # print(smallerOnLeft(arr))

        sor = smallerOrEqualOnRight(arr)
        sol = smallerOnLeft(arr)
        
        MOD = 10**9 + 7
        total = 0
        for i in range(len(arr)):
            total += (arr[i] * (sor[i][1] - i) * (i - sol[i][1])) % MOD
        return total % MOD

                



        