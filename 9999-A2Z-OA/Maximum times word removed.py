'''
Maximum Times Word Removed
🤘 INTERN
Amazon Engineering maintains a large number of logs of operations across all products. A software engineer is debugging an issue in a product. An efficient way to analyze logs is to write automated scripts to check for patterns. The engineer wants to find the maximum number of times a target word can be obtained by rearranging a subset of characters in a log entry.

Given a log entry s and target word t, the target word can be obtained by selecting some subset of characters from s that can be rearranged to form string t and removing them from s. Determine the maximum number of times the target word can be removed from the given log entry.

Note: Both strings s and t consist only of lowercase English letters.

Function Description

Complete the function maximumTimesWordRemoved in the editor.

maximumTimesWordRemoved has the following parameters:

String s: a log entry
String t: a target word
Returns

int: the maximum number of times the target word can be removed
࣪𓏲ּ ᥫ᭡ ₊ ⊹ Credit to kchoˑ ִֶ 𓂃🌼

Example 1:

Input:  s = "abacbc", t = "bca"
Output: 2 
Explanation:


All characters were removed from s.

✎, Credit to ketchup 🍅♡˳ >ᴗ< 
  
      
Example 2:

Input:  s = "abdadccacd", t = "edac"
Output: 0 
Explanation:

It is not possible to form the target word t from the characters in s.
'''

from collections import Counter


def maximumTimesWordRemoved(s, t) -> int:
    if len(s) == 0: return 0

    sFreq = Counter(s)
    tFreq = Counter(t)

    # For each char in t, how many words are can be created with sfreq
    # ie/ if tFreq[a] = 2 and sFreq[a] = 6 -> we can create 6/2 = 3 words, a has a capacity of 3 word
    capacity = dict()

    for t in tFreq.keys():
        c = sFreq[t] // tFreq[t]
        capacity[t] = c

    # find the bottleneck
    
    return min(capacity.values())


print(maximumTimesWordRemoved("abacbc", "bca"))
print(maximumTimesWordRemoved("monomonnom", "nom"))