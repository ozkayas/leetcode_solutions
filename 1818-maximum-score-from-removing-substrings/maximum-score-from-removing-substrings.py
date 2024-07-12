class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        filtered = list(s)
        totalScore = 0

        # gets the filtered list "bbaaabab"
        # apply the p:pattern using stack and calculate the score,
        # return filtered list with remaining chars in the original list
        def getScore(arr: List[str], p: str, point: int) -> (int, List[str]):
            score = 0   
            stack = []

            for ch in arr:
                if len(stack) == 0:
                    stack.append(ch)
                else:
                    if stack[-1] == p[0] and ch == p[1]:
                        score += point
                        stack.pop()
                    else:
                        stack.append(ch)
            return (score, stack)

        if x > y:
            score, filtered = getScore(filtered, "ab", x)
            totalScore += score
            score, filtered = getScore(filtered, "ba", y)
            totalScore += score
        else:
            score, filtered = getScore(filtered, "ba", y)
            totalScore += score
            score, filtered = getScore(filtered, "ab", x)
            totalScore += score
        
        return totalScore


'''
"cdbcbbaaabab"
bbbaaabab

''' 