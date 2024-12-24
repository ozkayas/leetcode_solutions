# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def swapCount(arr) -> int:
            sorted_arr = sorted(arr)
            position = {val:index for index,val in enumerate(sorted_arr)}
            swaps = 0
            for i in range(len(arr)):
                numHere = arr[i]
                while position[numHere] != i:
                    correct_index = position[numHere]
                    # Swap
                    arr[i], arr[correct_index] = arr[correct_index], arr[i]
                    swaps += 1
                    numHere = arr[i]
                    
            return swaps

        bfs = deque()
        bfs.append(root)
        total = 0

        while bfs:
            level = []
            for _ in range(len(bfs)):
                node = bfs.popleft()
                level.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            total += swapCount(level)
            level.clear()

        return total
            


                



        