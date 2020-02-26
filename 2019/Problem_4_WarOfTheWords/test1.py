from random import choice
import sys
a = 'ABCDEFGHIJ'
def garbage():
    return ''.join(choice(a) for _ in range(5))

tests, n = map(int, input().split())
for case in range(1, tests+1):
    print(garbage()) # start word
    for _ in range(50): # remaining 100 points
        best_word = input()
        if best_word == '-1': 
            sys.exit()
        print(garbage())
        trash_word = input()
        if trash_word == '-1': sys.exit()
        print(best_word)
sys.exit()
