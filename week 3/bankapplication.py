def bal(balance):
  print(balance)

def credit(balance,value):
  balance=balance+value
  return balance

def debit(balance,value):
  balance= balance-value
  return balance


















x=int(input("ENTER THE AMOUNT TO BE CREDITED"))
y=int(input("ENTER THE AMOUNT TO BE DEBITED"))
balance=0
print("Balance is ", end =" ")
balance=credit(balance,x)
balance=debit(balance,y)
bal(balance)