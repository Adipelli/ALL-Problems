for i in range(1,5):
    for j in range(1,5):
        if(i==j):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()


print("armstrong".center(40,"_"))
for i in range(500):
    sum=0
    num=i
    r=len(str(i))
    while(i!=0):

        res=i%10
        sum=sum + res**r
        i= i//10
    if num==sum:

       print(num)



