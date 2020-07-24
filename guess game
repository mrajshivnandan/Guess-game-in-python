n= 18
no_of_guess= 1
print("Guesses are limited upto 9 number")
while(no_of_guess<= 9):
    try:
        guess_no= int(input("Guess a number:\n"))
        if guess_no<18:
            print("Please enter a greater number")
        elif guess_no>18:
            print("Please enter a lesser number")
        else:
            print("You are a winner")
            print(f"You took {no_of_guess} guess to finish the game")
            break

        print(9-no_of_guess, "number of guesses left")
        no_of_guess= no_of_guess + 1
        if no_of_guess> 9:
            print("game over")
    except Exception as e:
        print(f'Error - Only numbers are allowed to type!')
