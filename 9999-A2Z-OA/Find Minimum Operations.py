'''
https://www.fastprep.io/problems/amazon-find-minimum-operations
Amazon Web Services (AWS) stores grayscale images as an array of white and black pixels. 
The image is stored as a binary string where a white pixel is represented by '1', and a black pixel is represented by '0'. 
The reverse of the image is represented as the reverse of this binary representation. For example, the reverse of "11010" is "01011". 
They want to store the reverse of each image as a backup. 
In order to reproduce the reverse from the original, the following operation can be performed any number of times: 
remove any character from the string and append it to the end of the string, i.e., choose any pixel and shift it to the end of the string.

Given the binary representation of pixels denoted by image, find the minimum number of operations needed to produce its reverse.

Function Description

Complete the function findMinimumOperations in the editor.

findMinimumOperations has the following parameter:

String image: a binary string that represents an image
Returns
int: the minimum number of operations required to produce a reverse, i.e., to reverse the string.

Example 1:
Input:  image = "0100110"
Output: 3 
Explanation:
The reverse of the image, i.e., the reverse of the string, is "0110010", and it can be produced using the sequence of operations shown in the image above 👆😳:
The string cannot be reversed in fewer than 3 operations. Return 3.

'''

def solve(s):
    n = len(s)
    rev = s[::-1]
    lp = 0
    for i in range(n):
        if s[i] == rev[lp]:
            lp += 1
    return n - lp

print(solve('abbaba'))

# "a b b a b a"
# "a b a b a b"
# "a b a b b a"
                                # "a b a b a b
                                # "a a b a b b
                                # "a b a b b a


# "a b a b b a"