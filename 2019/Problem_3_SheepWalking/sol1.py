def solve(grid):
    x, y = (int(x) for x in input().split())
    if x < 0:
        x = -x
    if y < 0:
        y = -y

    return grid[x][y]


if __name__ == "__main__":
    grid = [[0, 3], [3, 4]]
    i = 2
    while i < 501:
        a = grid[0][i - 1]
        b = grid[1][i - 1]
        xx = (1.5 + a / 2 + b/4) / 0.75
        grid[0].append(xx)
        grid[1].append(xx / 2 + b / 2 + 1)
        grid.append([xx, xx / 2 + b / 2 + 1])
        i += 1

    for i in range(2, 501):
        for j in range(2, 501):
            grid[i].append(0.5 * grid[i][j - 1] + 0.5 * grid[i - 1][j] + 1)
    cases_nr = int(input())
    for i in range(cases_nr):
        ans = solve(grid)
        print('Case #{}: {}'.format(i + 1, ans))

