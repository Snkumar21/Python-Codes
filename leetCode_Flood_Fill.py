class Solution(object):
    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        # If the pixel is already the target color, just return
        if original_color == color:
            return image

        def dfs(r, c):
            # stop if out of bounds or not the original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            # fill the pixel
            image[r][c] = color
            # explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image