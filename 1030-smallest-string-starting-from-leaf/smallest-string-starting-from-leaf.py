# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isLeaf(self, node:TreeNode) ->bool:
        return not node.left and not node.right


    def toChar(self, num:int) -> str:
        if num > 26 or num < 0:return ''

        base = ord("a")
        return chr(base + num)


    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = self.toChar(26)
        print(self.isLeaf(root))

        def dfs(node, s):
            cur_str = s + self.toChar(node.val)
            # print("entered dfs s - node.val", s,"-" ,self.toChar(node.val))
            if self.isLeaf(node):
                
                candid_str = (cur_str)[::-1]
                # print("candid_str, curans", candid_str, self.ans)
                if candid_str < self.ans:
                    self.ans = candid_str

                return

            if node.left:
                dfs(node.left, (cur_str)[:])

            if node.right:
                dfs(node.right, (cur_str)[:])            

        
        dfs(root, "")


        return self.ans
        