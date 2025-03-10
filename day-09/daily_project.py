# Day 9 daily project - Secret Auction Program
import time
# I am using time lib to simulate the countdown at the end.

logo = '''
                         ___________
                         |         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________|
                       .-------------.
                      /_______________||
'''

print("The Secret Auction is Starting now!")
print(logo)
print("Each one, in is turn - insert your name and then your bid!")

more_players = True

dic_bids = {}

while more_players:
    name = input("Insert your name : ")
    bid = int(input("Insert your bid in $ (make sure no one watching) : $"))
    dic_bids[name] = bid
    last_bid = input("There are more bids? (yes/no) - ")
    while last_bid not in ['yes', 'no']:
        print("Invalid input!")
        last_bid = "There are more bids? (yes/no) - "

    if last_bid == 'no':
        more_players = False

    print("\n"*100)
    # using new lines "to clean" the screen
    print(logo)

max_bid_name = ""
max_bid = 0
for key in dic_bids:
    if dic_bids[key] > max_bid:
        max_bid = dic_bids[key]
        max_bid_name = key

print("Auction is Close in:")
time.sleep(0.2)
print("3..")
time.sleep(0.7)
print("2...")
time.sleep(0.7)
print("1....")
time.sleep(0.2)
print(f"Sold to {max_bid_name} - The Highest bid was ${max_bid}")
