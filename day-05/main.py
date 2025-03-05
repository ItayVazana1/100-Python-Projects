# Day 5 - 100 Days of Code - Python

# Python loops
# When we want do somthing for more then one time,
# it's commone to use loops.
# types of loops in python :

# for loop
# the for loop is useful when we want to do somthing
# X time , which mean - do the operation X times ,
# without another condition.

# for loop (using range) :
x = 1
for i in range(0,5):
    print(f"2 in the power of {i} = {x}")
    x *= 2

# for loop on list (using items) :
my_list = ["Apple", "Banana", "Mango"]
for fruit in my_list:
    print(f"I love {fruit}")

# we can use loop to scan a list highest/lowest number
# also we can sum all of them (we dont even need a loop for that!)
new_list = [58, 100, 78, 95, 89, 98]
# sum with loop :
sum_list = 0
for num in new_list:
    sum_list += num
print(sum_list)

# sum without loop :
new_sum_list = sum(new_list)
print(new_sum_list)

# find highest:
num_max = 0
for num in new_list:
    if num_max < num:
        num_max = num
print(f"The max is {num_max}")

# find lowest:
num_min = 0
for num in new_list:
    if num_min == 0:
        num_min = num
    elif num_min > num:
        num_min = num
print(f"The min is {num_min}")

# FizzBuzz Game :
for i in range(1,100):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)








