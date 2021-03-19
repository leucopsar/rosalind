f = open("rosalind_hamm.txt")
d = {}
i =0
for line in f.readlines():
    d[i] = line
    i += 1
    
print(len(d[0]))
print(len(d[1]))
r = 0
for i in range(0, len(d[0])):
    print(d[0][i], d[1][i])
    if d[0][i] != d[1][i]:
        r+=1
print(r)
