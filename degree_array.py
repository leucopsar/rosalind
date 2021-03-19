f = open("rosalind_ddeg.txt")
lines = f.readlines()
start = lines[0]
start = start[:-1]
nodes = start.split(" ")[0]
edges = start.split(" ")[1]
tar = {} # adjacency dict
d = {} 
for i in range(1, int(nodes)+1):
    tar[i] = []
del lines[0]
#print(tar)
#print(len(lines))
for line in lines:
    li = line.replace("\n", "")
    li = li.split(" ")
    #print(li)
    n1 = int(li[0])
    n2 = int(li[1])
    tar[n1].append(n2)
    tar[n2].append(n1)

# double degree:
s = ""
#print(d)
for k in range(1, int(nodes)+1):
    count = 0
    for l in tar[k]:
        count += len(tar[l])
    d[k] = count
for i in range(1, int(nodes)+1):
    s += str(d[i]) + " "

print(s[:-1])


