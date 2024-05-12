from collections import Counter

def countUniqueStringAfterReversing(s:str)->int:
    N = len(s)
    count_c = Counter(s)    

    N = len(s)
    possibleAffectingSubs = N*(N-1) // 2
    count_c = Counter(s)    
    for curr_count in count_c.values():
        if curr_count > 1:
            possibleAffectingSubs -= curr_count*(curr_count-1) // 2  # remove all duplicated count
    return possibleAffectingSubs + 1     


print(countUniqueStringAfterReversing("abc"))
print(countUniqueStringAfterReversing("abca"))
print(countUniqueStringAfterReversing("abaa"))