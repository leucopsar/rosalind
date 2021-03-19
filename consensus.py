f = open("rosalind_lcsm.txt")
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
r=sl[0]
m_str = ""
for i in range(0, len(r)):
    for j in range(i, len(r)):
        sub = r[i:j+1]
        if len(sub) <= len(m_str): # candidate must be > max
            continue
        missing = False
        for k in range(1, len(sl)): # find in remaining dnas
            if sub not in sl[k]:
                missing = True
                break
        if not missing:
            #print(sub)
            m_str = sub
print(m_str)

