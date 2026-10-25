class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Iterative to avoid recursion limit on 100x100 grids
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

        # Step 1: eliminate islands connected to the border
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and grid[r][c] == 0:
                    dfs(r, c)

        # Step 2: count remaining islands (all are closed)
        count = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    count += 1

        return count