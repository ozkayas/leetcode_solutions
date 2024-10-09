class Solution:
    def myAtoi(self, s: str) -> int:

        isNegative = False
        res = 0
        i = 0
        # Skip any whitespaces
        while i < len(s) and s[i] == " ":
            i += 1

        if i == len(s):
            return 0
        # Is first ch valid?
        if s[i] not in ["+","-"] and not s[i].isdecimal():
            return 0

        # Process sign
        if s[i] == "-": 
            isNegative = True
            i += 1
        elif s[i] == "+":
            i += 1

        while i < len(s):
            if not s[i].isdigit(): 
                break
            res = res * 10 + int(s[i])
            i += 1

        # 32-bit integer sınırlarını kontrol et (opsiyonel)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if isNegative:
            res = -res
            if res < INT_MIN:
                return INT_MIN
        else:
            if res > INT_MAX:
                return INT_MAX

        return res
        