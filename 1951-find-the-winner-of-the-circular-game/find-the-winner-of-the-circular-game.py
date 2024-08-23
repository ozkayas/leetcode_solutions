class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        circle = deque([i+1 for i in range(n)])    

        while len(circle) > 1:
            for _ in range(k - 1):
                circle.append(circle.popleft())
            circle.popleft()
                
        return circle[0]
