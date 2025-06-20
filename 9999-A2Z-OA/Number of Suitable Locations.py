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

# Calculate the total distance from a point to all other points
def totalDistance(wh, center):
    sum = 0
    for c in center:
        sum += abs(c - wh)*2
    return sum

def suitableLocations(center, d) -> int:
    center.sort()

    ##### Trying to found a valid point to use as a bound to be used in 2 binary searches
    ### Searching between the leftmost center and the rightmost center
    anyValid = None
    for i in range(len(center)):
        if totalDistance(center[i], center) <= d:
            anyValid = center[i]
            break

    #### There is not suitable point, even in the range of center
    if anyValid is None:
        return 0

    #####  Binary search to find the first valid point from left side
    # l is potentially the left bound, l can be valid but l-1 is not
    # r is a point we are sure is valid
    # 0000011111 , we are trying to find the first 1
    l = center[0] - (d // 2)
    r = anyValid

    firstValid = None
    while l <= r:
        mid = l + (r - l) // 2

        if totalDistance(mid, center) <= d:
            # we found a valid point, but maybe there is a better one,
            # so set this now and continue searching to the left
            firstValid = mid
            r = mid - 1
        else:
            l = mid + 1

    #####  Binary search to find the first 'IN-valid point' from right side
    # 1111100000 , we are trying to find the first 0
    l = anyValid
    r = center[-1] + (d//2)

    firstInvalid = None # first invalid at the right side
    while l <= r:
        mid = l + (r - l)//2

        if totalDistance(mid, center) <= d:
            l = mid + 1
        else:
            firstInvalid = mid
            r = mid - 1

    return firstInvalid - firstValid


print(suitableLocations([-2, 1, 0], 8))  # 3
print(suitableLocations([2, 0, 3, -4], 22))  # 5
print(suitableLocations([-3,2,2], 8))  # 0


# Write me a loop which will count starts between pipes and give me a map of the count of stars for pipe intervals
# for example |*|**|*** should return { [1,3]:1, [3,5]:2} because there is 1 star between 1 and 3 and 2 stars between 3 and 5
def countStars(s):
    count = {}
    start = None
    for i in range(len(s)):
        if s[i] == "|":
            if start is not None:
                count[(start, i)] = s[start+1:i].count("*")
                start = None
            else:
                start = i
    return count

print(countStars("|*|**|***"))  # { [1,3]:1, [3,5]:2

