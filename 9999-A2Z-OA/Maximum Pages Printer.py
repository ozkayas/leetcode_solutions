from collections import defaultdict
import heapq


def maximumPagesPrinter(pages, threshold):
  page_group = defaultdict(list)
  total = 0
  for i in range(len(threshold)) : 
    heapq.heappush(page_group[threshold[i]],-pages[i])
  for k,v in page_group.items() : 
    for j in range(k) : 
      if not v : break
      total += -heapq.heappop(v)
  return total


# Test cases
if __name__ == "__main__":
    assert maximumPagesPrinter([4, 1, 5, 2, 3], [3, 3, 2, 3, 3]) == 14
    assert maximumPagesPrinter([10, 20, 30], [1, 2, 3]) == 60
    assert maximumPagesPrinter([5, 10, 15], [2, 2, 2]) == 25
    print(" 😎 All test cases passed! 😎 \n")

'''
# Maximum Pages Printer
The engineering team at an Amazon fulfillment center is optimizing n high-performance printers, where each printer i can print pages[i] number of pages.

Each printer can be in exactly one of three states:
operational, idle, or suspended.

Printers initially start in an idle state and can be activated one by one.

However, if too many printers are active at once, some will get suspended due to their threshold limit defined by the suspension rule below.

Suspension Rule:
If there are at least x operational printers, all such printers i with threshold[i] ≤ x will get suspended and stop printing.

Task:
The goal is to determine the maximum number of pages that can be printed before printers get suspended.

Note:
Activating a printer with threshold[i] = x allows it to print pages[i] pages.
However, once at least x printers are active, their pages get printed first,
and then all the printers with threshold ≤ x will get suspended immediately.

Choosing the activation order carefully is therefore crucial to maximize the total printed pages before suspensions occur.

Pages = [4,1,5,2,3] Threshold = [3,3,2,3,3] and output being 14

Explanation
The optimal way to maximize the number of pages printed is as follows: (Assuming 1-based indexing)

Turn on the 4th printer, which prints 2 pages.
Since the number of operational printers is 1 and does not exceed the threshold for any printer, no printer is suspended.

Next, turn on the 3rd printer, which prints 5 pages.
Now, there are 2 operational printers.
Since the threshold for printer 3 is threshold[3] = 2, printer 3 gets suspended and stops functioning. So, now we have only 1 operational printer which is the 4th one.

Turn on the 1st printer, which prints 4 pages.
There are now 2 operational printers, and printer 1 remains functional as its threshold is threshold[1] = 3.

Finally, turn on the 5th printer, which prints 3 pages.
Now, there are 3 operational printers (printers 1, 4, and 5).
Since the thresholds for printers 1, 2, 4, and 5 are all less than or equal to 3, these printers get suspended and stop functioning.

Thus, the total number of pages printed is:

2 (from printer 4) + 5 (from printer 3) + 4 (from printer 1) + 3 (from printer 5) = 14 pages.
'''

