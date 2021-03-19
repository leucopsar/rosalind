def listing(li):
    s = ""
    for i in li:
        s += i + "\n"
    return s[:-1]


def get_kmers(alph, k):
    res = []
    alph = alph.split(" ")
    m = len(alph)
    lists = []
    d = {}
    # construct lookup tables
    for i in range(0, k):
        d[i] = 0
        t = []
        for j in range(0, m):
            t.append(j)
        lists.append(t)
    # iterate
    # while(true?)
    print(lists)
    for i in range(0, pow(m, k)):
        mer = ""
        for j in range(0, k):
            #print(d[j])
            #print(lists[j][d[j]])
            mer+=alph[lists[j][d[j]]]
        res.append(mer)
        finished, d = get_update(d, m, k)
        if finished:
            break
    #print(listing(res))
    #print(len(res))
    return res

# alph list a la "A, BCDE.."
# x, y strings, a shorter
# returns -1 if x <lex y
# ret 1 if x >lex y etc.
def lex_than(x, y):
    alph = "D N A"
    (a, b) = (x, y)
    if(x == y): return 0 # else one is longer -> well-defined solution
    if len(x) > len(y):
        (a, b) = (y, x)
    matched=False
    m = 0
    for i in range(0, len(a)):
        if alph.index(a[i]) > alph.index(b[i]):
            m = 1
            break
        elif alph.index(a[i]) < alph.index(b[i]):
            m = -1
            break
    if m == 0: m = -1
    if a == x:
        return m
    else:
        return -1 if m == 1 else 1


def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare


def get_mers_until(alph, n): # lexicographically ordered
    res = []
    for i in range(1, n+1):
        for j in get_kmers(alph, i):
            res.append(j)
    print(listing(res))
    so = sorted(res, cmp=make_comparator(lex_than))
    
    #sorted(res, key=lambda x: len(x))
    print(listing(so))
    return so


def get_update(lookup, m, k):
    colFull = False
    res = lookup
    for j in range(0, k):
        index = (k-1)-j
        # if all silos at max: finished
        if lookup[index] == m-1:
            colFull = True
        else: # update dict
            colFull = False
            res[index] += 1
            #print("Incr: " + str(index) + " to " + str(res[index]))
            for i in range(index+1, k):
                res[i] = 0
            break
    return (colFull, res)


get_mers_until("D N A", 3)
#print(compare("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "APPLE", "APPLET"))
#print(compare("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "APPLET", "ARTS"))
