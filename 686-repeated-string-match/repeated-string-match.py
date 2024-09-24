class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = ceil(len(b)/len(a))
        repeated_a = a*repeat
        if b in repeated_a:
            return repeat

        for r in range(2):
            repeated_a += a
            repeat += 1
            if b in repeated_a:
                return repeat
        return -1


"""
len(b) / len(a) min repetatoin needed
x = 8/4 = 2 en az
x = 7/4 = 3 en az -> ceil alacagiz , zaten daha azi kurtarmaz
bu durumda da, saga ve sola birer tane daha eklenebilir.

bu durumda en fazla toplam x + 2 repetation icerisinde kontrol edecegiz.

abcd abcd
d abcd abc
cd abcd ab
bcd abcd a


abcd abcd a
d abcd abcd
cd abcd abc
bcd abcd ab

abcd abcd ab
d abcd abcd a
cd abcd abcd
bcd abcd abcd
"""

