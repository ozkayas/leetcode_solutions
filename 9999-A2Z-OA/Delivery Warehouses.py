'''
Amazon has multiple delivery centers and delivery warehouses all over the world! The world is represented by a number line from -10^9 to 10^9 There are in delivery centers, the one at location center[i]. A location x is called a suitable location for a warehouse if it is possible to bring all the products to that point by traveling a distance of no more than d. At any one time, products can be brought from one delivery center and placed at point x. Given the positions of delivery centers, calculate the number of suitable locations in the world. That is, calculate the number of points x on the number line (- 10 ^ 9 <= x <= 10 ^ 9) where the travel distance required to bring all the products to that point is less than or equal to d.

Note: The distance between point x and center[i] is |x| center[i], their absolute difference.

Example:

Given n = 3 center = [-2, 1, 0], d = 8

The various locations along with the distance traveled to bring all treasures at that point are

Locate the warehouse at -3 First bring products from center[0]-2 covering a distance of |-3 - (- 2) |=1 to reach the center and |- 3 - (- 2)| = 1 to return. Similarly we bring products from centers 1 and 2 to point -3 for total distance of 1+1+ 4 + 4 + 3 + 3 = 16 which is > d. This is not a suitable location.

Locate the warehouse at 0 total distance traveled is 2 * |0-(-2)| + 2*|0-1| + 2*|0-9| = 6 <= d This is a suitable location,

Locate the warehouse at -1 total distance traveled is 2 * |-1-(-2)| + 2*|-1-1| + 2*|-1-0| = 8 <= d This is a suitable location,

Locate the warehouse at 1 total distance traveled is 2 * |1-(-2)| + 2*|1-1| + 2*|1-0| = 8 <= d This is a suitable location,

The only suitable locations are (-1, 0, 1). Return 3.

Function Description:

Complete the function suitableLocations in the editor below.

suitableLocations has the following parameters:

int center[n]: the positions of delivery centers

long d: the maximum total travel distance for a suitable location

Returns

int: the number of suitable locations.

ex2: n= 4; center = [2, 6, 3, -4], d= 22
o/p2: 5

ex3: n= 3; center = [-3,2,2], d= 8
o/p3: 0
'''
### This is a binary search question, implement binary search on the set of possible answer set
## Like kooko eats banana

# center = [-2, 1, 0]
# d = 8

# center = [2, 6, 3, -4]
# d= 22

center = [-3,2,2]
d= 8


min_point = None
max_point = None

def total_d(wh):
    sum = 0
    for c in center:
        sum += abs(c - wh)*2
    return sum

center.sort()

##### Just found a valid point to use as a bound to be used int 2 binary searches
first_valid = None
for i in range(len(center)):
    if total_d(center[i]) <= d:
        first_valid = center[i]
        break
#### There is not suitable point, even in the range of center
if not first_valid:
    print("ans", 0)



# for i in range(l,r+1):
#     print(i, total_d(i))

#####  Binary search to find the first valid point from left side
l = center[0] - (d//2)
r = first_valid 

while l < r:
    mid = (l+r)//2
    
    if total_d(mid) > d:
        l = mid +1
    else:
        r = mid #not mid-1 because it is OK

min_point = l 
    
#####  Binary search to find the first 'IN-valid point' from right side
l = first_valid
r = center[-1] + (d//2)

while l < r:
    mid = (r+l)//2
    
    if total_d(mid) <= d:
        l = mid + 1
    else:
        r = mid #not mid-1 because it is OK

max_point = r-1


print("ans:", max_point-min_point+1)
