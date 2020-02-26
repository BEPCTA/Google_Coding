import sys

sys.stdin = open("args1.txt")
#sys.stdout = open('out.txt', 'w')

def solve_it():
    f, s = list(map(int, input().split()))
    t = set()
    for i in range(f):
        r, c = list(map(int, input().split()))
        t.add((r-1, c-1))
    print("set", t)
    res = 0
    for i in range(s):
        r = 0
        for j in range(s):
            if (i,j) in t or (j,i) in t:
                r += 1
        if res < r:
            res = r
    return res

def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
 #       print(test_case, file=sys.stderr, end=' ')
        res = solve_it()
        print('Case #' + str(test_case) + ':', res)

 #   print(file=sys.stderr)

if __name__ == '__main__':
    main()
