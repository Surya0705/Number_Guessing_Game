import random # Importing the Random Module for this Program
Random_Number = random.randint(1, 100) # Giving our program a Range.
User_Guess = None # Defining User Guess so that it doesn't throw up an error later.
Guesses = 0 # Defining Guesses so that it doesn't throw up an error later.

while(User_Guess != Random_Number): # Putting a while loop and telling Program to stop if Guess is Correct.
    User_Guess = int(input("Enter the Guess: ")) # Taking the input from the User.
    Guesses += 1 # Adding 1 per Guess.
    if(User_Guess == Random_Number): # Telling the Program what to do if the Guess is Correct.
        print("CORRECT! You Guessed it Right!") # Printing the Greetings if the guess is Correct.
    else: # Putting an Else Condition so that the Program knows what to do in case the Guessed Number is not Correct.
        if(User_Guess >= Random_Number): # In case if the User Guess is smaller than Random Number.
            print("You guessed it Wrong! Enter a Smaller Number...") # Telling the user what to do.
        else: # Putting an Else Condition so that the Program knows what to do in case the User guess is greater that Random Number.
            print("You guessed it Wrong! Enter a Larger Number...") # Telling the User what to do.
print(f"You were able to guess the Number in {Guesses} Guesses!") # Printing the final output that you Guessed the Number in __ Number of Times.