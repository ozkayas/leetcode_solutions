class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def sort_algo(log):

            leftPart, rightPart = log.split(" ",1)
            if rightPart[0].isalpha():
                return (0, rightPart, leftPart)
            else:
                return (1,)



        return sorted(logs, key=sort_algo)    
        