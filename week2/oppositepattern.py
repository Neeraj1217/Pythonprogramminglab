n=int(input("Enter the number of rows"))
for i in range(n,0,-1):
  print()
  for j in range((n+1)-i,0,-1):
    print(i, end= " ")
