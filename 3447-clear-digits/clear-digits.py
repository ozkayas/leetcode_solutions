class Solution:
    def clearDigits(self, s: str) -> str:
        nonDigitStack = []
        for ch in s:
            if ch.isdigit() and nonDigitStack:
                nonDigitStack.pop()
            else:
                nonDigitStack.append(ch)

        return "".join(nonDigitStack)
        