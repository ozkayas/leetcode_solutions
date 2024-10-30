class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        # Can this word fit in the curLine and stay in maxWidth
        def canFit(word:str, curLine: List[str]) -> bool:
            n = len(curLine) # spaces needed
            curWidth = sum([len(w) for w in curLine])
            return curWidth + n + len(word) <= maxWidth

        def spaceBetweenWords(curLine: List[str], spaceCount: int) -> List[str]:
            # add spaces between all words
            newLine = []
            for i in range(len(curLine)-1):
                newLine.append(curLine[i])
                newLine.append(" "*spaceCount)
            newLine.append(curLine[-1])
            return newLine

        def adjustedLine(curLine: List[str]) -> str:
            newLine = []
            curWidth = sum([len(w) for w in curLine])
            spacesToDistribute = maxWidth - curWidth
            if len(curLine) == 1:
                newLine = [curLine[0] + " "*spacesToDistribute]
            else: # if there is only 1 line, just append
                spaceSpots = len(curLine) - 1
                count = spacesToDistribute//spaceSpots
                remainingSpaces = spacesToDistribute % spaceSpots

                # add spaces between all words
                newLine = spaceBetweenWords(curLine, count)

                # add remaining spaces 
                i = 1
                while remainingSpaces:
                    newLine[i] = newLine[i] + " "
                    i += 2
                    remainingSpaces -= 1

            return "".join(newLine)


        def adjustLastLine(curLine: List[str]) -> str:
            newLine = spaceBetweenWords(curLine, 1)
            curWidth = sum([len(w) for w in newLine])
            spacesToDistribute = maxWidth - curWidth
            newLine.append(" " * spacesToDistribute)
            return "".join(newLine)



        curLine = []
        for i, w in enumerate(words):
             #can we add this to currentline
            if canFit(w, curLine):
                curLine.append(w)
            else:
                # We can not append w, so process the curLine , then reset and add w
                line = adjustedLine(curLine)
                ans.append(line)
                curLine.clear()
                curLine.append(w)

        lastLine = adjustLastLine(curLine)
        ans.append(lastLine)

        return ans