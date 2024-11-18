class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        Rows, Cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands = 0


        def bfs(r, c):

            queue = deque()
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr+row, dc+col
                    if (newRow < 0 or newCol < 0 or 
                    newRow >= Rows or newCol >= Cols or
                    grid[newRow][newCol] == "0"):
                        continue
                    queue.append((newRow,newCol))
                    grid[newRow][newCol] = "0"


        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands


