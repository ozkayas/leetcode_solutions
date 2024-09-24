# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        # will use a minHeap at size k to dynamicly hold kth max value
        minHeap = []
        heapq.heapify(minHeap)

        # bfs to track level order transversal
        # Will hold sum of each level. root is level:0 {0:5, 1:17, 2: 13, ..}
        levelSum = defaultdict(int)
        st = deque([(root, 0)])

        # check and update heap, if reached a new level, delete level to save space
        def updateHeap(level: int):
            if levelSum[level] == 0 and level > 0: # level>0 is needed not to include levelSum[-1]
                heapq.heappush(minHeap, levelSum[level-1])
                while len(minHeap) > k:
                    heapq.heappop(minHeap)
                # del levelSum[level-1]


        lastLevelVisited = 0
        while st:
            node, level = st.popleft()
            lastLevelVisited = level
            # Lets check if we reached a new level, and if so push into heap the prev level
            updateHeap(level)
            levelSum[level] += node.val

            if node.left:
                st.append((node.left, level+1))
            if node.right:
                st.append((node.right, level+1))
        ## update heap 1 more time after bfs is done
        updateHeap(lastLevelVisited+1)

        return minHeap[0] if len(minHeap) == k else -1



        