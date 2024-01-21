class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curC = image[sr][sc] # color to swap
        rows = len(image)
        cols = len(image[0])


        def dfs(r,c):
            image[r][c] = color

            for i,j in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
                if 0 <= i < rows and 0 <= j < cols and image[i][j] == curC and image[i][j] != color:
                    image[r][c] = color
                    dfs(i,j)

        

        dfs(sr,sc)

        return image
        