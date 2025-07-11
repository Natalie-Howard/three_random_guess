import random
def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    #print("Target: ", target) #for debugging
    while tries > 0:
        print(f"Number of tries left {tries}: ")
        guess = int(input(f"guess a random number between {start} and {stop}: "))

        if guess == target:
            print("You guessed the correct number!")
            return
        
        elif guess < target:
            print("Guess higher!")

        else:
            print("Guess lower!")

        tries -= 1
    print(f"You failed to guess the number: {target}")
#---------------------------------------------------

def guess_random_number_linear(tries, start, stop):
    target = random.randint(start, stop)
    print("The number for the program to guess is: ", target)

    for guess in range(start, stop +1):
        print("Number of tries left: ", tries)
        print("The program is guessing...", guess) 

        if guess == target:
            print("The program has guessed the correct number!")
            return guess 
        
        tries -= 1   

        if tries <= 0:
            print("The program has failed to guess the right number.")
            return None
#---------------------------------------------------

def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop +1)
    lower_bound = start
    upper_bound = stop 
    print(f"Random number to find: {target}")
    while lower_bound <= upper_bound:
        guess = (lower_bound + upper_bound) // 2        
        #print("Guessing:", guess) #to see what it's guessing

        if guess == target:
            print(f"Found it! {target}")
            return target
        elif guess > target:
            upper_bound = guess - 1
            print("Guessing lower!")
        else:
            lower_bound = guess + 1
            print("Guessing higher!")
        
        tries -= 1
        if tries <= 0:
            print("Your program failed to find the number.")
            return None

    return None #in the interest that all things are possible

#--------------------Driver code------------------------------

guess_random_number(5, 0, 10) 
#guess_random_number_linear(5, 0, 10)
#guess_random_num_binary(5, 0, 100)
