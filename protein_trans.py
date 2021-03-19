def get_table():
    f = open("codons.txt")
    lines = f.readlines()
    lu = {}
    for line in lines:
        cur = ""
        key = ""
        for i in range(0, len(line)):
            if line[i] == "\n":
                if cur != "" and key != "":
                    lu[key] = cur
                (cur, key) = ("", "")
                break
            if line[i] != " ":
                print(line[i])
                cur += line[i]
            else: # space
                if len(cur) == 3: # add key
                    lu[cur] = ""
                    key = cur
                    cur = ""
                else: # check if val or empty
                    if len(cur) == 1 or len(cur) == 4:
                        print(key, cur)
                        lu[key] = cur
                        (cur, key) = ("", "")
        if key != "":
            lu[key] = cur
    print(lu)
    print("Dicsize: " + str(len(lu)))
    return lu


def translate():
    f = open("rosalind_prot.txt").readlines()
    s = ""
    for line in f:
        s += line.replace("\n", "")
    #s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    print(len(s)%3 == 0)
    #print(len(s))
    sol = ""
    d = get_table()
    #print(d)
    i = 0
    while i < len(s)-2:
        #print(i)
        cur = s[i:i+3]
        #print(cur)
        i += 3
        if cur not in d:
         #   print("Not: " + str(i-1))
            continue
        r = d[cur]
        #i += 2
        if r == "Stop":
            break
        #print("Match: " + r)
        sol += r
    nf = open("sol_trans.txt", "w")
    nf.write(sol)
    nf.close()
    print(sol)



translate()
        
