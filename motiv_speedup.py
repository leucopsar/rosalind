def max_len(s, k): # is s[2:2] one letter?
    for j in range(1, len(s)):
        if s[j:k] == s[:k-j]: # if match return, any other will be shorter
            return k-j
    return 0


f = open("rosalind_kmp.txt")
s = ""
for line in f.readlines():
    if line[0] == ">":
        continue
    else:
        s += line.replace("\n", "")
#print(s)
res = ""#[]
n = len(s)
res += "0 "
#res.append(0)
for k in range(1, n):
    res += str(max_len(s, k+1)) + " "
    #res.append(max_len(s, k+1)) # k+1?
res = res[:-1]
#print(res)
fi = open("sol.txt", "w")
fi.write(res)
fi.close()
