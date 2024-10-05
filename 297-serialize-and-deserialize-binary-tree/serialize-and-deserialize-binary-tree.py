# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # Level order traverse, ser = "123##45####"
        serialList = []
        bfsStack = deque([root])
        while bfsStack:
            cur = bfsStack.popleft()
            if not cur:
                serialList.append("#")
                continue
            else:
                serialList.append(str(cur.val))
            bfsStack.append(cur.left)
            bfsStack.append(cur.right)
        # print("".join(serialList))
        return ",".join(serialList)

    def deserialize(self, data):
        if not data: return None
        tokens = data.split(",")
        if tokens[0] == "#": return None

        root = TreeNode(int(tokens[0]))
        if len(tokens) == 1: return root
        bfs = deque([root])
        i = 1
        
        while bfs and i < len(data):
            cur = bfs.popleft()
            if i < len(tokens) and tokens[i] != "#":
                cur.left = TreeNode(tokens[i])
                bfs.append(cur.left)
            i += 1
            if i < len(data) and tokens[i] != "#":
                cur.right = TreeNode(tokens[i])
                bfs.append(cur.right)
            i += 1

        return root 




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))