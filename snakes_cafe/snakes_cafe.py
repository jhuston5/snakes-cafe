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

# Thanks to Bionca for helping me here - utilize an empty list to store food values
real_food = []
for i in food.values():
  
  real_food +=i


# set up an order input
def restaurant_order():

  order = input("> ")


  # set a conditional if order is true to print an acknowledgement of the order
  # Check if it is a part of the food module

  if order in real_food:
    food_record.append(order)
    
    food_counter = food_record.count(order)
    for item in food_record:
      if food_counter > 1:
        print(f'** {food_counter} orders of {item} have been added to your meal **')
        restaurant_order()
      else:
        print(f'** {food_counter} order of {item} have been added to your meal **')
        restaurant_order()       
  elif order == "quit":
    print(food_record)
    exit()
  else:
    print('***Please make a different menu selection***')



restaurant_order()