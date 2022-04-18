d4=dict(name='rahul',runs=35,oopn="NZL",venue='auckland',year=2003)
print(f"d4:{d4}")
print(type(d4))


dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={**dic1,**dic2,**dic3}
print(dic4)


print("key is exists".center(40,"_"))
print(d4)
def is_present(x):
    if x in d4:
        print("key present")
    else:
        print("not present")
is_present('name')
is_present(1)

print("iterate".center(40,"_"))
print(d4)
for k,v in d4.items():
    print(k,v)

print("_"*40)
n=6
dict=dict()
for i in range(1,n+1):
    dict[i]=i*i
print(dict)


print("_"*40)
l1=[1,2,3,12,10,20,30,40,50]
print(f"l1:{l1}")
l1.sort()
print(l1[-2])

print("_"*40)
l1=[1,2,3,12,10,20,30,40,50]
print(f"l1:{l1}")
l1.sort()
print(l1[1])



print("minimum and maximum".center(40,"_"))
t_dict = {'apple': 500, 'banana': 200, 'pineapple': 100, 'grapes': 100, 'orange': 70}
print(min(t_dict,key=t_dict.get))
print(max(t_dict,key=t_dict.get))

print("reverse".center(40,"_"))
l=['apple','banana','ten','grapes','orange']
print(f"l:{l}")
res=sorted(l)
print(f"res:{res}")
res1=sorted(l,reverse=True)
print(f"res1:{res1}")


print("unique".center(40,"_"))
l1=[1,2,4,5,6,1,2,1]
print(f"l1:{l1}")
my_set=set(l1)
converted_list=list(my_set)
print(converted_list)

print("count of repetition".center(40,"_"))
l1=[1,2,4,5,6,1,2,1]
print(f"l1:{l1}")
count=l1.count(l1)
print(count)

print("common items".center(40,"_"))
l2=[10,20,30,40,50]
l3=[50,60,70,80]
res=set(l2).intersection(set(l3))
print(f"res:{res}")

print("no.of lists in a list".center(40,"_"))
def list_count(l4):
    return len(l4)
    l4=[1,[2,3,4],[2,4,5],[6,7],[8,9,10]]
    print(list_count(l4))