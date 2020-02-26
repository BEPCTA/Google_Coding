import sys
sys.stdin = open("args1.txt")


def answer():
    f, s = list(map(int, input().split()))
    ans = 0 
    
    return " ".join( str(a) for a in sorted(ans))

def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}: {1}".format(i + 1, answer()))

if __name__ == "__main__":
    main()