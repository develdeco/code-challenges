def solution(grid):
    for i in range(9):
        row = [0]*10
        for ri in range(9):
            if grid[i][ri] != '.':
                row[int(grid[i][ri])] += 1
                if row[int(grid[i][ri])] == 2:
                    return False
        col = [0]*10
        for ci in range(9):
            if grid[ci][i] != '.':
                col[int(grid[ci][i])] += 1
                if col[int(grid[ci][i])] == 2:
                    return False
        rix = (i//3)*3
        cix = (i%3)*3
        square = [0]*10
        for x in range(rix,rix+3):
            for y in range(cix,cix+3):
                if grid[x][y] != '.':
                    square[int(grid[x][y])] += 1
                    if square[int(grid[x][y])] == 2:
                        return False
    return True