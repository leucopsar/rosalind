def print_out(s):
    f = open("prob_res.txt", "w")
    f.write(s)
    f.close()

def get_fasta():
    d = {}
    entry = ""
    cur = ""
    lines = open("rosalind_grph.txt").readlines()
    for line in lines:
        if line[0] == ">":
            if cur != "":
                d[entry] = cur
            entry = line[1:].replace("\n", "")
            d[entry] = ""
            cur = ""
        else:
            cur += line.replace("\n", "")
    if cur != "":
        d[entry] = cur
    print(d)
    return d


def calc_overlap(d, k):
    edges = []
    for e1, v1 in d.items():
        #print("E1: " + e1)
        for e2, v2 in d.items():
            #print("E2: " + e2)
            if v1 == v2: continue
            #print(v1[len(v1)-k:],v2[:k])
            if v1[len(v1)-k:] == v2[:k]:
                edges.append((e1, e2))
    return edges


def is_overlap(left, right, k):
    return left[len(v1)-k:] == right[:k]




def mstr(edges):
    s = ""
    for e in edges:
        s += e[0] + " " + e[1] + "\n"
    return s


# after finding one with > half overlap: find longest possible? or candidate list
def combine(left, right): # in: two pres. overlapping strings
    j = 0
    left_size = len(left)
    right_size = len(right)
    # check for lengths of left/right 
    for k in range(0, left_size):
        if left[len(left)-k:] == right[:k]:
            j = k    
        if k == right_size-1: # case left > right, else go til left_size
            print("Out: " + str(k))
            break
    if j == 0:
        return "failed combination"
    print(j)
    return (j+1, left[0:] + right[j:])


le = "ABCDEF"
re = "DEFGHI"
print(combine(le, re))
print(combine("ABC", "FGHdfsjlk"))
#d = get_fasta()
#print_out(mstr(calc_overlap(d, 3)))
