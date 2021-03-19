def get_max(lol):
    res = []
    w = len(lol[0])
    h = len(lol)
    for i in range(0, w):
        m = -1
        ind = -1
        for j in range(0, h):
            if m < lol[j][i]:
                ind = j
                m = lol[j][i]
        res.append(ind)
    return res

f = open("rosalind_cons(1).txt")
cur = ""
dna = "ACGT"
sl = []
ind = {"A": 0, "C":1, "G":2, "T":3}
d = [0, 0, 0, 0]
lol = [[],[], [], []]
#print(g)
for line in f.readlines():
    if line[0] == ">":
        if cur != "":
            #print(cur)
            sl.append(cur)
        cur = ""
        continue
        #print(cur)
        #d[cur] = [0, 0]
    else:
        cur += line.replace("\n", "")

if cur != "":
    sl.append(cur)

for i in range(0, len(sl[0])):
    for read in sl:
        d[ind[read[i]]] += 1
    for j in range(0, 4):
        lol[j].append(d[j])
    d = [0, 0, 0, 0]
                  
#print(lol)
s = ""
res = get_max(lol)
for i in range(0, len(lol[0])):
    s += dna[res[i]]
s += "\n"

    
for let in "ACGT":
    #print(d[k])
    s += let + ":"
    for i in range(0, len(sl[0])):
        s+= " " + str(lol[ind[let]][i])
    s += "\n"
s = s[:-1]
rfile = open("cons_res.txt", "w")
rfile.write(s)
rfile.close()
print(s)

