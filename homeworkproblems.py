
for i in range(5):
    for j in range(i,-1,-1):
        print(i+1,end="")
    print()


print("_"*40)
for i in range(5):
    for k in range(6-i):
        print("",end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range(4,0,-1):
    for k in range(7,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("_"*40)
num=1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1

    print()

print("_"*40)
n1=0
n2=1
for i in range(10):

    print(n1)

    n3=n1+n2
    n1=n2
    n2=n3
print(n3)


print("_"*40)
n=int(input("enter the number"))
strong=n
sum=0
while(n>0):
    r=n%10
    fact=1
    for i in range (1,r+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(strong==sum):
    print("strong number")
else:
     print("not strong number")


print("pasacal triangle".center(40,"_"))
list1=[]
for i in range(4):
    temp_list=[]
    for j in range(i+1):
        if j==0 or j==1:
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1]+list1[i-1][j])
    list1.append(temp_list)
    for i in range(4):
        for j in range(4-i-1):
            print(" ",end=" ")
        for j in range(i + 1):
            print(list1[i][j], end=" ")
        print()






