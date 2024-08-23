class Solution:
    def minimumPushes(self, word: str) -> int:

        def tapValueFor(i: int) -> int:
            if i <= 8:
                return 1
            elif i <= 16:
                return 2
            elif i <= 24:
                return 3
            else:
                return 4
        
        letterMap = dict()
        # Mapping letters 8 by 8, because 8 empty slots for each letter
        mapCounter = 0

        f = Counter(word)
        fList = f.most_common() # sorted tuple of [(a,7),(b,5),...]

        ans = 0
        for letter, freq in fList:
            mapCounter += 1
            ans += tapValueFor(mapCounter) * freq
            # letterMap[letter] = tapValueFor(mapCounter)
        return ans 
        # ans = 0
        # for ch in word:
        #     ans += letterMap[ch]

        # return ans






        