'''
X stores its data on different servers at different locations. From time to time, due to several factors, X needs to move its data from one location to another. This challenge involved keeping track of the locations of X's data and report them at the end of the year.

At the start of the year, X's data was located at n different locations. Over the course of the year, X's data was moved from one server to another m times. Precisely, in the ith operation, the data was moved from movedFrom[i] to movedTo[i]. Find the locations of the data after all m moving operations. Return the locations in ascending order.

Note:

It is guaranteed that for any movement of data :

There is data at movedFrom[i].
There is no data at movedTo[i].
Returns

int[]: the locations storing data after all moves are made, in ascending order.
Example 1:

Input:  locations = [1, 7, 6, 8], movedFrom = [1, 7, 2], movedTo = [2, 9, 5]
Output: [5, 6, 8, 9] 
Explanation:


Data begins at locations listed in locations. Over the course of the year, the data was moved three times.

Data was first moved from movedFrom[0] to movedTo[0], from 1 to 2. Next, it is moved from 7 to 9, and finally from location 2 to 5.
      
In the end, the locations where data is present are [5,6,8,9] in ascending order.
      
Example 2:

Input:  locations = [1, 5, 2, 6], movedFrom = [1, 4, 5, 7] , movedTo = [4, 7, 1, 3]
Output: [1, 2, 3, 6] 
Explanation:



(ignore the typo in the img)

The operations should be in order.

For example, 5 is in the output because the 1st operation moved data from 1->2.

Then in the following operation (3rd), the data is moved from 2->5


｡ﾟ•┈ 🌷, ᥫ᭡ Credit to ꒰ა Edward ໒꒱┈•  ｡ﾟ
      
Example 3:

Input:  locations = [1, 2, 3], movedFrom = [1, 2], movedTo = [5, 6]
Output:  [3, 5, 6] 
'''


from collections import defaultdict
from typing import List

def getFinalLocations(locations, movedFrom, movedTo) -> List[int]:
    ans = []
    fromTo = defaultdict(int)
    for i in range(len(movedFrom)):
        fromTo[movedFrom[i]] = movedTo[i]

    for i, l in enumerate(locations):
        cur = l
        while fromTo[cur] != 0:
            temp = fromTo[cur]
            fromTo[cur] = 0
            cur = temp

        ans.append(cur)
         
    return sorted(ans)
         


print(getFinalLocations([1, 7, 6, 8],  [1, 7, 2], [2, 9, 5]))
print(getFinalLocations([1, 5, 2, 6], [1, 4, 5, 7] , [4, 7, 1, 3]))
print(getFinalLocations([1, 2, 3], [1, 2], [5, 6]))