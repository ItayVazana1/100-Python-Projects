# Day 9 - 100 Days of Code - Python

# Dictionaries and Nesting

# What is a Dictionary in python ?
# dictionaries in python works the same as real dictionary:
# it's a bunch of sets of 2 parameters : key and value.
# the key is the label of the content of the row , and we can
# access to this row by access the key
# the value is the other part of the set , and this is
# the real value behind the key.
# for example , if we want to create a dictionary , such that each
# key is a Letter in english and each value is a name that start
# with that letter , it will look something like that :
# dic = {
#           A : 'Angela'
#           I : 'Itay'
#           R : 'Ronald'
#       }
# so if we try access the value 'Itay' , we should to achieve
# it by using the Key I.


# here is how we create a dictionary in python:

dic = {"A": "Angela"}

print(type(dic))

# we can create a dictionary with more than one set:

dic1 = {"A": "Angela", "I": "Itay", "R": "Ronald"}

# but there is a more organized and pretty way to define the dictionary
# in the code - by using an appropriate indent , like that:

dic2 = {
    "A": "Amir",
    "B": "Beri",
    "C": "Candy"
}

# what is the big deal with dictionaries ?
# the fact that we can't access a value using the value.
# that says that the value is safe and hidden behind the key.
# we will use this information in our daily project.

# make sure when you define the dictionary , if the key is a string and not a number
# you must put it inside ' ' !

# so how we access values? here is an example:

print("this is how we access the 'Angela' value by using the key 'A'")
print(dic1['A'])

# if we will try to access value by itself - it will raise an error:
# print(dic2['Angela'])
# the error is : KeyError: 'Angela' , which mean there is no key called 'Angela'.

# we can also print the full dictionary this way:
print("this is the full dictionary:")
print(dic1)

# to add values (by define a key) to dictionary , we do this:
dic1['z'] = 'zebra'

# looping through a dictionary :
# let's see what is happening when we loop over a dictionary with for loop:
for thing in dic1:
    print(thing)

# the output is the available keys in the dictionary - not the values!
# so if we want to access the values in this approach we need to use the
# key that we got to access each value :

for key in dic1:
    print(f"[{key}] is the key fot the value [{dic1[key]}]")

# Nesting in python :
# Simply - just store a data structure inside another one.
# for example - list as an item in list , list as a value in dictionary
# or dictionary as item in list or dictionary as value of dictionary.

# Nesting give us a way to store more than one value behind one key.
# example :
ABC_dict = {
    'A': ['Algorithm', 'Animal', 'Automata'],
    'B': ['Basketball', 'Binary', 'Brave'],
    'C': ['Cave', 'Clock', 'Cooking']
}

# So now - if we want to access each values behind each key,
# we do this by access the list and then the items inside:
for key in ABC_dict:
    print(f"Words that starts with {key}:")
    for item in ABC_dict[key]:
        print(f"- {item}")

# we can also store both lists and regular values inside the same data structure:
ABC_dict1 = {
    'A': ['Algorithm', 'Animal', ['Automata']],
    'B': ['Basketball', 'Binary', 'Brave'],
    'C': ['Cave', 'Clock', 'Cooking']
}

# now , to access the string 'Automata' , we do this:
print(ABC_dict1['A'][2][0])

# so we cant nest more and more data structures inside each other,
# but be careful - it will also make it more complex
# to access specific data and add items to the data structure.

