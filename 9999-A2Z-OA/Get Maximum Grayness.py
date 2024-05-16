'''
Get Maximum Greyness
Several satellites provide observational black and white images which are stored in data centers at Amazon Web Services (AWS).

A black and white image is composed of pixels and is represented as an n x m grid of cells. Each cell has a value of 0 or 1, where 0 represents a white pixel and 1 represents a black pixel. The grayness of a cell (i, j) is affected by the pixel values in the ith row and the jth column. More formally, the grayness of the cell (i, j) is the difference between the number of black pixels in the ith row and the jth column and the number of white pixels in the ith row and the jth column.

Find the maximum grayness among all the cells of the grid.

Note: The value of cell (i, j) is counted both in the ith row and in the jth column.

Function Description

Complete the function getMaximumGreyness in the editor.

GetMaximumGreyness has the following parameter:

string pixels[n]: a grid of pixels, where the ithstring consists of m characters and represents the ithrow of pixels.
Returns

int: the max greyness of the grid of pixels.
*** 👑 Credit to kcho 👑 ***

Example 1:

Input:  pixels = ["1010", "0101", "1010"]
Output: 1 
Explanation:

The n x m = 3 x 4 grid of pixels looks like this:

      1  0  1  0

      0  1  0  1

      1  0  1  0
    
The grayness of each cell is:
  
      1  -1  1  -1

      1  -1  1  -1

      1  -1  1  -1

The maximum achievable grayness is 1.

Example 2:

Input:  pixels = ["011", "101", "001"]
Output: 4 
Explanation:

The 3 x 3 grid of pixels looks like this:

      0  1  1

      1  0  1

      0  0  1
  
The grayness of each cell is:
  
      0  0  4

      0  0  4

     -2 -2  2
    
The maximum achievable grayness is 4.
'''

def getMaximumGreyness(pixels) -> int:
    R, C = len(pixels), len(pixels[0])
    # Counter of 1 & 0 in each row and c
    # 
    rSum = [[0,0] for i in range(R)] # [[2,1], [2,1], [1,2]] for the second example
    cSum = [[0,0] for i in range(C)]  # [[1,2]  [1,2]  [3,0]]

    for r in range(R):
        for c in range(C):
            color = pixels[r][c]
            if color == "1":
                rSum[r][0] += 1
                cSum[c][0] += 1
            else:
                rSum[r][1] += 1
                cSum[c][1] += 1

    print(rSum, cSum)

    maxGreyness = float("-inf")
    for r in range(R):
        for c in range(C):
            black = rSum[r][0] + cSum[c][0]
            white = rSum[r][1] + cSum[c][1]

            maxGreyness = max(maxGreyness, (black-white))

    return maxGreyness

print(getMaximumGreyness(["011", "101", "001"]))
print(getMaximumGreyness(["1010", "0101", "1010"]))