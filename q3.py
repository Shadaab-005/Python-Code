def calculate(x,opr,y):
    if (opr=='+'):
        print(x+y)
    elif (opr=='-'):
        print(x-y)
    elif (opr== '*'):
        print(x*y)
    elif (opr== '/'):
        print(x/y)
    elif (opr=='and'):
        print(x and y)
    elif (opr=='or'):
        print(x or y)
   

x=int(input())
opt=input()
y=int(input())
calculate(x,opt,y)