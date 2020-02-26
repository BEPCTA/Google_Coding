import sys
sys.stdin = open("args1.txt")

def answer():
    f, s = list(map(int, input().split()))
    t = set()
    for i in range(f):
        r, c = list(map(int, input().split()))
        t.add((r-1,c-1))
    ans = 0
    for i in range(s):
        a = 0
        for j in range(s):
            if (i,j) in t or (j,i) in t:
                a +=1
        if ans < a: 
            ans = a
    return ans

def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}: {1}".format(i + 1, answer()))

if __name__ == "__main__":
    main()
