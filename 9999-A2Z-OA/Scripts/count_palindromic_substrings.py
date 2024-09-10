# Counts the number of palindromic substrings in a given string
def countPalindromicSubs(s: str) -> int:
    res = 0

    for i in range(len(s)):
        res += countPalindromes(s, i, i)
        res += countPalindromes(s, i, i+1)

    return res

def countPalindromes(s: str, l: int, r: int) -> int:
    res = 0

    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1

    return res