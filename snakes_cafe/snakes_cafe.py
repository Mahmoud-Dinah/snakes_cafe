print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
""")
menu = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado",
        "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
i =+ 1
order = ''
order = input(">")
while order != '':
 print(f"{i} order of {order} have been added to your meal ")
 break

print("would you like to order any things else")
order = input(">")
while order.lower() != "n":
  i = i+1
  order = input(">")
  print(f"{i} order of {order}  have been added to your meal")
  print("would you like to order any things else? if no please press n to exit")
else:
  print("thank you!")