l1=[]
l2=[]
l3=[]
n1=int(input("Enter the size of 1st list"))
n2=int(input("Enter the size of 2nd list"))
n3=int(input("Enter the size of 3rd list"))
def createlist(l,n):
  for i in range(n):
    temp=int(input("Enter the elements"))
    l.append(temp)
  return (l)



l1=createlist(l1,n1)
l2=createlist(l2,n2)
l3=createlist(l3,n3)

print("The elements in list 1 is",l1)
print("The elements in list 2 is",l2)
print("The elements in list 3 is",l3)
# es=0
def evensum(l):
    es = 0
    for i in range(0, len(l), 2):  # loop through even indices
        es += l[i]
    return es

evsum=evensum(l1)+evensum(l2)+evensum(l3)
print("the sum of even elements is",evsum)

def oddsum(l):
    os = 0
    for i in range(1, len(l), 2):
        os += l[i]
    return os

odsum=oddsum(l1)+oddsum(l2)+oddsum(l3)
print("The sum of odd elements is",odsum)

print("The product of even sum and odd sum is",evsum*odsum)