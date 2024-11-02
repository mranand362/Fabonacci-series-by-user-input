num = int(input("enter the number"))
a,b = 0,1
print(a,b , end=" ")
for x in range(2,num+1):
    c = a+b
    a=b
    b=c
    print(c , end=" ")