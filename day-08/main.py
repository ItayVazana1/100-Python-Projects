# Day 8 - 100 Days of Code - Python

# functions with input
# Caesar Cipher - the daily project
# converting using shift number

def greet():
    for i in range(3):
        print("Hello World!")


greet()

# what if we want to greet someone specific?
# what if we want to pass a name to the function and use it?
# we can do it by using a parameter to the function.
# def function(*insert here*)
# example:

def greet_someone(specific_name):
    print(f"Hello {specific_name} , how are you?")


someone = "David"
greet_someone(someone)

# or even do it with list :
names = ["Mishel", "David", "Itay", "Koral", "Donald"]
for name in names:
    greet_someone(name)

# function with more then 1 input:
def greet_with_name_and_loc(specific_name,specific_location):
    print(f"Hello {specific_name}")
    print(f"What is it like in {specific_location}")


locations = ["Finland", "Tokyo", "Tel-Aviv", "California", "Paris"]

i = 0
for name in names:
    greet_with_name_and_loc(name,locations[i])
    i += 1

# we can ensure the position of each string as a parameter by using keys :
i = 0
for name in names:
    greet_with_name_and_loc(specific_name=name,specific_location=locations[i])
    i += 1

# order is important - especially when working with lots of parameters.



