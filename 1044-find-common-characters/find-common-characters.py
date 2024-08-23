class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])

        for word in words[1:]:
            freqW = Counter(word)

            for ch, f in list(freq.items()):
                if ch not in freqW:
                    del freq[ch]
                else:
                    freq[ch] = min(freq[ch] , freqW[ch])

        ans = []
        for ch, f in freq.items():
            for i in range(f):
                ans.append(ch)
        return ans


            

        