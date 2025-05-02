import random

play = True

while play:
    
    secret_number = random.randint(1,100)
    attempts = 0

    while True:
        try:
            if attempts == 10: 
                print("❌ You have reached the maximum number of attempts!")
                print(f"The correct number was: {secret_number}")
                break
            else:
                guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("❌ Please Enter a valid number")
            continue
        
        attempts += 1
        
        if guess < secret_number: 
            print("Too Low! Try Again")
        elif guess > secret_number:
            print("Too High! Try Again")
        else:
            print(f"Congratulations you guessed it in {attempts} attempts")
            break
            
    playAgain = input("Do you want to play again ? yes/no").strip().lower()
    
    if playAgain != "yes":
        play = False
        print("👋 Thanks for playing!")
