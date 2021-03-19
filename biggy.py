s = 0
#for i in range(a, b+1):
#    if i%2!=0:
#        s+=i
a = 4944
b = 9366
i = a
if a%2==0:
    i = a + 1 
while i <= b:
    s += i
    i+=2
print(s)
