class Solution:
    def sortVowels(self, s: str) -> str:
        res = list(s)
        vowels = {"e","E","a","A","i","I","o","O","u","U"}
        v = []

        for char in s:
           if char in vowels:
               v.append(char)
            
        v.sort()
        # print(v)
        # for i,c in v:
        #     print(i,c)
        #     res[i] = c
        for i,s in enumerate(res):
            if s in vowels:
                res[i] = v.pop(0)
        
        return "".join(res)

            