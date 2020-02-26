# -*- coding: utf-8 -*-
from sys import stdin

def answer():
    K = int(stdin.readline().strip())
    w = [int(i) for i in stdin.readline().strip().split()]
    w = sorted(w)
    #print(K, w)
    err = 0
    for i in range(K//2):
        #print(i)
        err += (w[2*i] - i)**2
        err += (w[2*i +1] - i)**2
    if K%2:
        err += (w[-1] - (K-1)/2) **2

    return int(err)
        
def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print("Case #{}: {}".format(i+1, answer()))

if __name__=='__main__':
    main()
    
    