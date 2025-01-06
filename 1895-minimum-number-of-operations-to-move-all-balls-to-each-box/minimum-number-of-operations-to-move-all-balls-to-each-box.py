class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        answer = [0 for _ in range(N)]
        ballToAdd , ballsCarried = 0, 0
        for i in range(N):
            answer[i] += ballToAdd
            ballsCarried += int(boxes[i]) 
            ballToAdd += ballsCarried

        ballToAdd , ballsCarried = 0, 0
        for i in range(N-1,-1,-1):
            answer[i] += ballToAdd
            ballsCarried += int(boxes[i]) 
            ballToAdd += ballsCarried

        # print(answer)
        return answer
        