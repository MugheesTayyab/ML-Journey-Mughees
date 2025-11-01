
# Week 2 - Logic & Problem Solving in Python
# Author: Mughees
# Focus: Building core programming logic for Applied Machine Intelligence

# Function to generate multiplication table for a given number
def multiplication_table(n, limit=10):
    print(f"\nMultiplication Table of {n}")
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n * i}")

# Function to check whether a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

# Function to check whether a number is prime
def is_prime(num):
    if num <= 1:
        return f"{num} is not a prime number"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime number"
    return f"{num} is a prime number"

# Number guessing game
import random

def guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    target = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Enter your guess between 1 and 20: ")

        # input validation
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target} in {attempts} attempts.")
            break

# Main execution block
def main():
    print("=== Week 2: Python Problem Solving ===")

    # Multiplication Table
    num = int(input("\nEnter a number for multiplication table: "))
    multiplication_table(num)

    # Even or Odd
    num2 = int(input("\nEnter a number to check even/odd: "))
    print(even_or_odd(num2))

    # Prime Check
    num3 = int(input("\nEnter a number to check prime: "))
    print(is_prime(num3))

    # Guessing Game
    play = input("\nDo you want to play the guessing game? (y/n): ").lower()
    if play == 'y':
        guessing_game()

    print("\n--- End of Week 2 Tasks ---")

if __name__ == "__main__":
    main()
