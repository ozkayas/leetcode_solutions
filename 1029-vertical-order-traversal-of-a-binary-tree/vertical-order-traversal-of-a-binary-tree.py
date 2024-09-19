# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)

        st = deque([(root, 0, 0)])

        while st:
            curNode, level, col = st.popleft()
            nodes[col].append((curNode, level))

            if curNode.left:
                st.append((curNode.left, level+1, col-1))
            if curNode.right:
                st.append((curNode.right, level+1, col+1))
            
        minCol, maxCol = min(nodes.keys()), max(nodes.keys())
        ans = [] 
        for col in range(minCol, maxCol+1):
            nodes[col].sort(key = lambda item:(item[1],item[0].val))
            ans.append([node[0].val for node in nodes[col]])
        return ans

        