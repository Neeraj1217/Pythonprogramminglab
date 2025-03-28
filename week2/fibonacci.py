#printfiobonacciseries
n=int(input("Enter the term till which u want to print"))
a=0
b=1
print(a, end=" ")
print(b, end=" ")
while(n>0):
  c=a+b
  print(c, end=" ")
  a=b
  b=c
  n=n-1