# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        bfsStack = deque([(root, 0)]) 
        # Fill the temp when push a node to bfsStack
        ans, temp = [], []

        def fillAns():
            isLevelEven = temp[-1][1] %2 == 0 
            if isLevelEven:
                ans.append([n.val for n,l in temp])
            else:
                ans.append([n.val for n,l in reversed(temp)])


        while bfsStack:
            cur, level = bfsStack.popleft()
            # add temp to ans if last level is different than this level
            if temp and temp[-1][1] != level:
                fillAns()
                temp.clear()
            
            temp.append((cur, level))
            if cur.left:
                bfsStack.append((cur.left, level+1))
            if cur.right:
                bfsStack.append((cur.right, level+1))
                
        fillAns()
        
        return ans


        