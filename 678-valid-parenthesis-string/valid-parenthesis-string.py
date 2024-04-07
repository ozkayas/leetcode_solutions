class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = [] # stack ( ) with indices
        wc = []  # stack indices of *

        for i,c in enumerate(s):
            if c == "*":
                wc.append((i))
            elif c == "(":
                stack.append((c, i))
            else:
                # pair if we can and pop the opener
                if stack and stack[-1][0] == "(":
                    stack.pop()
                # Use if any wildcare in the stack use it
                elif wc:
                    wc.pop()
                # Can not balance this closer until this point, so we can never, reutnr False
                else:
                    return False
            
            print(stack, wc)

        if len(stack) == 0: # all ) are balanced either with ( or *
            return True

        else:
            # there are unbalanced ( s
            # These may be like  * * * ( ( ( and can not be balanced of like ( ( * * and we can balance,
            # So we need to check with indices
            # Actually we can use the same algo in reverse and solve also
            # But trying to finish with indices

            if len(stack) > len(wc):
                return False # not enough * to balance ( chars
            while stack:
                item, last_ind = stack.pop()
                last_wc_index = wc.pop()
                if last_ind > last_wc_index:
                    return False
            
            return True

                    




'''
* : 1
stack : (

* * * ( ( ( ( ) ) 
i

'''