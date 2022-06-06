def maskCard(cardno):
    cardno=str(cardno)
    str1="*"*(len(cardno)-4)+cardno[-4:]
    return str1

cardno=int(input("enter the card number"))
print(maskCard(cardno))