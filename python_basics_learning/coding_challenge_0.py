"""_summary_
Warm Up: Number Guessing Game:
Write a Python program that plays a simple number-guessing game with the user. The program should:
Generate a random number between 1 and 100.
Allow the user to guess the number in a limited number of attempts (e.g., 5).
Provide feedback to the user after each guess, indicating if the guess is too high, too low, or correct.
Keep track of the number of attempts taken by the user.
Hints:
Use the random module to generate a random number.
Use loop statements to iterate through the user's guesses.
Use conditional statements to compare the guess with the generated number.
Use string formatting to display feedback and information to the user.

"""
import random

def guess_number():
    random_num = random.randint(1,100)
    print(random_num)
    limited_attempts = 5
    while limited_attempts > 0:
        user_input = int(input("Enter a number: "))
        if(user_input > random_num):
            print(f"The number you have entered is {user_input} is too high.")
        elif(user_input < random_num):
            print(f"The number you have entered is {user_input} is too low.")
        else:
            print(f"Great work! you have guessed correctly!")
            break
        limited_attempts -= 1
    else:
        print(f"You have run out of tries.")
def main():
    guess_number()

if __name__ == "__main__":
    main()
    