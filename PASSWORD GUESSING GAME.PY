import random

easy_words=["apple","train","tiger",".money","india"]
medium_words=["python","bottle","monkey","planet","laptop"]
hard_words=["elephant","diamond","umbrella","computer","almirah"]

print("Welcome to the Password Guessing Game")
print("Choose a difficulty level:easy,medium or hard")

level = input('Enter difficulty: ').lower()
if level=="easy":
    secret=random.choice(easy_words)

elif level=="medium":
    secret=random.choice(medium_words)

elif level=="hard":
    secret=random.choice(hard_words)

else:
    print("Invalid choice.Defaulting to easy level.")
    secret=random.choice(easy_words)

attempts=0
print("\n GUESS THE SECRET PASSWORD")

while True:
    guess=input("Enter yourt guess: ").lower()
    attempts+=1

    if guess==secret:
        print(f'Congratulations! You guessed it in {attempts} attempts')
        break
        
    hint =""

    for i in range(len(secret)):
        if i< len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+= "_"

    print("Hint: ",hint)
print("GAME OVER")

