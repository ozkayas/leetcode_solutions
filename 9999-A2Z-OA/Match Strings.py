"""Match Strings 🍑 (Amazon CN)
🤘 INTERN
Amazon is developing an efficient string matching library. Develop a prototype service that matches a simple pattern with a text. There are two arrays of strings, text, and pat, each of size n. Each string in pat is a regex expression that contains exactly one wildcard character (*).

A wildcard character (*) matches any sequence of zero or more lowercase English letters. A regex matches some string if it is possible to replace the wildcard character with some sequence of characters such that the regex expression becomes equal to the string. No other character can be changed. For example, regex "abc*bcd" matches "abcbcd", "abcefgbcd" and "abccbcd" whereas it does not match the strings "abcbd", "abzbcd", "abcd".

For every i from 1 to n, your task is to find out whether pat[i] matches text[i]. Return the answer as an array of strings of size n where the ith string is "YES" if pat[i] matches text[i], and "NO" otherwise.

Note: The implementation shall not use any in build regex libraries."""

from Scripts.kmp_lsp import KMPSearch

# output = ["" for i in text]
def matchStrings(text: str, pat: str):

    # for i in range(len(pat)):
    #     leftPat, rightPat = pat[i].split("*")
    #     l_pat_size = len(leftPat)
    #     r_pat_size = len(rightPat)
    #     # print(leftPat, text[i][0:l_pat_size])
    #     # print(rightPat, text[i][-r_pat_size:])
    #     if leftPat == text[i][0:l_pat_size] and rightPat == text[i][-r_pat_size:]:
    #         output.append("YES")
    #     else:
    #         output.append("NO")

    leftPat, rightPat = pat.split("*")
    # Search for leftPat in text;
    leftFound, li, lj = KMPSearch(leftPat, text)
    if not leftFound:
        return False
    rightPat = rightPat[::-1]
    # Search for rightPat in text;
    rightFound, ri, rj = KMPSearch(rightPat, text[::-1])
    if not rightFound:
        return False

    # If both left and right are found, we must check if they overlap
    if li + len(leftPat) <= len(text) - rj:
        return True

    return False

print(matchStrings("hackerrank","hac*rank"))
print(matchStrings("abcbcd","abc*bcd"))
print(matchStrings("abcdefbcd","abc*bcd"))
print(matchStrings("abccbcd","abc*bcd"))
print(matchStrings("aaxsdfabccbcdxx","abc*bcd"))
print(matchStrings("abcbd","abc*bcd"))
print(matchStrings("abzbcd","abc*bcd"))
print(matchStrings("abcd","abc*bcd"))
