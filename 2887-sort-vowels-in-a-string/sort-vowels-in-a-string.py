class Solution:
    def sortVowels(self, s: str) -> str:
        res = []
        vowels = {"e","E","a","A","i","I","o","O","u","U"}
        v = []

        for char in s:
            if char in vowels:
                res.append(".")
                v.append(char)
            else:
                res.append(char)
  
        v.sort()
        p = 0
        for i,s in enumerate(res):
            if s == ".":
                res[i] = v[p]
                p += 1
        
        return "".join(res)

            