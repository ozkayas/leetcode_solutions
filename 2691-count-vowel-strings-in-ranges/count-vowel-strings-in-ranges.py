class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        prefix = [0]
        count = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix.append(count)
        
        def getVowels(query: List[int], prefix) -> int:
            s , e = query[0], query[1]
            return prefix[e+1]-prefix[s]

        result = []
        for q in queries:
            result.append(getVowels(q,prefix))

        return result



        
'''

  ["aba","bcb","ece","aa","e"]
 0   1     1     2    3    4

'''