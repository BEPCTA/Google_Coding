
from math import floor
import sys
sys.stdin = open("args1.txt")

def year( A, B , a, b):
    pairs = min(A,B)
    babies = floor(pairs *0.02)
    dA = floor(babies * a/100.)
    dB = floor(babies * b/100.)
    dbab = babies - dA -dB
    dA  += dbab//2
    dB  += dbab - dbab//2
 #   print(dA, dB, floor(A/100.), floor(B/100.))
    return A + dA - floor(A/100.), B + dB - floor(B/100.)

def answer():
    A, B, a, b, Y = map(int, input().split())
    A0, B0 = A, B
    for y in range(Y):    
        A,B = year(A,B,a,b)
        if A==A0 and B ==B0:
            print("year =", y, A, B)
            break 
        
        else:
            A0, B0 = A, B
    
    return " ".join( str(a) for a in [A, B])

def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}: {1}".format(i + 1, answer()))

if __name__ == "__main__":
    main()