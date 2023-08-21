class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = []
        temp = ""

        for ch in s:
            if ch == " ":
                words.append(temp)
                if len(words) == k:
                    return " ".join(words)
                temp = ""
            else:
                temp += ch


                
        words.append(temp)

        return " ".join(words)