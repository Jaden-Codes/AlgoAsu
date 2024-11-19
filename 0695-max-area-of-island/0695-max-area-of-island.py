class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        maxIslandarea = 0

        def bfs(r, c):
            queue = deque([])
            current = 1
            queue.append((r, c))
            grid[r][c] = 0

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr + row, dc + col

                    if (newRow < 0 or newCol < 0 or 
                    newRow >= Rows or newCol >= Cols or
                    grid[newRow][newCol] != 1):
                        continue

                    grid[newRow][newCol] = 0
                    queue.append((newRow, newCol))
                    current += 1
            return current


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    current = bfs(r, c)
                    maxIslandarea = max(current, maxIslandarea)
        return maxIslandarea

