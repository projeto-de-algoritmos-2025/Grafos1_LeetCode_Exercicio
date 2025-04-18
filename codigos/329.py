class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        memo = {}  # dicionario de memorização
        max_len = 0


        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]


            max_path = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc


                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    path_len = 1 + dfs(new_row, new_col)
                    max_path = max(max_path, path_len)


            memo[(row, col)] = max_path
            return max_path


        for i in range(rows):
            for j in range(cols):
                length = dfs(i, j)
                max_len = max(max_len, length)


        return max_len