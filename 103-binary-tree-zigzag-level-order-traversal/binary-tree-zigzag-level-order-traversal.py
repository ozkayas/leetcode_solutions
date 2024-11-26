# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        bfsQ = deque([root])
        direction = 1
        while bfsQ:
            temp = []
            for _ in range(len(bfsQ)):
                cur = bfsQ.popleft()
                temp.append(cur.val)
                if cur.left:
                    bfsQ.append(cur.left)
                if cur.right:
                    bfsQ.append(cur.right)
                
            if direction == 1:
                output.append(temp)
            else:
                output.append(temp[::-1])
            
            direction *= -1

        return output
