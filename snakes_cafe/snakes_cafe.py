from sys import exit
from food import food


print ("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
# Menu Sections 
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

food_record = []


# set up an order input
def restaurant_order():
  order_list = []

  order = input("> ")


  # set a conditional if order is true to print an acknowledgement of the order
  # Check if it is a part of the food module

  if order == True:
    food_record.append(order)
    print(food_record)
    food_counter = food_record.count(order)
    for item in food_record:
      if food_counter > 1:
        print(f'** {food_counter} orders of {item} have been added to your meal **')
      else:
        print(f'** {food_counter} order of {item} have been added to your meal **')
        restaurant_order
  elif order == "end":
    exit()
  else:
    print('***Please make a different menu selection***')



restaurant_order()