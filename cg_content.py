def analyse(line):
    l = 0
    ref = ["C", "G"]
    all = ["A", "T"]
    cgs = 0
    for i in range(0, len(line)):
        if line[i] in ref:
            cgs+=1
        elif line[i] not in all:
            continue
        l += 1
    return (cgs, l)



f = open("rosalind_gc.txt")
cur = ""
d = {}
for line in f.readlines():
    if line[0] == ">":
        cur = line[1:-1]
        #print(cur)
        d[cur] = [0, 0]
    else:
        d[cur][0] += analyse(line)[0]
        d[cur][1] += analyse(line)[1]

r = {}
for k, v in d.items():
    #print(d[k])
    d[k] = v[0]/float(v[1])
    print(k + ": " + str(d[k]))







