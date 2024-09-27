class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        O, C, OC = "(", ")", "()"

        # Slice s into sub valid pairs -> (..) / () / (..)
        def sliceIntoPairs(s: str) -> List[str]:
            pairs, st = [], []
            start = 0
            for i in range(len(s)):
                ch = s[i]
                if ch == O:
                    st.append(O)
                elif ch == C:
                    st.pop()
                    if not st:
                        pairs.append(s[start:i+1])
                        start = i+1 #Added a pair so reset start index for the next one
            return pairs

                        
        # returns score of given string as list,
        def score(s: str) -> int: 
            # Base case
            if s == OC:
                return 1

            sumOfScores = 0
            for pair in sliceIntoPairs(s):
                if pair == OC:
                    sumOfScores += 1
                else:
                    sumOfScores += 2 * score(pair[1:-1])
            
            return sumOfScores 

        
        # print(sliceIntoPairs("()"))
        # print(sliceIntoPairs("(())"))
        # print(sliceIntoPairs("(())()()"))

        return score(s)

        
            
