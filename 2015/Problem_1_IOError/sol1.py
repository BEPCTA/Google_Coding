import sys
sys.stdin = open("args1.txt")

def chrfromio(b):
  s = [(1 if c == 'I' else 0) for c in b]
  v = 0
  exp = 0
  for i in range(len(s)-1, -1, -1):
    v += (2**exp) * s[i]
    exp += 1
  return chr(v)

def fromio(inp):
  ans = ''
  for i in range(int(len(inp)/8)):
    b = inp[8*i:8*(i+1)]
    ans += chrfromio(b)
  return ans

def answer():
    nbytes = int(input())
    s = input() 
    return fromio(s)

def main():
    ncases = int(input())
    for i in range(ncases):        
        print("Case #{0}: {1}".format(i + 1, answer()))

if __name__ == "__main__":
    main()