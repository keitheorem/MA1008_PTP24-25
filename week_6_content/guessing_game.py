import random 
while True: 
    random_number = random.randint(0,100)
    print("This is a number guessing game!")
    print("Guess a number between 0-100 inclusive")

    for i in range(5,0,-1):
        guess = int(input("Your guess: "))
        
        if guess > random_number: 
            print("Too high")
        
        if guess < random_number: 
            print("Too low")

        if guess == random_number: 
            print("Correct. Well done. You got it in 5 tries!!")
            break
        
        if i > 2:
            print("You have" , i-1, "tries remaining...")
        
        if i == 2: 
            print("You have" , i-1, "try remaining...")
        
        if i == 1:
            print("Tough luck. You had your 5 tries.")
            print("The number is ", random_number)
    
    play_again = input("Want to play again? Enter Y for Yes, N for no: ")

    if play_again == 'N':
        break
