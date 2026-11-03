from ast import While
import random

secret_number = random.randint(1, 100)
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Congratulations ^_^! You guessed the number!")
            break
        elif guess < secret_number:
            print("Haaah!Too low: Try again.")
        else:
            print(" heheh!Too high Try again.")   
            break
        if guess ==  secret_number:
          print("Congratulations🎉! You guessed the number!")
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


        
        secret_number= random.randint(200,300)
print("Welcome to the second round of the Guess the Number game!")
print("I'm thinking of a number between 200 and 300.")

 


        