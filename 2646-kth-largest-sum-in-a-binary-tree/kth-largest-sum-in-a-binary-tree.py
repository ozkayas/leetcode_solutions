# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        bfs = deque([root])
        sums = []

        levelProcessed = 0
        levelSum = 0
        while bfs:
            for _ in range(len(bfs)):
                cur = bfs.popleft()
                levelSum += cur.val 
                if cur.left: bfs.append(cur.left)
                if cur.right: bfs.append(cur.right)
            levelProcessed += 1
            sums.append(levelSum)
            levelSum = 0

        sums.sort()
        return sums[-k] if k <= len(sums) else -1

            

        