class Solution:
    def reverseParentheses(self, s: str) -> str:
        tempList = [""]

        for c in s:
            if c == "(":
                tempList.append("")
            elif c == ")":
                revWord  = (tempList[-1])[::-1]
                tempList.pop()
                tempList[-1] += revWord
            else:
                tempList[-1]+= c
            
        return tempList[-1]




'''
loop each char, 
if ( start adding a string to a list
if ) reverse last element and append to previous element, and remove last element

[""] 
["", ed, et, oc]
["", ed, etco]
["", edocte]
["", edocteel]
[""+leetcode] => 


'''