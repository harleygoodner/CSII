#Author: Harley Goodner
#Date: April 3, 2023
#Discription: This 

import random

def main():
    '''
    main function that executes entire program
    '''
    computer_map = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    hit_map = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    user_map = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    user_map = user_setup(user_map)
    computer_map = computer_setup(computer_map)
    display_map(computer_map)

    user_hits = 0
    comp_hits = 0
    for turn in range(10):
        userwon, compwon = False, False
        userwon, hit_map, user_hits= user_move(turn, computer_map, hit_map, user_hits)
        if userwon:
            break
        compwon, user_map, comp_hits = computer_move(user_map, comp_hits)
        if compwon:
            break
        
    if not userwon and not compwon:
        print("Ten Rounds complete. The game ends in a tie.")


    



def computer_setup(computer_map):
    '''
    creates a dictionary that collects the frequency of words in a text file and then graphs them with a pie chart
    takes the variable file_in which is defined by the text file that is being examined
    returns a dictionary of word frenquenies and a pie chart of the top 10 most frequent words
    '''
    counter = 0
    while True:        
        row = random.randrange(0,4)
        column = random.randrange(0,4)
        if computer_map[row][column] == 1:
            continue
        elif computer_map[row][column] == 0:
            computer_map[row][column] = 1
            counter +=1
            
        if counter == 4:
            break
    
    return computer_map


def user_setup(user_map):
    counter = 0
    while True:
        row = (int(input("What row do you want to place your ship (1-5): ")) -1)
        column = (int(input("What column do you want to place your ship (1-5): ")) -1)
        if row not in [0,1,2,3,4] or column not in [0,1,2,3,4]:
            print("You choose a location outside the map. Choose a location in the map.")
        elif user_map[row][column] == 1:
            print("You already placed a ship in this row. Choose a different location")
            continue
        elif user_map[row][column] == 0:
            user_map[row][column] = 1
            print("Ship placed!")
            counter += 1

        if counter == 4:
            break
        
    return user_map

def user_move(turn, computer_map, hit_map, user_hits):
    while True:
        print(f"This is the computer's map: {display_map(hit_map)}")
        user_column = (int(input("Guess ship column position (1-5): ")) - 1)
        user_row = (int(input("Guess ship row position (1-5): ")) - 1)
        if user_column not in [0,1,2,3,4] or user_row not in [0,1,2,3,4]:
            print("You guessed a row outside the map. Try again.")
        elif hit_map[user_row][user_column] == "🌊" or hit_map[user_row][user_column] == "🚢":
            print("Already guessed, try again")
        elif computer_map[user_row][user_column] == 1:
            print("Battleship Sunk!")
            hit_map[user_row][user_column] = "🚢"
            print(f"{9-turn} rounds left")           
            user_hits +=1
            break
        elif computer_map[user_row][user_column] == 0:
            print("Missed")
            hit_map[user_row][user_column] = "🌊"
            print(f"{9-turn} rounds left")
            break           
    userwon = False
    if user_hits == 4:
        print("You sunk all of the computer's ships! You win! Game over.")
        userwon = True

    return userwon, hit_map, user_hits
        

def computer_move(user_map,comp_hits):
    row = random.randrange(0,4)
    column = random.randrange(0,4)
    if user_map[row][column] == 1:
        print("Computer's turn...Computer sunk your battleship :(")
        comp_hits +=1
    elif user_map[row][column] == 0:
        print("Computer's turn...Computer missed your battleship :)")
    compwon = False
    if comp_hits == 4:
        print("Computer has sunk all your ships. You lose. Game over.")
        compwon = True

    return compwon, user_map, comp_hits




def display_map(map):
    for i in map:
        print(i)


    
if __name__ == '__main__':
    main()