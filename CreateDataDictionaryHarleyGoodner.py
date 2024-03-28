#Author: Harley Goodner
#Date: March 28, 2023
#Discription: This code was created to create a dictionary that collects the frequency of words in Shakespeare plays and then graphs the frequencies of the ten most frequent words in a pie chart.


from pathlib import Path
import plotly.express as px

def main():
    '''
    main function that executes entire program
    '''

    current_dir = Path(__file__).parent
    file_path1 = current_dir / "Romeo_and_Juliet.txt"
    file_path2 = current_dir / "Midsummer_Night's_Dream.txt"

    file_input1 = open(file_path1)
    file_input2= open(file_path2)


    file_input1.readline()
    file_input2.readline()
    
    run = True

    while run is True:
        answer = input("What do text do you want to look at? \n 1. Romeo \n 2. Midsummer Night's Dream \n Q. Quit \n Enter Your Choice: ") #creates the menu for user
        #runs the function corresponding to the action the user decides to take and takes the data file as the input for each function
        if answer == "1": 
            get_word_frequency(file_input1)   
        elif answer == "2":
            get_word_frequency(file_input2)
        elif answer == "Q":
            run = False
            print("Bye")
            return
        else:
            print("Invalid")
            
   
   
def get_word_frequency(file_in):
    '''
    creates a dictionary that collects the frequency of words in a text file and then graphs them with a pie chart
    takes the variable file_in which is defined by the text file that is being examined
    returns a dictionary of word frenquenies and a pie chart of the top 10 most frequent words
    '''
    word_freq = {}
    for line in file_in:   
        for word in line.split(" "):
            clean = ""
            for char in word:
                if char.lower() in "abcdefghijklmnopqrstuvwxyz":                                    #makes all characters lowercase and removes characters that are not letters
                    clean += char.lower()
            if not clean:
                continue

            if clean in word_freq.keys():
                word_freq[clean] += 1
            else:
                word_freq[clean] = 1
    for i in ["and", "it", "the", "to", "a", "of", "my", "is", "that", "in", "you",                #removes unneccesary frequent words (pronouns, conjunctions, etc.)
            "thou", "me", "not", "with", "for", "this", "be", "but","i", "her", "as", 
            "she", "so", "he", "him", "thee", "your", "am", "do", "their", "by", "thy",
            "shall", "now", "then", "if", "or", "what", "will", "o", "his", "have","all", 
            "from", "an", "on", "here", "at", "which", "there", "are", "we", "did", "our", 
            "come", "when", "go", "no", "they", "man", "sc", "must", "more", "would", "one",
            "how", "hath", "up", "out", "act"]:
        try:
            del word_freq[i]
        except:
            pass
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse = True))    #sorts the dictionary from most frequent to least frequent
    print(dict(sorted_word_freq))
    updated = dict([(i, sorted_word_freq[i]) for i in list(sorted_word_freq.keys())[:10]])          #makes a new dictionary with only the top ten most frequent words from the original sorted dictionary
     
    fig = px.pie(values=updated.values(), names=updated.keys(), title= "Frequency of Words in Shakespeare:")                                     #makes a pie chart from the dictionary defined by the variable 'updated'
    fig.show()

    
   


if __name__ == '__main__':
    main()







