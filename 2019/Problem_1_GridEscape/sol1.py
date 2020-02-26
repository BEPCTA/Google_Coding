# -*- coding: utf-8 -*-

def get_answer():
    r, c, k = map(int, input().split())
    if k == r * c - 1:
        return 'IMPOSSIBLE'
    if c == 1:
        res = []
        for i in range(k):
            res.append(['W'])
        if k < r:
            res.append(['S'])
            for i in range(r - k - 1):
                res.append(['N'])
    else:
        open_row = ['W' for i in range(c)]
        closed_row = ['E'] + ['W' for i in range(c - 1)]
        res = []
        rows_created = k // c
        for i in range(rows_created):
            res.append(open_row)
        left = k % c
        if left > 0:
            cur_row = open_row[:]
            if left == c - 1:
                cur_row[-1] = 'S'
            else:
                cur_row[left] = 'E'
            res.append(cur_row)
            rows_created += 1
        for i in range(r - rows_created):
            res.append(closed_row)
    res_lst = [''.join(row) for row in res]
    return 'POSSIBLE' + '\n' + '\n'.join(res_lst)


def main():
    t = int(input())
    for i in range(t):
        print('Case #{0}: {1}'.format(i + 1, get_answer()))

if __name__ == '__main__':
    main()
