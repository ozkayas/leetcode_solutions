# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1

        # {2: [0, 3], 3: [1, 5]}
        levelNodes = defaultdict(list)

        st = deque([(root, 0, "")])

        while st:
            node, row, bi = st.popleft()
            if row > 0:
                levelNodes[row].append(int(bi,2))

            if node.left:
                st.append((node.left, row+1, bi+"0"))
            if node.right:
                st.append((node.right, row+1, bi+"1"))
            
        ans = 0
        for value in levelNodes.values():
            ans = max(ans, (value[-1]-value[0]+1))

        return ans