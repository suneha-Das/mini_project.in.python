import random
lower_bound= 1
upper_bound= 1000
max_attempts= 10

secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input(" guess a number between the given range:"))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input, please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            
def check_guess(guess, secret_number):
    if guess == secret_number:
        print ("Correct")
    elif guess < secret_number:
        print ("Too low")
    else:
        print ("Too high")

    
def play_game():
    attempts = 0
    won = False
    while attempts < max_attempts:
        attempts +=1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print("congratulations! you guessed the secrect number", (secret_number), "in", (attempts), "attempt.")
            won = True
            break
        else:
            print("Try again!")

    if not won:
                  print("sorry, you ran out of attempts! The secret number is", (secret_number), ".")

            
if __name__ == "__main__":
                  print("welcome to the Number guessing game!")
                  play_game()
                  
