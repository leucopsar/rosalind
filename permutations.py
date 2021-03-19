from itertools import permutations
from math import factorial

def enumerating():
    # Enumerating
    n = 5
    n_list=[]
    for i in range(1, n + 1):
        n_list.append(str(i))
    all = get_list(n_list)
    print(len(all))
    #print(get_list(n_list))
    for i in all:
        print(listing(i))
    

def get_list(li):
    res = []
    if len(li) == 1:
        res.append(li)
    else:
        for c in li:
            cur = []
            for i in li: cur.append(i)
            cur.remove(c)
            for my_list in get_list(cur):
                t = []
                for i in my_list: t.append(i)
                t.insert(0, c)
                res.append(t)
    return res


def oriented(n):
    res = []
    number_of_permutations = factorial(n)
    p_n = pow(2, n)
    r = p_n*number_of_permutations
    li=list(permutations(range(1,n+1)))
    base = []
    for el in li: # el has n elements
        for i in range(0, p_n):
            t = []
            for j in range(0, n):
                b = -1 if ((i >> j) & 1) else 1
                t.append(b*el[j])
            base.append(t)
    #print(base)
    s = str(r)
    for e in base:
        s += "\n"
        for el in e:
            s+= str(el) + " "
        s = s[:-1]
    fi = open("sign_res.txt", "w")
    fi.write(s)
    fi.close()
    #print(s)


def listing(li):
    s = ""
    for i in li:
        s += i + " "
    return s[:-1]



oriented(4)



