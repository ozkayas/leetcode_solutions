# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inOrderList = []

        def inOrder(node: TreeNode):
            if not node: return

            inOrder(node.left)
            self.inOrderList.append(node)
            inOrder(node.right)
        
        inOrder(root)

        # print(self.inOrderList)

        def createBalancedBST(inOrder: List, start: int, end: int):
            if start > end: return None
            mid = (start + end)//2

            midNode = inOrder[mid]
            midNode.left = createBalancedBST(inOrder, start, mid-1)
            midNode.right = createBalancedBST(inOrder, mid +1, end)

            return midNode
        
        return createBalancedBST(self.inOrderList, 0, len(self.inOrderList)-1)


        