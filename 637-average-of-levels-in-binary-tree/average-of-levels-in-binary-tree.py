# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        values , counter = {},{}
        q = [(root, 0)]
        res = []

        while q:
            cur, level = q.pop(0)
            # print(cur.val, level)
            if level in values:
                values[level] += cur.val
                counter[level] += 1
            else: 
                values[level] = cur.val
                counter[level] = 1
    
            if cur.left:
                q.append((cur.left, level+1))
        
            if cur.right:
                q.append((cur.right, level+1))

        # print(values)
        # print(counter)
        for i in range(len(values)):
            # print(values[i], counter[i])
            res.append(values[i]/counter[i])

        return res