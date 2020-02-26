# -*- coding: utf-8 -*-
N = 505
grid = [[-1] * N for _ in range(N)]
grid[0][0] = 0
grid[0][1] = grid[1][0] = 3
grid[1][1] = 4
for i in range(2, N):
    x, y = grid[0][i-1], grid[1][i-1]
    b = (2/3) * y + (1/3) * x + 2
    a = (1/2) * x + (1/2) * b + 1
    grid[0][i] = grid[i][0] = a
    grid[1][i] = grid[i][1] = b

def dp(x, y):
    x, y = abs(x), abs(y)
    if grid[x][y] == -1:
        grid[x][y] = 0.5*dp(x-1,y) + 0.5*dp(x,y-1) + 1
    return grid[x][y]

for case in range(1, int(input())+1):
    x, y = map(int, input().split())
    print("Case #{}:".format(case), dp(x, y))
