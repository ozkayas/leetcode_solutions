# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        levelOfX , levelOfY = -1, -2

        bfsQ = deque()
        bfsQ.append((root, 0))

        while bfsQ:
            curNode, level = bfsQ.popleft()
            # Edge case if x and y have same parent
            if curNode.left and curNode.right and set([curNode.left.val, curNode.right.val]) == set([x, y]):
                return False

            # Check if we found x or y
            if curNode.val == x:
                levelOfX = level
            if curNode.val == y:
                levelOfY = level

            if levelOfX == levelOfY:
                return True

            # Continue bfs ing
            if curNode.left:
                bfsQ.append((curNode.left, level+1))
            if curNode.right:
                bfsQ.append((curNode.right, level+1))

            
        return False
        