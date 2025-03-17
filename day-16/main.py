# Day 16 - 100 Days of Code - Python

# Today's main topic - OOP in general and in python
# what is OOP?

# OOP stands for Object-Oriented Programming

# until this point , each one of the project
# that was build in this course was coded
# based on Procedural Programming

# Procedural Programming is the common and easy way :
# the program have no clear structure , each function called
# and used by any variable , and there is a main program
# that use those functions.
# in another way - we can say that the program is running
# from top to bottom (and somtimes jump to function) but
# the general flow is from top to bottom.
# It's also called "Spaghetti style"

# But somtimes we have some more complex objects in our program.
# for example - a human:
# A human have many things that defined him :
# name , age , hair color , height , weight , eye color and more..
# Human have also many functions (different activities) :
# sleeping , eating , working , drinking and many more.

# each human have different way to do somthing and
# also different thing which defined it.
# so it will be very not efficient to define each human
# in procedural programming - cause in this way , we need
# to implement function for each type of man and the code
# will be long and very complex to write and read.

# This is where the OOP is great for us.
# it's gives us a way to create object named human
# and this object have some things and function that
# defined him.
# to create new human - we just need to inherit from
# the human object , and implement only the functions
# and variable that unique for him.

# OOP also give us the option to create as many object we want from
# of the same class (Object type) so we can reuse a code to build
# different object from the same class

# OOP is great for large scale programs , which use many objects and many
# parts that based on same thing but each one working a little bit different.

# the things that defined an object called "attributes"
# the functions that object can do called "methods"
# to Object is a way to combine some data with some operations
# the type of object is called "class"

# to create a new object from class , we write this :
# object_name = class()
# so if want to create an object named Turtle from class named Animal, it will look like that:
# turtle = animal()
# the () after animal is important to activate the constructor.
# the constructor is the function that "build" the object based on
# the attributes of animal class , and also give the object the access to
# the method inside animal.

# before we continue , let's learn something important named : "Python package"
# a python package is a code that someone else write , and we can add import it
# to our program and use all the functions and variables in our program for something.
# for example - the Turtle package is a specific python package that help us build
# GUI application.
# we can add it to our python project and use it functionality in our program.
# how to add it to our project ?
# we can use something called "pip" :
# move to our project dir in the CMD or Terminal
# then type : pip install <name_of_package>
# and this will install it inside our python environment.

# another way is use the Package installer in the JetBrain Pycharm IDE , which make it a little bit intuitive.

# let's practice by using "prettytable" package:
# first , need to install it ..
# then , import it to this file :
from prettytable import PrettyTable
# and now we can create a new table object:
table = PrettyTable()
# let's see what we got:
print(table)
# we got an empty table built from symbols, boring right?
# let's add some data:
pokemon_names = ["Pikachu", "Squirtle", "Charmander"]
pokemon_type = ["Electric", "Water", "Fire"]
# now , we need to find the correct method of prettytable class to add data,
# and then we need to follow the DocString of this method and supply the correct
# parameters.

table.add_column("Pokemon Name", pokemon_names)
table.add_column("Type", pokemon_type)
# now let's print it:
print(table)
# output:
r"""
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
"""
# we can see that we created a table , in simple way
# using only lists and table object from prettytable.

# we can also change the attributes of the table object.
# let's try something:
table.align = "l"
print(table)
# output:
r"""
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
"""
# we can see that we changed the alignment of the content of table
# from center to left, cool right?

# Now - let's use the CoffeeMachine_Package to build a version of
# the previous project (Coffee machine) but this time - in OOP approach.
# to make life easier - the classes are already implemented :)
# move to the main_CM.py to watch the full code.

# we can see that the fact that we use classes and objects make our main program much more clear.
# it's also helped us that all the methods already implemented.
# so the OOP approach help us to create the same complex project - but in more clear and structured way!

