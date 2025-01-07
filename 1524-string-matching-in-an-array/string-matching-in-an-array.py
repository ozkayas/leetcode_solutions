class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # KMP ile cozulmeli ancak usendim :)

        matching = []
        for seeking in words:
            for anyWord in words:
                if seeking == anyWord:
                    continue
                if seeking in anyWord:
                    matching.append(seeking)
                    break
        return matching

        