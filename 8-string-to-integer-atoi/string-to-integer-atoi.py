class Solution:
    def myAtoi(self, s: str) -> int:
        N = len(s)
        sign, number = 1, 0
        i = 0
        while i < N and s[i] == " ":
            i += 1
        if i == N:
            return number
        if s[i] in  {"-","+"}:
            sign = -1 if s[i] == "-" else 1
            i +=1
        
        while i < N and s[i] == "0":
            i += 1

        res = 0
        while i < N and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        # 32-bit integer sınırlarını kontrol et (opsiyonel)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if sign == -1:
            res = -res
            if res < INT_MIN:
                return INT_MIN
        else:
            if res > INT_MAX:
                return INT_MAX

        return res