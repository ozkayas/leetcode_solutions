class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda p:p[1])
        arrows = 1
        end = points[0][1]
        for p in points[1:]:
            if end < p[0]:
                arrows += 1
                end = p[1]
            
        return arrows
        

    #     class Solution:
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     if not points:
    #         return 0
    #     points.sort(key=lambda x: x[1])
    #     arrows = 1
    #     end = points[0][1]
    #     for i in range(1, len(points)):
    #         if points[i][0] > end:
    #             arrows += 1
    #             end = points[i][1]
    #     return arrows




'''        points.sort(key = lambda item:item[1])

        # print(points)
        arrows = 0

        while points:
            ballonsToShot = []
            arrows += 1
            if (len(points))==1:
                return arrows

            # Find how many ballons can we shot together with the first one
            firstBalon = points.pop(0)
            for p in points:
                if p[0] <= firstBalon[1]:
                    ballonsToShot.append(p)

            # print(ballonsToShot)
            for b in ballonsToShot:
                points.remove(b)




        return arrows
'''