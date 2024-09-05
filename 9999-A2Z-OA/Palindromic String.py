# checks if these start and can be start and end of a palindrome, they may have different lengths
# abc, xdcba -> True
from typing import List


def maybePairs(start: str, end: str) -> bool:
    if len(start) <= len(end):
        return end[::-1].startswith(start)
    else:
        return start.startswith(end[::-1])


# print(maybePairs("abc", "xdcba")) # True
# print(maybePairs("abcdw", "ba")) # True
# print(maybePairs("axbcdw", "ba")) # True

ans = ''

def solution(arr: List[str], s: str, e: str) :
    global ans
    # Try to add a string inbetween the start and end of a palindrome
    for i in range(len(arr)):
        candidate = s + arr[i] + e
        if candidate == candidate[::-1] and len(candidate) > len(ans):
            ans = candidate

    # find a possible pair of start and end of a palindrome\
    # will hold tuples of possible start and end indices
    possiblePairIndices = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if maybePairs(arr[i], arr[j]):
                possiblePairIndices.append((i, j))
                if arr[i] == arr[j][::-1]:
                    candidate = arr[i]+arr[j]
                    if len(candidate) > len(ans):
                        ans = candidate

    if not possiblePairIndices:
        return

    print(possiblePairIndices)

    for i, j in possiblePairIndices:
        # remove the pair from the list and make a recursive call
        nextArr = arr[:]
        nextArr.pop(i)
        nextArr.pop(j-1)
        # to find the next pair
        solution(nextArr, s+arr[i], arr[j]+e)


solution(["applw", "racecar", "qpkos", "race", "car", "amkw", "jowgg"], "", "")
print(ans)
ans = ''
solution(["applw", "racecar", "qpkos", "racecar", "amkw", "jowgg"], "", "")
print(ans)
ans = ''
solution(["abab", "baba", "cbca", "cbba", "aaaa" ], "", "")
print(ans)
ans = ''
solution(["abc", "xdcba", "ab", "ba"], "", "")
print(ans)
ans = ''




