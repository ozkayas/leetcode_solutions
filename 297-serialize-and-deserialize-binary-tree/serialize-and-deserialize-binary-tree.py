# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return "#"
        output = []
        bfsQ = deque([root])
        while bfsQ:
            cur = bfsQ.popleft()
            output.append(str(cur.val) if cur else "#")
            if cur:
                bfsQ.append(cur.left)
                bfsQ.append(cur.right)
        return ",".join(output)

    def deserialize(self, data):
        if data == "#": return None
        
        data = data.split(",")
        i = 0
        root = TreeNode(data[i])

        bfsQ = deque([root])
        while bfsQ:
            cur = bfsQ.popleft()
            # Read children from data and continue building tree
            i += 1
            if i < len(data) and data[i] != "#":
                leftChild = TreeNode(data[i])
                bfsQ.append(leftChild)
                cur.left = leftChild
            i += 1
            if i < len(data) and data[i]  != "#":
                rightChild = TreeNode(data[i])
                bfsQ.append(rightChild)
                cur.right = rightChild
        
        return root
   

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))