'''
1. Amazon Transaction Logs
Your Amazonian team is responsible for maintaining a monetary transaction service. The transactions are tracked in a log file.

A log file is provided as a string array where each entry represents a transaction to service. Each transaction consists of:

sender user id: Unique identifier for the user that initiated the transaction. It consists of only digits with at most 9 digits.
recipient user id: Unique identifier for the user that is receiving the transaction. It consists of onlv digits with at most 9 digits
amount of transaction: The amount of the transaction It consists of only digits with at most 9 digits
The values are separated by a soace. For example. "sender user id recipient user_id amount of_transaction".

Users that perform an excessive amount of transactions might be abusing the service so you have been tasked to identify the users that have a number of transactions over a threshold. The list of user ids should be ordered in ascending numeric value

Example
logs = ["88 99 200", "88 99 300", "99 32 100" " 12 12 15"}
threshold = 2

The transactions count for each user, regardless of role are:

ID	Transartione
99	3
88	4
12	1
32	1
There are two users with at least threshold = 2transactions: 99 and 88. In ascending order, the return array is /'88', '99').
Note: In the last log entry, user 12 was on both sides of the transaction. This counts as only 1 transaction for user 12.

Function Description
Complete the unction process/ os in the editor below.

The function has the following parameter(s):

string logs[n] each logs[i] denotes the ith entry in the logs
int threshold: the minimum number of transactions that a user must have to be included in the result
Return

string[]: an array of user id's as strings, sorted ascending by numeric value
Constraints

1 <= n <= 10^5
1 <= threshold <= n
The sender user id, recipient user id and amount of transaction contain only characters in the range ascii['0'-'9'].
The sender user id, recipient user id and amount of transaction start with a non-zero digit.
0 < enath or sender user Id, recipient user lo, amount or transaction <= 9
The result will contain at least one element.
Sample Input 1

size n = 4;
logs[] = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
threshold = 2
Sample Output 1

1
2
Explanation

ID	Transartione
1	3
2	2
7	1
3	1
Only users 1 and 2 have at least threshold = 2 transactions. The return arrav in numericallv ascending order is f"1" "2"7. Note that in the last log entry the user with id a pertormed both roles in the transaction. This is counted as one transaction for the user

Sample Input 2

size n = 4;
logs[] = ["9 7 50", "22 7 20", "33 7 50", "22 7 30"]
threshold = 3
Sample Output 2

7
Explanation

ID	Transartione
9	1
7	4
22	2
33	1
Only user 7 has 3 or more transactions The return array is ["7"]
'''