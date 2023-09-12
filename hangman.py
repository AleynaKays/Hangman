name = input("Enter name: ")
print("Welcome"+ name + "time to play hangman")

secret_word= "kertenkele"

guess_string= ""

lives=10

while lives > 0:

    character_left=0

    for character in secret_word:

        if character in guess_string:
            print(character)
        else:
            print("-")
            character_left += 1

    if character_left==0:
        print("KAZANDIN!")
        

    guess =input("Guess a letter: ")
    guess_string += guess
    
    if guess not in secret_word:
        lives-=1
        print("Yanlış Tahmin!")
        print(f"You have {lives} left")
        
    if lives==0:
        print("KAYBETTİN")
        