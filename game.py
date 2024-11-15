#importing necessary modules
import random
import time

#functions based on the difficulty level chosen
def Easy(num):
    # Record the start time
    start_time = time.time()
    print("Great! You have selected the Easy difficulty level.\nLet's start the game!")
    attempts=10
    return check(start_time,attempts)

def Medium(num):
    # Record the start time
    start_time = time.time()
    print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
    attempts=5
    return check(start_time,attempts)

def Hard(num):
    # Record the start time
    start_time = time.time()
    print("Great! You have selected the Hard difficulty level.\nLet's start the game!")
    attempts=3
    return check(start_time,attempts)

#function to check if the guess is correct and calculate the total time taken to complete the game
def check(start_time,attempts):
    i=0
    while i<attempts:
        guess=int(input('\nEnter your guess: '))
        if guess==num:
            print("\nCongratulations! You guessed the correct number in {0} attempts.".format(i))
            break
        else:
            if guess>num:
                status="less"
            else:
                status="greater"
            print("\nIncorrect! The number is {0} than {1}.".format(status, guess))
        i+=1
    # Record the end time
    end_time = time.time()
    
    total_time=end_time-start_time
    print(f"Game completed in {total_time:.2f} seconds.")

#printing the welcome message
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\n\n")
print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")

#chossing the difficulty level
difficulty=int(input('Enter you choice: '))

#generate the random number between 1 and 100
num=random.randint(1,101)

if difficulty==1:
    Easy(num)
elif difficulty==2:
    Medium(num)
elif difficulty==3:
    Hard(num)