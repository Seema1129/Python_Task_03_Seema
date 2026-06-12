# Number Guessing Game

secret_number = 25
attempts = 0

print("Guess the number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        print("Number of attempts:", attempts)
        break
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")