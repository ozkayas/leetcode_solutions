'''
A student is preparing for a test from amazon academy for a scholarship.

The student is required to completely read n chapters (which is the length of the pages array) for the test where the ith chapter has pages[i] number of pages. The chapters are read in increasing order of the index. Each day the student can either read till the end of a chapter or at the most x pages, whichever is minimum. The number of pages remaining to read decreases by x in the later case.

Note:

The test will be given in [days] number of days from now. Find the minimum number of the pages, x, which the student should read each day to finish all pages of all chapters within days number of days. If it is not possible to finish these chapters in days number of days, return -1.

Function Description

Complete the function findMinimumPagesPerDay in the editor.

findMinimumPagesPerDay has the following parameters:

int pages[n]: an array of integers representing the number of pages in each chapter
int days: the number of days to finish reading
Returns

int: the minimum number of pages to read each day, or -1 if it's not possible

Note: In one day, the student cannot read pages of more than one chapter. Thus, if a chapeter finishes, the next chapter starts only on the next day even if the num of pages read is less than x.

✨ Credit to ꒰ August ꒱ؘ ࿐ ࿔*:･ﾟ✨

Example 1:

Input:  pages = [5, 3, 4], days = 4
Output: 4 
Explanation:

Day 1: The student reads A pages of the first chapter - pages remaining = [1, 3, 4]

Day 2: The student can only read till the end of the first chapter - pages remaining = [0, 3, 4]

Day 3: The student can only read till the end of the chapter x = 4 pages, since 3<4, the student reads till the end of the chapter 2- pages remaining = [0, 0, 4]

Day 4: The student reads all the 4 pages of the last chapter - pages remaining = [0, 0, 0]
      
Example 2:

Input:  pages = [2, 3, 4, 5], days = 5
Output: 4 
Explanation:

If x = 4, the student would read the 1st, 2nd and 3rd chapters in 1 day each, and the 4th chapter in 2 days. The total num of days taken = 1 + 1 + 1 + 2 = 5, which is within the num of allowed days. If x is less than 4, the chapters cannot be finished within 5 days.
      
Example 3:

Input:  pages = [2, 3, 4], days = 4
Output: 3 
Explanation:



Thus, in 4 days, the student can read all pages of all chapters and finish.

If x is less than 3, it is impossible to read all chapters in 4 days. Thus, the
minimum num of pages read each day is 3.
      
Constraints:
1 <= n <= 105
1 <= days <= 109
1 <= pages[i] <= 104
'''

def minimumNumberOfPages(pages, days):
    def totalDays(num_pages):
        total = 0
        for page_count in pages:
            total += (page_count + num_pages - 1) // num_pages
        return total
    
    low = 1
    high = max(pages)
    result = float('inf')
    
    while low <= high:
        mid = (low + high) // 2
        total = totalDays(mid)
        
        if total <= days:
            # OK but try to find a smaller solution
            result = min(result, mid)
            high = mid - 1
        else:
            low = mid + 1
            
    if result == float('inf'):
        return -1
    else:
        return result
    
print(minimumNumberOfPages([5, 3, 4], 4)) # output 4
print(minimumNumberOfPages([2, 3, 4, 5], 5)) # output 4
print(minimumNumberOfPages([2, 3, 4], 4)) # output 3