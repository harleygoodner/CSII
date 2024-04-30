#Author: Harley Goodner
#Date: April 3, 2023
#Discription: This code allows a user to play a simple game of battleship against the computer. The game lasts 10 rounds and if either player successfully sinks all four of the opponent's ships, they win and the game ends. The user places their ships wherever on the 5x5 board, and the computer randomly places their ships on their 5x5 board.

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
        user_won, comp_won = False, False
        user_won, hit_map, user_hits= user_move(turn, computer_map, hit_map, user_hits)
        if user_won:
            break
        comp_won, user_map, comp_hits = computer_move(user_map, comp_hits)
        if comp_won:
            break
        
    if not user_won and not comp_won:
        print("Ten Rounds complete. The game ends in a tie.")


    



def computer_setup(computer_map):
    '''
    allows the computer to randomly place its four ships on its map
    takes the computer map
    returns computer map with the four ships randomly placed on it
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
    '''
    allows the user to place their ships wherever they want on the map
    takes the user map
    returns user map with the four ships placed on it
    '''
    counter = 0
    while True:
        while True:
            try:
                row = (int(input("What row do you want to place your ship (1-5): ")) -1)
                column = (int(input("What column do you want to place your ship (1-5): ")) -1)
                break
            except:
                print("improper input")
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
    '''
    allows the user to guess where the computer's ships are located
    takes turn, which is a counter of the amount of rounds remaining, takes the computer map, takes the hit map (map of where the user has guessed and the result of those guesses), takes user_hits, which is a counter of the amount of ships the user has sank
    returns user_won (boolean for if the user has won and game should end), the hit map, and the user_hits counter
    '''
    while True:
        print(f"This is the computer's map: {display_map(hit_map)}")
        while True:
            try:
                user_column = (int(input("Guess ship column position (1-5): ")) -1)
                user_row = (int(input("Guess ship row position (1-5): ")) -1)
                break
            except:
                print("improper input")
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
    user_won = False
    if user_hits == 4:
        print("You sunk all of the computer's ships! You win! Game over.")
        user_won = True

    return user_won, hit_map, user_hits
        

def computer_move(user_map,comp_hits):
    '''
    allows the computer to randomly guess where the user's ships are located
    takes the user map and comp_hits, a counter of the amount of ships the computer has sunk
    returns comp_won (boolean for if the user has won and game should end), the user map, and the comp_hits counter
    '''
    row = random.randrange(0,4)
    column = random.randrange(0,4)
    if user_map[row][column] == 1:
        print("Computer's turn...Computer sunk your battleship :(")
        comp_hits +=1
    elif user_map[row][column] == 0:
        print("Computer's turn...Computer missed your battleship :)")
    comp_won = False
    if comp_hits == 4:
        print("Computer has sunk all your ships. You lose. Game over.")
        comp_won = True

    return comp_won, user_map, comp_hits




def display_map(map):
    '''
    displays a board so that the user can see the locations that they have already guessed and the results of those guesses
    takes the variable map which is the board
    returns nothing since the map is printed within the function
    '''
    for i in map:
        print(i)


    
if __name__ == '__main__':
    main()
