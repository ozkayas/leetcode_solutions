from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hMap = {} # <string , list>

        for word in strs:
            wordKey = ''.join(sorted(word))
            if wordKey in hMap:
                hMap[wordKey].append(word)
            else:
                hMap[wordKey] = [word]

        return list(hMap.values())