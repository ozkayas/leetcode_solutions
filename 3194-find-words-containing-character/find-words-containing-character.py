class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        N = len(words)

        for i in range(N):
            if x in words[i]:
                output.append(i)


        return output 