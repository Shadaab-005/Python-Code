
array=[]
for i in range(0,100):
    x=int(input())
    array.append(x)
found=0
for i in range(100):
   for j in range(i+1,100):
       if (array[i]==array[j]):
           print(array[i])
           found+=1
           break
   if found==1:
        break

