f = open("rosalind_ini6(2).txt")
li = f.readlines()[0]
li = "We tried list and we tried dicts also we tried Zen"
#splits = li.split(" ")
#print(splits)
db = {}
for s in li.split(' '):
 #   print(s)
    if s in db:
        db[s] += 1
        continue
    db[s] = 1

#print(len(db))
for k, v in db.items():
    print(k + " " + str(v))
