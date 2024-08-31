# Write a program to bet on the value produced by rolling a dice. The value of the dice
# rolling is produced by a random number generator.

import random 

# Receive bet from user
user_bet = int(input("Your bet: "))

# Generate random number
dice_result = random.randint(1,6)

if dice_result == user_bet: 
    print("The dice value is", dice_result, ". You win.")

else:
    print("The dice value is ", dice_result, ". You lose.")

