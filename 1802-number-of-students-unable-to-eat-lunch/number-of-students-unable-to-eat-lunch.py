from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        std = deque(students)
        sand = deque(sandwiches)
        allowed_ro = len(std) 
        ro  = 0

        while sand and ro < allowed_ro:
            if std[0] == sand[0]:
                sand.popleft()
                std.popleft()
                allowed_ro -= 1
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