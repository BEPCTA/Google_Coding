# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:18:08 2020

@author: user
"""

def solve_a():
    r, c, k = (int(x) for x in input().split())
    if k == r * c - 1:
        return 'IMPOSSIBLE', []
    grid = [['X'] * c for _ in range(r)]
    for i in range(r * c):
        if i < k:
            grid[i // c][i % c] = 'N'
        elif i == c * r - 1 and c == 1:
            grid[i // c][i % c] = 'N'
        elif i == c * r - 1:
            grid[i // c][i % c] = 'W'
        elif i // c == r - 1:
            grid[i // c][i % c] = 'E'
        else:
            grid[i // c][i % c] = 'S'
    return 'POSSIBLE', grid


if __name__ == "__main__":
    cases_nr = int(input())
    for i in range(cases_nr):
        ans = solve_a()
        print('Case #{}: {}'.format(i + 1, ans[0]))
        for x in ans[1]:
            print(''.join(x))
