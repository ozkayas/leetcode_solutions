"""
Data analysts at Amazon are analyzing a data set of n strings in the array dataSet[], each consisting of lowercase English letters. Each character in a string corresponds to a particular feature.

The information gain obtained by training a model with two strings, dataSet[i] and dataSet[j], is the difference between the lengths of the strings i.e., |len(dataSet[i]) - len(dataSet[j])|. To avoid too many overlapping features, two strings can be selected only if the number of common features between them does not exceed a given threshold, max_common_features. The number of common features here is equal to the number of common characters between the two strings. For example, "abc" and "bcd" have 2 common features 'b' and 'c'. While "aa" and "aaa" have two common features, the "a" two 'a' characters.

Given dataSet and max_common_features, determine the maximum information gain possible.
Function Description
getMaxInformationGain takes the following arguments:
String[] dataSet: the strings of features
int max_common_features: the maximum number of common features allowed between data points
Returns
int: the maximum possible information gain
Example 1:
Input:  dataSet = ["abofh", "ab", "mo"], max_common_features = 1
Output: 3
Explanation:
It is optimal to choose the strings "abofh" and "mo". Their number of common features is 1 ('o') and the information gain is |5 - 2| = 3.
Example 2:

Input:  dataSet = ["a", "bcdef"], max_common_features = 1
Output: 4
Explanation:
The two strings can be chosen. They do not share any common features and their difference in length is 4.
"""
from functools import cache
from typing import List

def canonical(s:str) -> List[int]:
    l = [0 for _ in range(26)]
    for ch in s:
        idxOfCh = ord(ch)-ord("a")
        l[idxOfCh] += 1

    return l

def commonChar(s1, s2) -> int:
    l1 = canonical(s1)
    l2 = canonical(s2)

    commons = 0
    for i in range(26):
        commons += min(l1[i], l2[i])
    return commons


def getMaxInformation(dataSet: List[str], mcf: int) -> int:
    dataSet.sort(key = lambda i:len(i))
    # print(dataSet)
    maxSoFar = 0

    @cache
    def dp(l:int, r:int ):
        nonlocal  maxSoFar
        diff = abs(len(dataSet[l]) - len(dataSet[r]))
        if diff < maxSoFar:
            return

        # First check if commons satisfied
        if(commonChar(dataSet[l], dataSet[r])) <= mcf:
            maxSoFar = diff

        dp(l+1, r)
        dp(l, r-1)

    dp(0, len(dataSet)-1)

    return maxSoFar



print(getMaxInformation(["a", "bcdef"], 1))
print(getMaxInformation(["abofh", "ab", "mo"], 1))
print(commonChar("abc","rr"))
