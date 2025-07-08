'''Find Security Level
👩‍🎓 NEW GRAD
🌟 OA
📚
RELATED PROBLEMS

Source said that the other problem 👇 in the same batch was for Newe Grad, so I assume this problem is for New Grad as well.

Segmentify: Minimum Subsegments 🦔
Amazon is launching a revolutionary security feature that incorporates an advanced antivirus program, adept at identifying and halting potential threats. This framework manages n active programs, each with a unique Program Identifier (PID).

The antivirus program evaluates the overall security risk of the system using a specialized algorithm.

• The algorithm analyzes contiguous subarrays of Program Identifiers (PIDs) represented by the array pid.
• For each subarray, it calculates the sum of the PIDs and divides this sum by a given integer k.
• The remainder obtained from this division is compared to the number of programs in the subarray.
• A subarray is flagged if the remainder equals the number of programs within it and is considered as malicious.
• The overall security risk is determined by the total count of such flagged subarrays.

Formally, given an array pid of size n, representing the PIDs of the programs running on the computer, and an integer k, with which remainder has to be checked. The task is to calculate the system's security risk level.

Note:
• Remainder is defined as the remaining part after performing the division. For example, the remainder of 13 with 5 is 3.
• A subarray is a continuous portion of an array. For example, in the array [5, 7, 9, 11], possible subarrays include [5, 7], [7, 9, 11], [11] etc. Note that a subarray maintains the original order of elements and consists of consecutive elements.

Function Description

Complete the function findSecurityLevel in the editor.

findSecurityLevel has the following parameters:

int pid[n]: an array of integers denoting the PIDs of the programs
int k: an integer with which remainder is checked
Returns

long: an integer denoting the overall security risk of the system

Example 1:

Input: pid = [1, 3, 2, 4], k = 4
Output: 2
Explanation:

      
There are 2 different malicious contiguous subarrays:


      

        
Subarray from index [0, 0] with pid given by: [1], the remainder of the sum of pid sum = 1 of the subarray (1) with k = 4 is 1, the remainder of 1 with 4 is 1, which is equal to the number of elements in the subarray, i.e., 1. Hence, this subarray is flagged.

        
Subarray from index [2, 3] with pid given by: [2, 4], the remainder of the sum of pid sum = 2 + 4 = 6 of the subarray with k = 4 is 2, which is equal to the number of elements in the subarray, i.e., 2. Hence, this subarray is flagged.

      

      
An example of a contiguous subarray is which is not flagged:


      

        
Subarray from index [0, 1] with pid given by: [3, 2] is not flagged because the remainder of the sum of PIDs = 3 + 2 = 5, whose remainder with k = 4 is 1, while there are 2 elements in the subarray. Hence, the subarray is not malicious.

      

      
Hence, the overall security risk of the system is 2. Thus, return 2 from the function.
'''

## SOLUTION
# Target subarrays can only have 1, 2 or 3 elements.
# So a simple loop over they array and look for 3 subs will lead to O(3*n) at most -> O(n)