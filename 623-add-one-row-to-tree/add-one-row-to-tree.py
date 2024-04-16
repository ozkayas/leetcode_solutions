# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        ## TODO: Implement Edge case for depth == 1
        if depth == 1:
            newRoot = TreeNode(val, root, None)
            return newRoot

        stack = deque([(root,1)])

        while stack:
            curNode, curDep = stack.popleft()

            if curDep == depth-1:
                newLeft = TreeNode(val, curNode.left, None)
                newRight = TreeNode(val, None, curNode.right)
                curNode.left = newLeft
                curNode.right = newRight
    

            elif curDep >= depth:
                break

            else:
                #not yet reached the desired level
                if curNode.left:
                    stack.append((curNode.left, curDep+1))
                if curNode.right:
                    stack.append((curNode.right, curDep+1))


        return root