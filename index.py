import random

secret_number = random.randint(1,100)
attemps = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attemps += 1
    
    if guess < secret_number: 
        print("Too Low! Try Again")
    elif guess > secret_number:
        print("Too High! Try Again")
    else:
        print(f"Congratulations you guess it in {attemps} attemps")
        break