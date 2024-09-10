from collections import defaultdict

from Scripts import count_palindromic_substrings as helper
# def countDistinctPasswords(password: str) -> int:
#     N = len(password)
#     totalSubs = N * (N + 1) // 2
#
#     totalSubPalindromes = helper.countPalindromicSubs(password)
#     print(f"totalSubPalindromes: {totalSubPalindromes}")
#
#     return totalSubs - totalSubPalindromes +1

# This is N2 solution
def countDistinctPasswords(s):
    ans = 1
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                ans += 1
    return ans


# This is N solution
def countDistinctPasswords2(s):
    counter = defaultdict(int)
    ans = 1

    for i in range(len(s) - 1, -1, -1):
        counter[s[i]] += 1
        ans += len(s) - i - counter[s[i]]

    return ans

print(countDistinctPasswords("abc")) # 4
print(countDistinctPasswords("abaa")) # 4
print(countDistinctPasswords("abca")) # 6
print(countDistinctPasswords("daadacca")) # 21
# print(countDistinctPasswords2("abc")) # 4
print(countDistinctPasswords2("abaa")) # 4
# print(countDistinctPasswords("abca")) # 6
# print(countDistinctPasswords2("daadacca")) # 21
