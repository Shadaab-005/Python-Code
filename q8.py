word=input("enter the word comtaining numbers with alphbet")
sum=0
for i in range(len(word)):
     if word[i].isdigit():
         x=int(word[i])
         sum=sum+x
print(sum)
