# 0 1 1 2 3 5.......
""" a b c d e
c=a+b 1
d=b+c 2
e=c+d 3 """

x=int(input("enter the number: "))
k = 1
j = 1
i = 0
print(k)
print(j)
while j < x :
    i = k+j
    k = j
    j = i
    print(i)
    
    









