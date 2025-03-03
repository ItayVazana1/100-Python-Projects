# Day 3 - 100 Days of Code - Python

# conditions in python
# "if" condition is useful when we want to control the flow of program based on specific conditions.
# what can be the condition ? many , many things . for example :
# check if value of variable is equal or different or larger or smaller when compared to somthing.
# current state of boolean variable
# combination of some conditions (AND)
# one or more of condition from the combination is True (OR)

# Just to be clear , we need to remember - a conditions is True when the statement is true , and false when not.
# another thing that we need to know is how to use "else".
# this is the another option the flow move to when the condition is False.
# if the condition is True , the block of code under else will not execute.
# in the same way , if condition is False , the block of code under if(statement) will not execute.


# example of using if without else:
my_name = "Itay"
if my_name == "Itay" :
    print("correct")

# example of using if with else:
if my_name == "Maxim":
    print("this is Maxim")
else:
    print("this is not Maxim")

# we can also use "elif" which is else with if:
if my_name == "Maxim":
    print("this is Maxim")
elif my_name == "Itay":
    print("this is Itay")
else:
    print("this is not Maxim")

# Modulo = unique math operation .. the result of using it is the reminder of divide a with b :
# a mod b = the reminder of a/b , without the whole number.
# we can describe it more simply : if a is the number of apples , and b is the number of baskets,
# assuming we need to insert equal amount of apples to each basket.
# the number of baskets with equal amount of apples is the result of a//b.
# and that say -> a mod b = c , and c is the number of apples we cannot insert them to any basket.
# why we cant ? beacause if we wil add them equaly to each basket , there will be basket
# in the end with lower amount of apples.
# I hope the idea of Modulo is more clear now :)

#example of using modulo:
a = 5
b = 4
print("this is a/b = " + str(a/b))
print("this is a//b (without reminder) = " + str(a//b))
print("this is a/b - a//b (only reminder) = " + str((a/b)-(a//b)))
print("this is a mod b (the reminder of when we try to inset a into b the reminder) = " + str(a%b))
print(f"explanation why this is the result of a mod b:\nwe have {a} apples and {b} baskets\n"
      f"the apples amout in each one of the basket should be equal.\n"
      f"so 4 basket , 4 apples , and the reminder apple (the last one) is 1")

# condition inside condition :
# lets look at this block of code:
name = "Itay"
age = 27
gender = "male"
favorite_anime = "one piece"
score = 0

if name == "Itay":
    score += 1
    if age < 14:
        score +=1
    elif 14 < age < 30:
        score +=2
    else :
        score += 0.5
    if favorite_anime == "Dragon Ball":
        score +=0.5
    else:
        score += 1
    if gender == "male":
        score -= 1
    else:
        score -= 0.5
else:
    score = 1

print(score)

# we can see that the flow of the program (the value of score) is based on 4 different parameters.
# this technique can help us to build programs that for each combination of parameters the result will be different.

#example: pizza ordering system:
print("Welcome to my pizzeria!")
total_bill = 0
size = input("Please choose Size: S/M/L")
if size == "s" or size == "S":
    total_bill += 7.5
elif size == "m" or size == "M":
    total_bill += 10
elif size == "l" or size == "L":
    total_bill+=12
else:
    print("Invalid input!")
    exit(1)
upgrade = True
while upgrade:
    print("Toppings Menu:\nRegular(+0.5$):\n1.Tuna\n2.Olives\n3.Tomato\n\nSpecial(1.5$):\n1.Extra Cheese\n2.Mushrooms\n3.Boild Egg\n")
    topping = input("want some topping on your pizza?\nplease choose:\nN-No please , R-Yes,Regular topping , S-Yes,Special topping")
    if topping == "n" or topping == "N":
        upgrade = False
    elif topping == "r" or topping == "R":
        total_bill += 0.5
    elif topping == "s" or topping == "S":
        total_bill += 1.5
    else:
        print("Invalid input! Try again..")
print(f"The total bill for your pizza is ${total_bill}")

# As mentiond before , we can use combination of statement in the same condition. Here are some examples:
a = 5
b = 7
c = 5
# not = use it when the condition is need to be Fasle to get inside the "if block"
# and = use it when the condition is need to be True for each one of the sub-conditions to get inside the "if block"
# or = use it when the condition is need to be Fasle to get inside the "if block"
# != is different and == is equal
# we can use all of those in the same condition to make complex conditions as we wish.. some examples:

if not a == b and a == c :
    print(f"a=c={a} and b={b}")

if a == b or b == 7 or c == 2:
    print(f"one of the conditions is true:\n1.a=b={a}\n2.b={b} and equal to 7\n3.c={c} and equal to 2")

if not a==b and (a == c or c == 1):
    print(f"the condition a={a} , b={b} and {a}={b} must be False AND also a need to be equal to c={c} OR c=2")
    