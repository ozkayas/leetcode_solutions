class Solution:
    def minOperations(self, logs: List[str]) -> int:
        opStack = []

        for log in logs:
            if log == "../" and opStack:
                opStack.pop()
            elif log == "./" or log == "../":
                continue
            else:
                opStack.append(log[:-1])
        return len(opStack)
