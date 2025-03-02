# Day 1 - 100 Days of Code - Python

print("Hello world!")

# C:\Users\itay3\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\itay3\Desktop\Courses\100 Days of code - python\Day 01\main.py"
# that is the location where this file is running
# shift + F10 = keyboard shortcut to run the program
# the "" inside the print function is a symbol for printing the value inside the " " as a String.
# the first " defined where the string is started and the other " defined the end
# if the " will not be close , like : "string...  , then it's would be an error :
#   File "C:\Users\itay3\Desktop\Courses\100 Days of code - python\Day 01\main.py", line 3
#     print("Hello world!)
#           ^
# SyntaxError: unterminated string literal (detected at line 3)
# another way to detect errors before running is to search for red squiggly lines under code , and then
# stand on it with the mouse cursor and see more about the error.

# print some strings one after one:
print("Hello world!")
print("I am Itay!")
# do the same thing but in one print command:
print("Hello world!\nI am Itay!")
# remember that if you want a clean next line , make sure you are not adding " " or TAB after \n

# print strings with '+' symbol between them:  (String Concatenation)
print("Hello" + "world!")
# the output will be this : Helloworld!, which mean - without a gap , space or TAB between them.
# so if we want the Space between , then we need to code it like that:
print("Hello" + " " + "world!")
# or
print("Hello " + "world!")

# space is a big issue in python , look what happening when add space before print command:
# File "C:\Users\itay3\Desktop\Courses\100 Days of code - python\Day 01\main.py", line 31
#    print("Hello " + "world!")
# IndentationError: unexpected indent
# a correct indent in python program is important to compile it correctly !

# print is great to show data , but how we can get input ?
# to get data from user we change the print to input , the content inside the () is stays the same.
# but for using this data we need to store it in a variable , or at least use it inside a print, example:
print("Hey , " + input("Hey What your name?") + ", I hope this is your real name!")
# another way is to store it in a variable and then print it , which give us the option to use the data
# again , but no immediate.
# we can declare a variable by just assign the input with = , like here:
name = input("I am asking again...what is your name?")
print("OK , " + name + ", I choose to believe you!")
# now we can access the content of the 'name' variable whenever we want, by using the reference 'name'.
# we can also change the content of main , by assign it to another input or constant string , like this:
name = 'Koral'
print("My name is " + name + ", nice to meet!")
# we can also check what is the length of the string that inside 'name' , with len(name):
length = len(name)
print(length)  # which is 5
# comments in python (like this one) is created by add the '#' symbol before the content we want to comment.


# Choose name of variables wisely!
# - Use names with clear meaning ("name" is better than "n")
# - If the name is too long , use '_" to separate between words ("my_name" is better than "myname")
# - Don't use name that is identical to function names (like "print" or "input")

