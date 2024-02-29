# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque() 
        m = dict() #hMap to store latest visited value on a level m[level]
        q.append((root,0))

        while q:
            cur, level = q.popleft()
            #check if not approp, return False immedi
            if cur.val % 2 == 0 and level % 2 == 0: return False
            if cur.val % 2 == 1 and level % 2 == 1: return False

            if level not in m:
                m[level] = cur.val
                # print("Adding", cur.val, level)
            else:
                # Attn to decr and increasing
                if level % 2 == 0: #level is Even, must increase
                    if cur.val <= m[level]:
                        return False
                    else:
                        m[level] = cur.val
                else:
                    if cur.val >= m[level]:
                        return False
                    else:
                        m[level] = cur.val
                    
                    # print(m)

            # Nothing wrong for the current node, so add children to q
            if cur.left: q.append((cur.left, level+1))
            if cur.right: q.append((cur.right, level+1))

        return True
        
# we need a solution level by level => BFS
# keep track of levels, queue (node, level)
# for each level keep track of last visited value hashMap