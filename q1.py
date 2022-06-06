def myfxn(list,cond):
    if (cond=="asc"):
        list.sort()
        print(list)
        
    elif(cond=="desc"):
        list.sort(reverse=True)
        print(list)
    elif(cond=="none"):
        list=list
        print(list)
    else:
        print("\nchoose order as 'asc';'desc';'none' only")


n=int(input("enter no. of elements in list"))
list1=[]
for i in range(n):
    
    x=float(input())
    list1.append(x)
cond=input("enetr the order ")
myfxn(list1,cond)
