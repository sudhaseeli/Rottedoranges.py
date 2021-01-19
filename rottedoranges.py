class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotton = set()
        s = len(grid)
        p = len(grid[0])
        for k in range(s):
            for l in range(p):
                if grid[k][l] == 2:
                    rotton.add((k,l))
                elif grid[k][l] == 1:
                    fresh.add((k, l)) 
        mins = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while len(fresh) > 0:
            infected = set()
            for r in rotton:
                row = r[0]
                col = r[1]
                for dir in dirs:
                    new_row = dir[0] + row
                    new_col = dir[1] + col
                    if (new_row, new_col) in fresh:
                        fresh.remove((new_row, new_col))
                        infected.add((new_row, new_col))   
            if len(infected) == 0:
                return -1
            rotton = infected
            mins += 1
        return mins
