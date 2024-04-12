'''
Amazon's database doesn’t support very large numbers, so numbers are stored as a string of binary characters, '0' and '1'. Accidentally, a '!' was entered at some positions and it is unknown whether they should be '0' or '1'.
The string of incorrect data is made up of the characters '0', '1' and '!' where '!' is the character that got entered incorrectly. '!' can be replaced with either '0' or '1'. Due to some internal faults, some errors are generated every time '0' and '1' occur together as '01' or '10' in any subsequence of the string. It is observed that the number of errors a subsequence '01' generates is x, while a subsequence '10' generates y errors.
Determine the minimum total errors generated. Since the answer can be very large, return it modulo 109+7.
Note: A subsequence of a string is obtained by omitting zero or more characters from the original string without changing their order.
Hint: It can be proved that (a + b) % c = ((a% c) + (b % c)) % c where a, b, and c are integers and % represents the modulo operation.

Function Description

Complete the function getMinErrors in the editor.

getMinErrors has the following parameter(s):

String errorString: a string of characters '0', '1', and '!'
int x: the number of errors generated for every occurrence of subsequence 01
int y: the number of errors generated for every occurrence of subsequence 10
Returns

int: the minimum number of errors possible, modulo 109+7

Example 1:

Input:  errorString = "101!1", x = 2, y = 3
Output: 9 
Explanation:

If the '!' at index 3 is replaced with '0', the string is "10101". The number of times the subsequence 01 occurs is 3 at indices (1, 2), (1, 4), and (3, 4). The number of times the subsequence 10 occurs is also 3, indices (0, 1), (0, 3) and (2, 3). The number of errors is 3 * x + 3 * y = 6 + 9 = 15.
   
If the '!' is replaced with '1', the string is "10111". The subsequence 01 occurs 3 times and 10 occurs 1 time. The number of errors is 3 * x + y = 9.
      
The minimum number of errors is min(9, 15) modulo (109 + 7) = 9.  
      
Example 2:

Input:  errorString = "01!0", x = 2, y = 2
Output: 8 
Explanation:

The better string is 0100 with one substring 01 and two substrings 10 making total errors generate = 21 + 32 = 8 (p.s. 2 + 1 + 3 + 2 = 8 makes more sense to me... Many thanks inadvance if you could help clarify the calculation here 🤝)
      
Example 3:

Input:  errorString = "!!!!!!!", x = 23, y = 27
Output: 0 
Explanation:

There is a tie for the best string generated, 00000 or 11111, with zero substrings 01 or 10.
      
Constraints:
1<= len (errorString)<=105
0 <= x, y <= 105
s consists only of characters '0', '1', and 'l'


'''
from typing import List

MOD = 10 ** 9 + 7
# errorString = "101!1"
# x = 2
# y = 3

errorString = "01!0"
x = 2
y = 2

# errorString = "!!!!!!!"
# x = 23
# y = 27


#### HELPER METHODS ###
## Function that counts 0 & 1s succeding an index
def freq_counter(bits:List[int]) -> List[List[int]]:
    N = len(bits)
    freqs = [[0,0] for _ in range(N)] 
    for i in range(N-2,-1,-1):
        if bits[i+1] == 0:
            freqs[i][0] = freqs[i+1][0] + 1
            freqs[i][1] = freqs[i+1][1]
        else:
            freqs[i][1] = freqs[i+1][1] + 1
            freqs[i][0] = freqs[i+1][0]

    return freqs

# Function that calculate errors
def error_counter(bits:List[int], x:int, y:int) -> int:
    freqs = freq_counter(bits)
    # print(freqs)
    x_count , y_count = 0, 0
    for i, b in enumerate(bits):
        if b == 0:
            x_count += freqs[i][1]
        else:
            y_count += freqs[i][0]
    # print("01", x_count, "10", y_count)
    return ((x_count*x) % MOD + (y_count * y ) % MOD) % MOD
        

### MAIN CODE ####

# Put 0 and 1 instead of !
zero_case = [0 if c == "!" else int(c) for c in errorString]
one_case = [1 if c == "!" else int(c) for c in errorString]

# print(error_counter(zero_case,x,y))
# print(error_counter(one_case,x,y))

print("RESULT: ", min(error_counter(zero_case,x,y),error_counter(one_case,x,y)))


    
