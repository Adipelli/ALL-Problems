print("_"*40)
d1={'apple':500,'banana':200,'pineapple':100,'grapes':100,'orange':70}
temp=[]
res=dict()
for key,value in d1.items():
    if value not in temp:
        temp.append(value)
        res[key]=value
print(res)

print("occurance".center(40,"-"))
l1=[10,20,30,10,40,10]
def remove_value(sample_list,val):
    return[i for i in sample_list if i != val]
res=remove_value(l1,10)
print(f"res:{res}")

print("sum of all items".center(40,"_"))
l=[10,20,30,40]
sum=sum(l)
print(f"sum:{sum}")

