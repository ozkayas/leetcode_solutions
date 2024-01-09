class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0

        for snt in sentences:
            count = 0
            for ch in snt:
                if ch == " ":
                    count += 1

            result = max(result, count)

        return result + 1
        