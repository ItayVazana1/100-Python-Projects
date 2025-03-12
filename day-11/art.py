

game_logo = r"""

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/    
      
"""


game_rules = """
Game Rules:

- Players: Single-player game (in this version).
- Bank: Both the player and the computer start with the same amount of coins.
- Betting: At the beginning of each round, the player places a bet from their bank.
- Card Usage: Once a round is finished, the used cards are removed from play. When all cards are used, a new deck is introduced.
- Game End Conditions:
  1. The player chooses to quit after any round, and their final bank amount is compared to the computer’s. The side with the higher bank wins.
  2. The player runs out of coins, resulting in an automatic loss.

Round Structure:

1. Both the player and the computer receive one public (visible) card.
2. Each side is then dealt one private (hidden) card.
3. The player’s goal is to increase the total sum of their cards while staying at or below 21.
4. The player may request additional cards to get closer to 21, but exceeding 21 results in an immediate loss (bust).
5. The computer follows the "17 Rule" – if its total hand value is less than 17, it must draw another card until reaching 17 or higher.

Card Values:

- Numbered Cards (2-10): Face value.
- J, Q, K: Each worth 10 points.
- Ace (A): Can be worth either 1 or 11, based on the player’s choice.

Possible Outcomes:

1. Player wins – Their total is higher than the computer's but still 21 or less.
2. Computer wins – The computer has a higher total, 21 or less.
3. Draw – Both the player and computer have the same total, 21 or less.
4. Computer wins – The player exceeds 21 (bust).
5. Player wins – The computer exceeds 21 (bust).
"""

symbols_signs = ["♣", "♦", "♥", "♠"]
