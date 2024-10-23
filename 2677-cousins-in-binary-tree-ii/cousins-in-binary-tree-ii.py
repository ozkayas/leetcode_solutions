# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
      
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum = defaultdict(int)
        levelParent = defaultdict(lambda: defaultdict(list))
        # for each node put hold also level and parent : (node, level, parent)
        bfs = deque([(root, 0, None)])
        while bfs:
            cur, level, parent = bfs.popleft()
            levelSum[level] += cur.val
            if level < 2:
                cur.val = 0
            if level > 1:
                levelParent[level][parent].append(cur)
            if cur.left:
                bfs.append((cur.left, level+1, cur))
            if cur.right:
                bfs.append((cur.right, level+1, cur))


        # Process values
        for level in levelParent.keys():
            sm = levelSum[level]
            for parent, children in levelParent[level].items():
                siblingSum = sum([child.val for child in children])
                cousinsSum = sm - siblingSum
                for child in children:
                    child.val = cousinsSum

        return root   