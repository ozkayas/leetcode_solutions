class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # find indexes for smaller values at left and at right
        def smallerOnLeft():
            # (index, value). start with -1, -1/ for some problems used -inf, -1/ sum of min of subarrays ie.
            st = [(-1, -1)]
            smallers = [-1 for i in range(len(heights))]

            for i in range(len(heights)):
                # pop biggers
                while st[-1][1] >= heights[i]:
                    st.pop()
                # save index at top for 
                smallers[i] = st[-1][0]
                st.append((i, heights[i]))

            return smallers

        # find indexes for smaller values at left and at right
        def smallerOnRight():
            # (index, value). start with -1, -1/ for some problems used -inf, -1/ sum of min of subarrays ie.
            st = [(len(heights), -1)]
            smallers = [len(heights) for i in range(len(heights))]

            for i in range(len(heights)-1, -1, -1):
                # pop biggers
                while st[-1][1] >= heights[i]:
                    st.pop()
                # save index at top for 
                smallers[i] = st[-1][0]
                st.append((i, heights[i]))

            return smallers
        
        # print(smallerOnLeft())
        # print(smallerOnRight())

        left = smallerOnLeft()
        right = smallerOnRight()
        
        maxSoFar = 0
        for i in range(len(heights)):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            maxSoFar = max(maxSoFar, area)

        return maxSoFar



        return 0



        