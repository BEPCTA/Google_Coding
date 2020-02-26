# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 00:04:40 2020

@author: user
"""
def get_answer():
    k = int(input())
    ms = list(map(int, input().split()))
    # backwards
    curmax = ms[-1]
    curmin = ms[-1]
    cutoff = 0
    for i in range(k - 1, 0, -1):
        if ((ms[-1] - curmax) * (ms[i] - curmax) > 0) or ((ms[-1] - curmin) * (ms[i] - curmin) > 0):
            cutoff = i
            break
        if ms[i] > curmax:
            curmax = ms[i]
        if ms[i] < curmin:
            curmin = ms[i]
    if cutoff == 0:
        return 0
    # forward
    curmax = ms[0]
    curmin = ms[0]
    count = 0
    start = 0
    for i in range(1, cutoff + 1):
        if ((ms[start] - curmax) * (ms[i] - curmax) > 0) or ((ms[start] - curmin) * (ms[i] - curmin) > 0):
            count += 1
            curmax = ms[i]
            curmin = ms[i]
            start = i
        if ms[i] > curmax:
            curmax = ms[i]
        if ms[i] < curmin:
            curmin = ms[i]
    return count


def main():
    t = int(input())
    for i in range(t):
        print('Case #{0}: {1}'.format(i + 1, get_answer()))

if __name__ == '__main__':
    main()
