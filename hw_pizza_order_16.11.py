from os import system
system ('cls')



# ############################## CHOICE AND CHECK
food_1_name      = 'Pizza'
food_1_price     = 200   
food_1_available = 5
food_1_quantity  = int(input('How many ' + food_1_name + ' do you want ?'))

if food_1_quantity >= 0 and food_1_quantity <= food_1_available:
    food_1_cost = food_1_quantity * food_1_price
else:
    print("We have only: ", food_1_available )
    food_1_quantity = 0
    food_1_cost = 0


food_2_name      = 'Pasta'
food_2_price     = 70   
food_2_available = 10
food_2_quantity  = int(input('How many ' + food_2_name + ' do you want ?'))

if food_2_quantity >= 0 and food_2_quantity <= food_2_available:
    food_2_cost = food_2_quantity * food_2_price
else:
    print("We have only: ", food_2_available )
    food_2_quantity = 0
    food_2_cost = 0


food_3_name      = 'Cola'
food_3_price     = 50   
food_3_available = 10
food_3_quantity  = int(input('How many ' + food_3_name + ' do you want ?'))

if food_3_quantity >= 0 and food_3_quantity <= food_3_available:
    food_3_cost = food_3_quantity * food_3_price
else:
    print("We have only: ", food_3_available )
    food_3_quantity = 0
    food_3_cost = 0
# ##############################


# ############################## COST
if food_1_quantity > 0:
    print('You took ' + str(food_1_quantity) + ' x ' + str(food_1_name) + ' = ' + str(food_1_cost))
if food_2_quantity > 0:
    print('You took ' + str(food_2_quantity) + ' x ' + str(food_2_name) + ' = ' + str(food_2_cost))
if food_3_quantity > 0:
    print('You took ' + str(food_3_quantity) + ' x ' + str(food_3_name) + ' = ' + str(food_3_cost))

total = food_1_cost + food_2_cost + food_3_cost
# ##############################


# ############################## DELIVERY
if food_1_quantity > 0 or food_2_quantity > 0 or food_3_quantity > 0:
    delivery = input( "Do you want delivery? (y/n) ")
    delivery_cost = 150
    if delivery == "y":
        if total >= 1000:
            print ("Your delivery is free and total cost of the order is:", total)
        else:
            total += delivery_cost
            print ("Your delivery cost is ", delivery_cost, "and total cost of the order is:", total)
    else:
        print("Your total cost of order is:", total)
else:
    print("You didn't order anything.")
# ##############################
    

