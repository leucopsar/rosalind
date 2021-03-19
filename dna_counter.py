text = open("rosalind_dna(1).txt").readlines()[0]
#text = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
db = {'A':0, 'C': 0, 'G': 0, 'T': 0}
for i in text:
    if i in db:
        db[i] += 1
s = ""
for l in "ACGT":
    s += str(db[l]) + " "
print(s)
