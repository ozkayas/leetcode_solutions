# Iterative DFS
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        if not root: 
            return ""
        queue = [root]
        while queue:
            cur = queue.pop()
            if not cur:
                ans.append("n")
                continue
            ans.append(str(cur.val))
            queue.append(cur.right)
            queue.append(cur.left)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = deque(data.split(","))
        root = TreeNode(int(data.popleft()))
        # If a node in the queue, it is waiting for children to be attached to it. We will add left and right,
        queue = [(root, 0)]
        while data:
            if not queue:
                # this would be an error case
                return None
            cur = data.popleft()
            # Create a new Node or None and try to attach it as left or right of a parent
            if cur == "n":
                val = None
            else:
                val = TreeNode(int(cur))
            
            parent, cnt = queue.pop()
            if cnt == 0:
                parent.left = val
            else:
                parent.right = val
            cnt += 1
            if cnt < 2:
                queue.append((parent, cnt))
            
            # We attached this to a parent , but if it is actually a Node, it will be a parent also, so add to queue
            # If 0, it is waiting for a left child, if 0 it is waiting for a right child 
            if val:
                queue.append((val, 0))
        return root



# Iterative BFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        if not root: 
            return ""
        stack = deque([root])
        while stack:
            cur = stack.popleft()
            if not cur:
                ans.append("n")
                continue
            ans.append(str(cur.val))
            stack.append(cur.left)
            stack.append(cur.right)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = deque(data.split(","))
        root = TreeNode(int(data.popleft()))
        stack = deque([root])
        cnt = 0
        while data:
            if not stack:
                # this would be an error case
                return None
            cur = data.popleft()
            if cur == "n":
                val = None
            else:
                val = TreeNode(int(cur))
                stack.append(val)

            if (cnt % 2) == 0:
                stack[0].left = val
            else:
                stack[0].right = val
                stack.popleft()
            cnt = (cnt+1)%2
        return root