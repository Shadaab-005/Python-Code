def stringManipulation(str):
    Str=""
    for i in range(len(str)):
        Str+=str[i]+str[i]

    print(Str)
s=input("enter the string:  ")
stringManipulation(s)
