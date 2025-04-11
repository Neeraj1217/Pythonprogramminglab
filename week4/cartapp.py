itemlist=[]
pricelist=[]
def additem(item,price):
  pricelist.append(price)
  itemlist.append(item)
  print(item,"has been successfully added to your cart.")

def removeitem(itemr):
  if itemr in itemlist:
    index=itemlist.index(itemr)
    itemlist.pop(index)
    pricelist.pop(index)
    print(itemr,"has been successfully removed from your cart.")
  else:
    print("The item you are trying to remove was not found in your cart.")

def viewcart():
  print("Items in your cart:")
  for i in itemlist:
    print(i, end =" ")
  print()
  print("Prices of the items:")
  for j in pricelist:
    print(j, end = " ")
  print()

while True:
  print("Please choose an option:")
  print("1 - Add an item to your cart")
  print("2 - Remove an item from your cart")
  print("3 - View items in your cart")
  print("4 - Checkout and exit")
  a=int(input("Enter your choice: "))
  if(a==1):
    item=input("Enter the name of the item you wish to add: ")
    price=int(input("Enter the price of the item: "))
    additem(item,price)
  elif(a==2):
    itemr=input("Enter the name of the item you wish to remove: ")
    removeitem(itemr)
  elif(a==3):
    viewcart()
  elif(a==4):
    print("Thank you for shopping with us. Exiting the program...")
    break
