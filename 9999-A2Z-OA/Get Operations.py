"""
There are n processes. The i-th process has resourcefi] number of resources. All the resourcefi] are distinct. The CPU wants the processes to be arranged in increasing order of their resource(i]. The CPU does several operations to get this.
In each operation, the CPU selects an integer x and a process with number of
resources = x. It then places all processes with resource values less than x before the
processes with resource values greater than or equal to x, maintaining their original order i.e. the relative order between processes having resource value less than x should be maintained and the same applies for processes having resource value greater than or equal to x.
Find the lexicographically smallest sequence of Xs that the CPU chooses, such that it takes the minimum number of operations to complete the task.
Note: If the minimum number of operations = 0, then return a sequence only
containing the integer -1.
Example
n = 6
resource = [6, 4, 3, 5, 2, 1]
CPU can achieve the minimum number of operations in the following way (underlined elements denote the processes that have less than x resources):
Choose x=2:
［6,4.3.5,2.1→11 6,4.3,5.2］

Choose x=3:
11. 6,4,3, 5.2-①26,4,3,5］
Choose x=4:
1 3, 6, 4, 3, 5]→ 1, 2, 3, 6, 4,5]
Choose =6:
1236,451-1234 5 6]
Minimum number of operations = 4, and the answer is (2, 3, 4, 6].
Function Description
Complete the function getOperations in the editor below. getOperations has the following parameters):
int resourcein]: Contains the number of resources of each process
Returns
int!: Lexicographically smallest sequence of Xs such that it takes the minimum number of operations to complete the task.
"""

## Redditte gordugum bir cozum. N2 karmasikliga sahip. Calisiyor
def getOperations(resources):
    res = []

    n = len(resources)
    sorted_resources = sorted(resources)

    while resources != sorted_resources:
        index = 0

        while index < n and resources[index] == sorted_resources[index]:
            index += 1

        if index < n:
            pivot = resources[index]
            res.append(pivot)

            left, right = [], []

            for value in resources:
                if value < pivot:
                    left.append(value)
                else:
                    right.append(value)

            resources = left + right

    return [-1] if not res else sorted(res)


from Scripts import find_left_min_greater

def getOperationsX(resources):
    left_min = find_left_min_greater.find_left_min_greater(resources)
    res = []

    i = len(resources) - 1
    while i > 0:
        # all nums are distinct so > is ok, next is bigger than current so we must transport current
        if resources[i-1] > resources[i]:
            pivot = left_min[i]
            res.append(pivot)
        i -= 1

    return res





if __name__ == "__main__":
    assert getOperations([6, 4, 3, 5, 2, 1]) == [2, 3, 4, 6]
    assert getOperations([15, 10, 14, 12, 13]) == [14, 15]
    assert getOperations([2, 4, 14, 10, 5, 3]) == [4, 10, 14]
    assert getOperationsX([6, 4, 3, 5, 2, 1]) == [2, 3, 4, 6]
    assert getOperationsX([15, 10, 14, 12, 13]) == [14, 15]
    assert getOperationsX([2, 4, 14, 10, 5, 3]) == [4, 10, 14]
