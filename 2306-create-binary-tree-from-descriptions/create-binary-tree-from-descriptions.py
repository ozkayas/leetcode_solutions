# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # adj map parent: [leftChild, rightChild]
        adjMap = defaultdict(lambda : [None, None])
        children = set()
        root = None

        for desc in descriptions:
            parent = desc[0]
            child = desc[1]
            isLeft = desc[2] == 1

            if isLeft:
                adjMap[parent][0] = child
            else:
                adjMap[parent][1] = child
            children.add(child)

        # find root node, if a node is a parent but not a child, then it is the root
        for parent in adjMap.keys():
            if parent not in children:
                root = parent
                continue
        # print("root", root)
        
        rootNode = TreeNode(root, None, None)

        bfsDeq = deque([rootNode])

        while bfsDeq:
            curNode = bfsDeq.popleft()
            if adjMap[curNode.val][0]:
                curNode.left = TreeNode(adjMap[curNode.val][0])
                bfsDeq.append(curNode.left)
            if adjMap[curNode.val][1]:
                curNode.right = TreeNode(adjMap[curNode.val][1])
                bfsDeq.append(curNode.right)

        return rootNode



# 20: [15, 17] 
# 50: [20, 80] 
# 80: [19, None] 