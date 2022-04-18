
cntr=0
j=1
while cntr<6:
    num=j
    flag=False
    lst=[]
    for i in range(3):
        if (num-1)%3==0:
            res=(num-1)//3+1
            lst.append(res)
            if i==2:
                flag=True
        else:
            break
    if flag and num and num%3==0:
        print("Total {} remaining {} fathar distributes {} to each other".format)
