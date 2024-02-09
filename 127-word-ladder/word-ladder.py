class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = [(beginWord, 1)]
        wordListSet = set(wordList)

        while q:
            curWord, lvl = q.pop(0)
            

            #search a 1 letter neighbor in wordList, check if endWord or add to q if exists
            
            for i in range(len(curWord)):
                arrW = list(curWord)
                for c in [chr(i) for i in range(ord('a'), ord('z')+1)]:
                    if arrW[i] == c: continue

                    arrW[i] = c #ait , bit, cit, 
                    candidate = "".join(arrW)
                    # print(candidate)
                    
                    if candidate in wordListSet:
                        if candidate == endWord:
                            return lvl + 1
                        wordListSet.remove(candidate)
                        q.append((candidate, lvl+1))
                        
        
        return 0



        


        