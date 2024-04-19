guess = input("Enter word to guess: ") #take in word to guess
guess_attempt = ["_"] * len(guess) #create an empty string list to track progress of player
guess_progress = int(0)
line = []
mistake_counter = int(0) #use to track mistakes and to know which version of the graphic to print

def print_graphic(mistake_number): #function to print appropriate graphic based on in-game situation
    match(mistake_number):
        case 0:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
        case 1:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|       O")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
        case 2:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|       O")
            line.append("|       | ")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
        case 3:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|       O")
            line.append("|      /|")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
        case 4:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|       O")
            line.append("|      /|\\")
            line.append("|")
            line.append("|")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
        case 5:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|       O")
            line.append("|      /|\\")
            line.append("|       |")
            line.append("|")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
        case 6:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|       O")
            line.append("|      /|\\")
            line.append("|       |")
            line.append("|      /")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
        case 7:
            line.append("________")
            line.append("|       |")
            line.append("|       |")
            line.append("|       O")
            line.append("|      /|\\")
            line.append("|       |")
            line.append("|      / \\")
            line.append("|")
            line.append("|_____________")
            line.append("|   HANGMAN   |")
            line.append("|_____________|")
    for x in line:
        print(x)

while True:
    print_graphic(mistake_counter)
    print("Word: ")
    print(*guess_attempt)  #display progress on word to guess
    letter = input("Letter: ") #input letter to guess

    check_include = bool(False)

    for x in range(len(guess)): #iterate list
        if letter == guess[x]: #check if guessed letter is equal to the letter in the current list cell
            guess_attempt[x] = letter #add the guessed letter to the guess attempt tracker
            check_include = True #if letter is found, change value of bool
            guess_progress += 1

    if check_include == False: #if guessed letter is not found in list
        mistake_counter += 1
    
    if mistake_counter == 7:
        print_graphic(mistake_counter)
        print("\nYOU LOSE")
        break
    
    if guess_progress == len(guess): #win condition
        print_graphic(mistake_counter)
        print("Word: ")
        print(*guess_attempt)  #display progress on word to guess, at this time will be complete
        print("\nYOU WIN") #victory message
        break #exit while loop
