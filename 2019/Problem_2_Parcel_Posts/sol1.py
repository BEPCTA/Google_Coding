# -*- coding: utf-8 -*-

def solve():
    k = int(input())
    heights = [int(x) for x in input().split()]
    diffs = [heights[i + 1] - heights[i] for i in range(k)]
    s = []
    for x in diffs:
        if x > 0:
            s.append('+')
        elif x < 0:
            s.append('-')
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i] != s[i + 1]:
            count += 1
            i += 1
        i += 1
    return count - 1

if __name__ == "__main__":
    cases_nr = int(input())
    for i in range(cases_nr):
        ans = solve()
        print('Case #{}: {}'.format(i + 1, ans))

