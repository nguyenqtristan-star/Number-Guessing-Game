import random

def get_randNumb():
    return(random.randrange(0, 101))

def get_difficulty():
    print("\nPlease select difficulty level:")
    print("1. Easy (10 guesses)")
    print("2. Medium (5 guesses)")
    print("3. Hard (3 guesses)")
    
    difficulty = int(input("Select Difficulty: "))
    while difficulty > 3 or difficulty < 1:
        difficulty = int(input("Select Difficulty: "))


    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 5
    else:
        return 3
    
    

print("Welcome to Number Guessing Game! \nI'm thinking of a number between 1 and 100.")


while True:
    difficulty = get_difficulty()
    numb = get_randNumb()
    guess = None
    attempts = 0
    while guess != numb:
        if attempts >= difficulty:
            print("You lose by too many attempts.\n")
            break

        guess = int(input("\nEnter Guess: "))
        if guess > numb:
            print("Incorrect! the number is less than", guess, ".")
        elif guess < numb:
            print("Incorrect! the number is greater than", guess, ".")
        else:
            print("You guessed the correct number in", attempts + 1, "attempts")
            break
        attempts += 1

    play = int(input("play again?(-1 to exit): "))
    if play == -1:
        print("Thank you for playing!")
        break

















