counter = 0

# Get numbers 1 to 1000
for i in range(2,1001):
    is_prime = True

    # Use this loop to determine if it is a prime number or not 
    for a in range(2,i): 
        if i%a == 0: 
            is_prime = False
            break

    # Check if last digit is 7 
    string_num = str(i)
    if string_num[-1] == "7":
        is_prime = False

    # If is_prime == True: 
    if is_prime: 
        print(f"{i:>4}", end = " ")
        counter += 1
    
    # after every 10 prime numbers, print a space
    if counter%10 == 0: 
        print("")


