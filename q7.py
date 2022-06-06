import  numpy as np



arr=np.array([21,23,45,67,87,90,33,21,33,23,33,21,90,21,67,21])
arr.sort()
n=arr.size
i=0
max=0
while (i<n):
    x=np.where(arr==arr[i])
    n1=len(x[0])
    
    if max<n1:
        max=n1
        max_element=i
    i=i+n1

print("the number having maximum frequency :", arr[max_element])
