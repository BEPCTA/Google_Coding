# -*- coding: utf-8 -*-

from sys import stdin
import heapq

# parts = [int(i) for i in stdin.readline().strip().split()]
# for i in range(f):
#     nums.append(tuple(int(i) for i in stdin.readline().strip().split()))

def get_answer():
    size = int(stdin.readline().strip())
    parts = [int(i) for i in stdin.readline().strip().split()]
    res = [0 for i in range(size)]
    hp = [-el for el in parts]
    heapq.heapify(hp)
    if size % 2 == 0:
        half = size // 2
        # res[half] = -heapq.heappop(hp)
        # res[half + 1] = -heapq.heappop(hp)
        o1 = [i for i in range((size - 1) // 2 + 1)]
        opt = o1 + o1[::-1]
        for i in range(half):
            res[half - i - 1] = -heapq.heappop(hp)
            res[half + i] = -heapq.heappop(hp)
    else:
        half = (size - 1) // 2
        res[half] =  -heapq.heappop(hp)
        o1 = o1 = [i for i in range(half)]
        opt = o1 + [(size - 1) // 2] + o1[::-1]
        for i in range(1, half + 1):
            res[half - i] = -heapq.heappop(hp)
            res[half + i] = -heapq.heappop(hp)
    ssq = 0
    for i in range(len(res)):
        ssq += (res[i] - opt[i]) ** 2
    return ssq

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print("Case #{0}: {1}".format(i + 1, get_answer()))

if __name__ == "__main__":
    main()
