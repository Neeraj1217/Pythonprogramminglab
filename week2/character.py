string=input("Enter the string")[0]
if string.isupper():
  print(string,"Is Upper")
elif string.islower():
  print(string,"Is Lower")
elif string.isdigit():
  print(string,"Is Digit")
else:
  print(string,"Is a Special Character")