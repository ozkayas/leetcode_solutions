"""Given a binary string S,
perform tthe following operation on S any number of times ( possibly zero):
select an index i such taht S[i] is equal to 1 and S[i+i] is equal to 0 , then remove either S[i] or S[i+1] from S.
Find the smallest string S that you can get after performing operations on S.

Any similar question to this one?

If there are multiple smallest strings possible then return the string which is lexicographically smallest.
"""

def smallestString(s: str) -> str:
    remainingZeros = 0
    for ch in s:
        if ch == "0":
            remainingZeros += 1

    stack = []
    for ch in s:
        if len(stack) == 0 or ch == "1":
            stack.append(ch)
        else:
            if stack and stack[-1] == "1":
                if remainingZeros > 1:
                    remainingZeros -= 1
                else:
                    # this is the last 0, so remove all 1s until here
                    while stack and stack[-1] == "1":
                        stack.pop()
                    stack.append(ch)
            else:
                stack.append(ch)

    return "".join(stack)


print(smallestString("000111"))
print(smallestString("101010"))
print(smallestString("1101010"))
