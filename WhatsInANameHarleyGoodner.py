#Author: Harley Goodner
#Date: February 28, 2023
#Discription: This code was created to come up with a plethora of the string class functions from scratch in order to manipulate a string which was, in this case, a person's name.
#Bugs: None Found

import random
def main():
    '''
    This is the main where I prompt the user to enter their name and then choose from a menu of options to modify it
    I call the modifying functions from the main
    '''
    user_name = input("What is your name? ")            #user is inputting their full name here
   
    run = True

    while run is True:
        menu = input("What do you want to do? \n 1. Reverse name and display \
\n 2. Determine the number of vowels \n 3. Determine number of consonents \
\n 4. Return first name \n 5. Return last name \n 6. Return middle name \
\n \7. Return boolean if last name contains a hyphen \n 8. Convert name to all lowercase \
\n 9. Convert name to all uppercase \n 10. Scramble name \n 11. Return boolean if first name is a palindrome \
\n 12. Make initials from a name \n 13. Return name as alphabetical list of characters \
\n 14. Return boulean if name contains a title/distinction \n 15. Rank name based on its popularity \
\n Q. Quit \n Enter your Choice: ")
        if menu == "1":
            reverse_name(user_name)
        if menu == "2":
            find_vowels(user_name)
        if menu == "3":
            find_consonents(user_name)
        if menu == "4":
            get_firstname(user_name)
        if menu == "5":
            get_lastname(user_name)
        if menu == "6":
            get_middlename(user_name)
        if menu == "7":
            is_hyphen(user_name)
        if menu == "8":
            make_lowercase(user_name)
        if menu == "9":
            make_uppercase(user_name)
        if menu == "10":
            scramble_name(user_name)
        if menu == "11":
            is_palindrome(user_name)
        if menu == "12":
            get_initials(user_name)
        if menu == "13":
            make_alphabetical(user_name)
        if menu == "14":
            is_title(user_name)
        if menu == "15":
            how_popular(user_name)
        if menu == "Q":
            run = False
            print("Bye!")
            return



def reverse_name(name):
    '''
    this function reverses and displays the name
    takes name
    returns the name in reverse order
    '''
    index = len(name)-1
    while index >= 0:
        letter = name[index]
        print(letter, end="")
        index -= 1


def find_vowels(name):
    '''
    determines the number of vowels in the user's name
    takes name
    returns the number of vowels in the name
    '''
    vowels = 0
    for letter in name:
        if letter in "aeiouyAEIOUY":
            vowels += 1
    print(vowels)


def find_consonents(name):
    '''
    finds the number of consonents in the name
    takes name
    returns the number of consonents
    '''
    consonents = 0
    for letter in name:
        if letter not in "aeiouyAEIOUY":
            consonents += 1
    print(consonents)


def get_firstname(name):
    '''
    this function returns the user's first name
    takes name
    returns the first name out of the entire name
    '''
    for i,letter in enumerate(name):                #goes through the array keeping track of the place in the array
        if letter == " ":
            print(name[:i])
            break


def get_lastname(name):
    '''
    this function returns the user's last name
    takes name
    returns the last name out of the entire name
    '''
    spaces = []
    for i,letter in enumerate(name):
        if letter == " ":
            spaces.append(i)           
    print(name[spaces[-1] + 1:])
            

def get_middlename(name):
    '''
    this function returns the user's middle name
    takes name
    returns the middle name out of the entire name
    '''
    spaces = []                      
    for i,letter in enumerate(name):
        if letter == " ":
            spaces.append(i)           
    print(name[spaces[0] + 1: spaces[-1]])


def is_hyphen(name):
    '''
    this function returns boolean if the last name contains a hyphen
    takes name
    returns true or false based on if there is a hyphen in the last name
    '''
    #performs the last name function
    spaces = []                         
    for i,letter in enumerate(name):
        if letter == " ":
            spaces.append(i)           
    lastname = name[spaces[-1] + 1:]
    
    hyphen = False
    for letter in lastname:
        if letter == "-":
            hyphen = True
            break
    print(hyphen)


def make_lowercase(name):
    '''
    this function converts the user's name to all lowercase letters
    takes name
    returns the user's name in all lowercase
    '''
    new_name = ""
    for letter in name:
        if 65 <= ord(letter) <= 90:                 #finds ord of the letters in the name from the ascii table which assigns a number to each character
            new_name += chr(ord(letter) + 32)       #converts the number back to its assigned character after adding 32 to make it lowercase
        else:
            new_name += letter
    print(new_name)

def make_uppercase(name):
    '''
    this function converts the user's name to all uppercase letters
    takes name
    returns the user's name in all uppercase
    '''
    new_name = ""
    for letter in name:
        if 97 <= ord(letter) <= 122:
            new_name += chr(ord(letter) - 32)
        else:
            new_name += letter
    print(new_name)
    return new_name
        
def scramble_name(name):
    '''
    this function modifies the array of the user's name to create a random name (mixes up letters)
    takes name
    returns the mixed up letters of the user's name
    '''
    new_name = list(name)
    random.shuffle(new_name)
    print(''.join(new_name))                        #joins each separate character together to form a word

def is_palindrome(name):
    '''
    this function returns boolean if the user's name is a palindrome
    takes name
    returns true or false based on if the user's name is a palindrome
    '''
    palindrome = False
    if name == name[::-1]:                          #if the name equals the name in reverse
        palindrome = True
    print(palindrome)

def get_initials(name):
    '''
    this function makes initials out of the user's name
    takes name
    returns the initials of the user's name
    '''
    new_name = list(name)
    initials = new_name[0]
    for i, letter in enumerate(new_name):
        if letter == " ":
            initials += new_name[i + 1]             #adds the next character (the one after the space)
    print(initials)

def make_alphabetical(name):
    '''
    this function returns the user's full name as a sorted array of characters
    takes name
    returns the array in alphabetical order
    '''
    new_name = list(name)
    new_name.sort()
    print(new_name)
  
def is_title(name):
    '''
    this function returns boolean if the name contains a title or distinction
    takes name
    returns true or false based on if there is a title or distinction in the user's name
    '''
    titles = ["Dr.", "Sir", "Esq", "Ph.d"]
    distinction = False
    for item in titles:
        if item in name:
            distinction = True
            break
    print(distinction)

def how_popular(name):
    '''
    this function returns the rank of how popular the user's name is by using a dataset of popular name rankings
    takes name
    returns the user's name in uppercase and the popularity rank of the user's name
    '''
    popularity = open("c:\\Users\hgoodner24\\Downloads\\Baby_Names.csv")
    popularity.readline()
    first_name = name[:name.index(' ')]             #takes just the first name of the full name
    first_name = make_uppercase(first_name)         #uses uppercase function
    for row in popularity:
        names = row.split(",")
        if first_name == names[0][1:-1]:            #strips quotes surrounding the name in the database
            print("Rank:" + names[1])
            break
        else:
            print("Name not found")
            break

if __name__ == '__main__':
    main()