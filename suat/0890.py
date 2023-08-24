class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        hMap = {}
        output = []

        for word in words:
            hMap.clear()
            for i, c in enumerate(pattern):
                if (c not in hMap):
                    if (word[i] not in hMap.values()):
                        hMap[c] = word[i]
                    else:
                        break
                elif hMap[c] != word[i]:
                    break
                if i == len(word) -1:
                    output.append(word)


        return output
