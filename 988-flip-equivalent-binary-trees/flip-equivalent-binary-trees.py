# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are equivalent
        if not root1 and not root2: return True
        # If one of them is None, they are not equivalent
        if not root1 or not root2: return False
        # If the values do not match, they are not equivalent
        if root1.val != root2.val: return False

        bfs1 = deque([root1])
        bfs2 = deque([root2])

        while bfs1 and bfs2:
            cur1 = bfs1.popleft()
            cur2 = bfs2.popleft()
            if cur1.val != cur2.val:
                return False

            # Check left and right children, ensuring None values are handled
            left_vals_1 = {cur1.left.val if cur1.left else None, cur1.right.val if cur1.right else None}
            left_vals_2 = {cur2.left.val if cur2.left else None, cur2.right.val if cur2.right else None}

            if left_vals_1 != left_vals_2:
                return False

            # Ensure children are flipped if necessary to match cur2 structure
            if cur1.left and cur2.left and cur1.left.val != cur2.left.val:
                cur1.left, cur1.right = cur1.right, cur1.left

            if cur1.left:
                bfs1.append(cur1.left)
            if cur2.left:
                bfs2.append(cur2.left)
            if cur1.right:
                bfs1.append(cur1.right)
            if cur2.right:
                bfs2.append(cur2.right)

        return True

        