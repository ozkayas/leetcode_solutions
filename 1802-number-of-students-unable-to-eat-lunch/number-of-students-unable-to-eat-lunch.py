from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        std = deque(students)
        sand = deque(sandwiches)
        ro  = 0

        while sand and ro < len(sand):
            if std[0] == sand[0]:
                sand.popleft()
                std.popleft()
                ro = 0
            else:
                std.rotate(-1)
                ro += 1

        if not sand:
            return 0
        else:
            return ro
        

'''
allowed_ro = 3 // update it after each pop
ro = 3

[1,1,1,0,0,1]
[1,0,0,0,1,1]

[0,0,1 1 1]
[0,0,0,1,1]

[1 1 1]
[0,1,1]


'''