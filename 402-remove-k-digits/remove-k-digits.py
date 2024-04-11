from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        pop_counter = k

        for n in num:
            # print(list(stack))
            
            # empty any nums bigger than this and do this max k times
            while pop_counter and stack and stack[-1] > n:
                stack.pop()
                pop_counter -= 1

            stack.append(n)
        

        # Convert stack to string
        stack_as_string = "".join(stack)

        # Take the bottom n - k items of the string
        # n = 5 and k : 2 then we need max 3 elements [0:3]
        ans = stack_as_string[:(len(num)-k)]

        return ans.lstrip("0") or "0"


       



'''

 5 4 5 1 1 1 1 

       1 0 2 0 0 0   k : 0
         |

stack: 0 2 0 0 0    
pop: 


'''