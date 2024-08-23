class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        def freqTable(s: str) -> Dict[str, List[int]]:
            n = len(s)
            freq = dict()
            abc = 'abcdefghijklmnopqrstuvwxyz'

            for ch in abc:
                freq[ch] = [0 for _ in range(n)]

            # insert first letter
            freq[s[0]][0] = 1
            
            for i in range(1, n):
                cur = s[i]
                for key in freq.keys():
                    if cur == key:
                        freq[key][i] = freq[key][i-1] + 1
                    else:
                        freq[key][i] = freq[key][i-1]


            return freq
        
        def canBePalindrome(freqs: Dict[str, List[int]], left: int, right: int, k: int):
            oddCounter = 0
            abc = 'abcdefghijklmnopqrstuvwxyz'

            for ch in abc:
                rightF = freqs[ch][right]
                leftF = freqs[ch][left-1] if left > 0 else 0
                if (rightF - leftF) % 2 != 0:
                    oddCounter += 1

                # print(f"ch {ch}, rightF {rightF}, leftF {leftF}, oddCounter {oddCounter}")
            
            oddCounter -= (2 * k)

            return oddCounter < 2
        
        ans = []
        # a : 1 1 1 1 2
        # b : 0 1 1 1 1
        # c : 0 0 1 1 1
        # d : 0 0 0 1 1
        freqs = freqTable(s)
        # print(freqs)

        for query in queries:
            ans.append(canBePalindrome(freqs, query[0], query[1], query[-1]))

        return ans