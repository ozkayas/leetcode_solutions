'''
The developers at Amazon are developing a regex matching library for their NLP use cases. A prototype regex matching has the following requirements:

The regex expression contains lowercase English letters, '(', ')', '.', and '*'.
'.' matches with exactly one lowercase English letter.
A regular expression followed by '*' matches with zero or more occurrences of the regular expression.
If an expression is enclosed in parentheses '(' and ')', it is treated as one expression and any asterisk '' applies to the whole expression. It is guaranteed that no expression enclosed within parentheses contains any '' but is always followed by '*'. Also, there is no nested brackets sequence in the given regex expression for the prototype.
For example:

Regex "(ab)*d" matches with the strings "d", "ababd", "abd", but not with the strings "abbd", "abab".
Regex "ab*d" matches with the strings "abbbd", "ad", "abd", but not with strings "ababd".
Regex "a(b.d)*" matches with the strings "abcdbcd", "abcdbed", "abed", "a" but not with strings "bcd", "abd".
Regex "(.)*" matches with the strings "a", "aa", "aaa", "b", "bb" and many more but not "ac", "and", or "bcd" for example.
Given an array, arr, of length k containing strings consisting of lowercase English letters only and a string regex of length n, for each of them find whether the given regex matches with the string or not and report an array of strings "YES" or "NO" respectively.

Example:

Suppose, n = 8, regex = '(a.b)*bd', k = 3, arr = ['acbabbbd', 'bd', 'abbd']

arr[0] = "acbabbbd" matches the regex "(a.b)bd", if we replace '' with 2 occurrences of "a.b", i.e. it becomes "a.ba.bbd". Now, replace both '.' with 'c' and 'b' respectively.
arr[1] = "bd" matches the regex "(a.b)bd", if we replace '' with 0 occurrences of "a.b", i.e. it becomes "bd".
arr[2] = "abbd" doesn't matches the regex "(a.b)*bd".
Hence, the answer is ["YES", "YES", "NO"].
'''

