f = open("rosalind_ini5.txt", "r")
my_list = f.readlines()
#for l in my_list:
 #   print(l)
n = len(my_list)

#print(my_list[3])
#print(n)
end = n
if n%2!=0:
    end = n-1
i = 1
while i < end:
    print(my_list[i])
    i += 2
