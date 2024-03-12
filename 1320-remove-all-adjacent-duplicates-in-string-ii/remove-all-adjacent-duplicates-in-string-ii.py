class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #will hold char and repeated number
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append([char,1])
                continue
            
            if stack[-1][0] != char:
                stack.append([char,1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                        stack.pop()
                    
        
        return "".join([char*count for char,count in stack ])





