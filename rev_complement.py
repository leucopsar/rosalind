def rev_comp(s):
    d = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    res = ""
    end = len(s)
    for i in range(0, end):
        c = s[end-1-i]
        if c in d:
            res+=d[c]
    return res


def rev_palindrome(s):
    if len(s) < 4: return
    _min = 4
    _max = 12
    res = []
    for i in range(0, len(s)-_min+1):
        for j in range(i+_min, len(s)+1): # i+4 with exclusivness
            
            sub_size = j - i
            if sub_size > _max:
                break # next leftIndex
            # constrained length ensured
            can = s[i:j]
            #print(i+1, j+1, can == rev_comp(can))
            #print(i+1, j+1, can, rev_comp(can), can == rev_comp(can))
            if can == rev_comp(can):
                res.append([i+1, sub_size])
    s = ""
    for e in res:
        s += str(e[0]) + " " + str(e[1]) + "\n"
    s = s[:-1]
    return s  



s = ""
sl = open("rosalind_revp.txt").readlines()
for i in range(1, len(sl)):
    #print(sl[i])
    t = sl[i].replace("\n", "")
    t = t.replace("\r","")
    s+=t
#s = "TCAATGCATGCGGGTCTATATGCAT"
print(len(s))
f = open("revp_sol.txt", "w")
f.write(rev_palindrome(s))
f.close()

