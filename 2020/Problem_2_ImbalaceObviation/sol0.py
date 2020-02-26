import sys
sys.stdin = open("args1.txt")


def answer():
    n = int(input())
    bb = list(map(int, input().split()))
    print(n, bb)
    if n== 1:
        return "R"
    if n == 2:
        return "RL"
    
    b1 =[]
    b2 =[]
    ans =""
    for i in range(len(bb)):
        if i%2:
            b2.append(bb[i])
        else:
            b1.append(bb[i])
    b1 = sorted(b1)
    b2 = sorted(b2)
    print (b1, b2)    
    for i in range(len(b2)):
        r, l = b1[i], b2[i]
        print(r,l)
        if r < l:
            ans +="R"
            ans +="L"
        else:
            ans +="L"
            ans +="R"
    if len(b1) > len(b2):
        if ans[-1] == "R" :
            ans +="L"
        else:
            ans +="R"
    
    return ans[:n]

def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}: {1}".format(i + 1, answer()))

if __name__ == "__main__":
    main()