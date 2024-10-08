'''
https://www.fastprep.io/problems/amazon-get-k-rep-value

The team of machine learning scientists at Amazon wants to improve Amazon's product recommendation system. 
Based on a user's purchase history, the objective is to generate some extensive features that will be given as input to the machine learning model. 
One of the new proposed features is a k-repetitiveness feature whose computation is described below.

The purchase history of a user with the products available on Amazon is available in the form of a string user_history 
where the ith character represents the category of the ith product purchased by the user. 
The length of string user_history is n. There is also a given integer k.

The value of the k-repetitiveness feature for the string user_history is defined as the maximum number of substrings of the given string 
such that some product category in that substring appeared at least k times.

Find the value of the k-repetitiveness feature for the given string user_history.

Note: A substring is a continuous subsegment of a string.

Function Description

Complete the function getkRepValue in the editor.

getkRepValue has the following parameters:

String user_history: the interaction history of the user
int k: the minimum occurrence of a product for a substring to be included in the k-repetitiveness feature
Returns

An integer denoting the value of the k-repetitiveness feature.

Example 1:

Input:  user_history = "ceccca", k = 3
Output: 7 
Explanation:

The only product that appears 3 times or more in the original string is 'c'. The substrings where the product 'c' appears 3 or more times are:

So, the value of the k-repetitiveness feature is 7.
  
      
Example 2:

Input:  user_history = "acaab", k = 3
Output: 2 
Explanation:

The only substrings that have some product appearing at least k times are "acaa" and "acaab".
 

'''
from collections import defaultdict

class Solution:

    def getkRepValue(self, s:str, k:int) -> int:
        ## Will hold indexes of chars, also to keep the freq
        ## ie; {c:[0,2,3,4] , e:[1]}
        indexTable = defaultdict(list)

        counter = 0
        foundKRepItem = False
        firstIndex = 0

        for i in range(len(s)):
            ch = s[i]
            indexTable[ch].append(i)

            if len(indexTable[ch]) >= k:
                #found repetitive, update
                foundKRepItem = True
                firstIndex = indexTable[ch][-k]
            
            if foundKRepItem:
                counter += firstIndex + 1


        return counter



# user_history,k  = "ceccca",  3
# user_history,k  = "acaab",  3
user_history,k  = "acaacc",  3  ## output: 4
user_history,k  = "acaaccb",  3  ## output: 6
user_history,k  = "acaaccbc",  3  ## output: 11

sl = Solution()
result = sl.getkRepValue(user_history,k)
print(result)