import sys
sys.stdin = open("args1.txt")


def answer():
    ss = input()
    ans = 0
    Iz = 0
    iz = 0
    for s in ss:
        if s == "I":
            Iz += 1
            continue
        elif s == "i":
            iz +=1
            continue
        
        if s == "O" and Iz:
            ans +=1            
            Iz -=1
        else:
            if iz: 
                iz -=1
            else:
                Iz -=1
    return ans

def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}: {1}".format(i + 1, answer()))

if __name__ == "__main__":
    main()