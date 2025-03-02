print("Hello , and welcome to the Band Name Generator!\nI will help you to generate the perfect name for your band!")
in_name = input("So , before we start - what is your name?\n")
print("OK ," + in_name + " , I will ask you 2 questions to generate the perfect name:")
in_city = input("First , what is the name of the city that you grew up in?\n")
in_pet = input("Second , what is the name of your pet?\n")
band_name = in_city + " " + in_pet
print("Well done " + in_name + "!\nSo the name for your new band is ---> " + band_name)