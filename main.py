import random

number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input("Guess The Number Between 1 - 100: "))

        if guess < number_to_guess:
          print("Too Low!")
        elif guess > number_to_guess:
          print("Too High")
        else:
           print("Congratulation! You guessed the number")
           break
    except ValueError:
       print("Pleese, Enter a valid number!") 