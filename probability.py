# statistics
from math import log10

def get_prop():
    (k, m, n) = (17, 26, 24)
    d = []
    s = float(k + m + n)
    # chance of dominant aleele in offspring 1-No
    r = 0
    print(((n-1)/(s-1)))
    d.append((n/s)*((n-1)/(s-1)))
    d.append((n/s)*(m/(s-1))*0.5)
    d.append((m/s)*(n/(s-1))*0.5)
    d.append((m/s)*((m-1)/(s-1))*0.25)
    print(d)
    for i in range(0, 4):
        r+= d[i]
    r = 1-r
    return r


def get_random_probs():
    res = ""
    b = []
    (s, a) = get_file()
    for i in range(0, len(a)):
        res += str(result_prob(s, a[i])) + " "
    return res[:-1]


def result_prob(s, cg_p):
    r = 1
    d = {"C": float(cg_p/2), "G": float(cg_p/2),
         "A": float((1-cg_p)/2), "T": float((1-cg_p)/2)}
    for i in range(0, len(s)):
        r *= d[s[i]]
    #print(log10(r))
    return round(log10(r), 3)


def get_file():
    lines = open("rosalind_prob.txt").readlines()
    s = lines[0].replace("\n", "")
    d = []
    for i in range(1, len(lines)):
        splits = lines[i].replace("\n", "").split(" ")
        out = list(map(float, splits))
        d += out
    print(d)
    print(s)
    return (s, d)
    

s = get_random_probs()
print(s)
