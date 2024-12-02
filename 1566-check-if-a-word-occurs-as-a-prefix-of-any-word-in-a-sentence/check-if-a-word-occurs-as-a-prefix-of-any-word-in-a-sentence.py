class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if len(word) < len(searchWord):
                continue
            elif word.startswith(searchWord):
                return i+1

        return -1


        