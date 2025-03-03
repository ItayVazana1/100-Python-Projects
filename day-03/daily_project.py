# day-3 project - find the treasure!

print("Welcome to your adventure to find the treasure!")
player_name = input("First , insert your name:\n")
print(f"Hey {player_name} , you need to arrive to the beach to procced..\n"
      f"How you want get there?\n")
q1 = int(input("insert the number of your chosen option:\n"
           "1 - take a flight with plane\n"
           "2 - take a ride with your car\n"
           "3 - walking easy and safe,using your legs\n"
           "option : "))
if q1 == 2:
    print("you got flat tire .. so unlucky.. maybe next time :)")
    exit(0)
elif q1 == 1:
    print("you arrived the beach after short flight .. what a style!")
elif q1 == 3:
    print("you arrived the beach.. maybe drink some water , you look tired..")
else:
    print("Invalid Input.. back to start position! bye bye!")
    exit(0)
print(f"Great job {player_name}! now , you need to find the right way from here.\n"
      f"Which direction you choose:\n")
q2 = int(input("insert the number of your chosen option:\n"
           "1 - right\n"
           "2 - left\n"
           "option : "))
if q2 == 1:
    print("you fall and broke your leg .. put some ice on it .. maybe next time :)")
elif q2 == 2:
    print("you find 3 doors in the middle of nowhere - red , yellow and blue")
else:
    print("Invalid Input.. back to start position! bye bye!")
    exit(0)
print(f"So {player_name} , you need to Choose a door.. but which one?\n")
q3 = int(input("insert the number of your chosen option:\n"
           "1 - Red\n"
           "2 - Yellow\n"
           "3 - Blue\n"
           "option : "))

if q3 == 1:
    print("you find a room full of hungry lions.. The game is over for you.")
    exit(0)
elif q3 == 3:
    print("you find yourself at the hospital after some hours.. what was happened?? The game is over for you...(?)")
    exit(0)
elif q3 == 2:
    print("you found it!! well done! ---- You are the Winner!")
else:
    print("Invalid Input.. back to start position! bye bye!")
    exit(0)
