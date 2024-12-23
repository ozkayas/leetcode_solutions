class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfsQ = deque()
        bfsQ.append(root)

        level = 0
        while bfsQ:
            #if level even, fill children in a list then reverse
            if level % 2 != 0:
                values = []
                for r in bfsQ:
                    values.append(r.val)
                for r in bfsQ:
                    r.val = values.pop()
            for _ in range(len(bfsQ)):
                cur = bfsQ.popleft()
                if cur.left:
                    bfsQ.append(cur.left)
                if cur.right:
                    bfsQ.append(cur.right)
            level += 1

        return root
                    





        