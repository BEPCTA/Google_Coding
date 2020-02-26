import sys
sys.stdin = open("args1.txt")


def answer():
    n = int(input())
    pp = list(map(int, input().split()))
    p2 = []
    ans =[]
    for p in pp:
        if (len(p2) == 0 or p2[0] != p):
            ans.append(p)
            p2.append( p*4/3)
        else:
            del p2[0]
    return " ".join( str(a) for a in sorted(ans))


def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}: {1}".format(i + 1, answer()))

if __name__ == "__main__":
    main()