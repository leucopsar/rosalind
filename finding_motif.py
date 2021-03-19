import requests as req

def find_motif_in_data()
    r = req.get('https://www.uniprot.org/uniprot/B5ZC00.fasta')
    print(r.text)[0:300]




def find_motif_base()
    f = open("rosalind_subs.txt")
    s = f.readlines()

    base = s[0][:-1]
    ss = s[1][:-1]
    #print(base)
    print(ss)
    slen = len(ss)
    print(base, ss)
    i = 0
    res = ""
    while i <= len(base)-slen:
        cur = base[i:i+slen]
        if cur == ss:
            res += str(i+1) + " "
            #i+= slen
        i+=1
    print(res)



