import sys, math
sys.stdin = open("args1.txt")

def multifactorial9000(num_exc):
  ans = math.log10(9000)
  curr = 9000
  curr -= num_exc
  while curr > 0:
    ans += math.log10(curr)
    curr -= num_exc
  return math.ceil(ans)

# from number of exclamation points to number of digits
digits = [-1]*9001
for num_exc in range(1, 9001):
  digits[num_exc] = multifactorial9000(num_exc)

def solve(d):  
  i = 1
  while i <= 9000 and d <= digits[i]:
    i += 1
  if i > 9000:
    return "..."
  return "IT'S OVER 9000" + "!"*i

def main():
    ncases = int(input())
    for i in range(ncases):  
        d = int(input())
        print("Case #{0}: {1}".format(i + 1, solve(d)))

if __name__ == "__main__":
    main()