a=50000
count = 0
pin = 1350
for count in range (2):
  givepin = int(input("enter the pin"))

  if givepin == pin: 
     amount=int(input("enter the amount you want"))
     if amount>a:
       print("invalid amount")
     else:
       balanceamount= a-amount
       print('Balance amount is: ',balanceamount)
       break