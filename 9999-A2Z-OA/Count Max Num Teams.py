from typing import List

def teams(skill: List[int], size: int, diff: int) -> int:
    teamCounter = 0
    skill.sort()
    
    l, r = 0, 0
    
    while l < (len(skill)-size+1):
        r = l + (size - 1)
        
        if skill[r] - skill[l] <= diff:
            # Found a good team
#             print(l,r)
            teamCounter += 1
            l = r +1
            r = l
        else:
            l += 1
            
    return teamCounter