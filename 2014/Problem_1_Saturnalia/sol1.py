import sys
sys.stdin = open("args1.txt")


def answer():
    s = input()
    t = "+-" + "-" * len(s) + "-+"
    print(t)
    print("| " + s + " |" )
    print(t)    
    
    
def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}:".format(i + 1))
        answer()

if __name__ == "__main__":
    main()