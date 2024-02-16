class Solution:
    def sortVowels(self, s: str) -> str:
        res = list(s)
        vowels = {"e","E","a","A","i","I","o","O","u","U"}
        v = []

        for i,char in enumerate(s):
           if char in vowels:
               v.append((i,char))
            
        v.sort(key=lambda x:x[1])
        # print(v)
        # for i,c in v:
        #     print(i,c)
        #     res[i] = c
        for i,s in enumerate(res):
            if s in vowels:
                res[i] = v.pop(0)[1]
        
        return "".join(res)

            