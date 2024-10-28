# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ans = []
        bfs = deque([root])
        level = 0
        while bfs:
            for _ in range(len(bfs)):
                cur = bfs.popleft()
                if len(ans) == level: # No item added to ans at this level yet
                    ans.append(cur.val)
                if cur.right:
                    bfs.append(cur.right)
                if cur.left:
                    bfs.append(cur.left)

            level += 1
        
        return ans


        