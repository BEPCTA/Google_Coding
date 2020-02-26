fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline())

for q in range(0, n):
    fout.write('Case #' + str(q + 1) + ': ')
    a = int(fin.readline())
    s = list(map(int, fin.readline().split()))
    
    prev = []
    
    for x in s:
        if (len(prev) == 0 or prev[0] != x):
            fout.write(str(x) + " ")
            prev.append(x / 3 * 4)
        else:
            prev = prev[1:]
    
    fout.write("\n")
    
fin.close()
fout.close()