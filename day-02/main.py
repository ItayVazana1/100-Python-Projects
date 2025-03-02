# Day 2 - 100 Days of Code - Python

# Printing characters by index:
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
print("Hello"[-1])
print("Hello"[-2])
print("Hello"[-3])
print("Hello"[-4])
# printig a specific character from string is possible
# by using [x] when x is the index of the character in the string.
# the first index is 0 , not 1
# to access the character in reverse - we can use negative number.
# the first negative index (the last characther) is in index -1.

# Data Types in Python: 
# string = a collection of characters (ASCII) that create words , exmple:
my_string = "Hello World!"
# int (integer) = a whole number , positive and negative , example:
my_int = 5
# float = floating point number (like 4.5 , 3.12 ...) , example:
# be careful! --> if value is not inside "" , and contain . , even if some of
# the characters are not number , it is still a float!
# example : f = 734_63.265 is float , and considerd as 73463.265
my_float = 1.278
# boolean = a boolean value , True or False (start with Capital letter) - Super useful!
# be careful! --> "True" is a string , True is boolean!!
my_bool = True

print(my_string)
print(my_int)
print(my_float)
print(my_bool)

# remember len() function? this function is not working well for any number data type.
# why ? because a number object has no len().
# the len() is working only on somthing like collection of items , like:
# String , Array , List , Tuple...

#if we need to check what is the type of specific variable , we can use type() function
#(inside a print to print the result):
print(type(my_string))
print(type(my_int))
print(type(my_float))
print(type(my_bool))

# converting of data types
# it is possible to convert the string "123" to the number 123.
# we can do that with casting to specific data type which we want.
# first we have this: 
num1 = "123"
num2 = "456"
# and we want to add them and get the result :
print(num1 + num2)
# we got "123456" , because + between string is just print them concatned..
# but if we will use this :
print(int(num1)+int(num2))
# and now we got the result. which is equal to 579
# this casting is also helps when we want to print string and number in the same sentence:
number = int(num1)
print("this is string and the number is " + str(number) ) 
# pay attention ! some times , casting can make lose of data.
# lets take an example of casting from float to int:
new_float = int(my_float)
print("original float is " + str(my_float))
print("after casting to int " + str(new_float))
# as we can see , we lost the data that smaller then 1 , so we get only the whole part of the float.

# Math operations on variables : 
# adding:
print(5+4)
# sub:
print(5-4)
# multiply
print(5*4)
# divide
print(5/4) #this will always return a float.
# divide without reminder (only int result)
print(5//4)
#exponent (a ** b) = a^b
print (3 ** 3)

# the right order of operations : 
# PEMDAS
# 1 - () Parenyhesses 
# 2 - ** Exponent
# 3 - * Multiply
# 4 - / and // Devide (with or without remider)
# 5 - + adding
# 6 - - substrct

# rounding of number
# the first techniq is to floor it by casting to int..
# this is not always correct beacause 3.99 will converted to 3
# which is wrong beacause its closer to 4.
# insted , a best practice is to use floor() function.
number = 3.784
print("original number = " + str(number))
print("round using casting to int = " + str(int(number)))
print("round using round function = " + str(round(number)))

# while rounding . we can also "cut" the length of number if the resulotion is to high:
number = 3.7858468486847
print("original number = " + str(number))
print("the number in .01 format = " + str(round(number,2)))

# change value of variable using itself:
# option 1 - using the full format:
score = 0
score = score + 1
# option 2 - using short syntax : 
score += 1

# fstring = combine data types in a string in native way:
# this is the old way :
new_num = 123
my_str = "I am " + str(new_num)
# the new way:
my_str1 = f'I am {new_num}'
print("this is the old format --> " + my_str)
print("and this is the fstring format --> " + my_str1)
