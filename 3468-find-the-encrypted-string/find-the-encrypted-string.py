class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = k % len(s)

        circle = deque(list(s))

        for _ in range(k):
            circle.append(circle.popleft())

        return "".join(list(circle))
        