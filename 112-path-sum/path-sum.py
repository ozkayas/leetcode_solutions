# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        ans = False

        def isLeaf(node) -> bool:
            return not node.left and not node.right


        def dfs(node, sumUptoThis):
            nonlocal ans
            if not node or ans: return

            # print(f"node: {node.val}")
            # print(f"sumUptoThis: {sumUptoThis}")
            if (node.val + sumUptoThis) == targetSum and isLeaf(node):
                # print(f"found {node.val}")
                ans = True
                return
            else:
                dfs(node.left, node.val+sumUptoThis)
                dfs(node.right, node.val+sumUptoThis)

        dfs(root, 0)

        return ans
        