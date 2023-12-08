#Author: Harley Goodner
#Date: November 28, 2023
#Discription: This code was created to build an archetecture to allow for the analysis of data. The program allows a user to sift through data and answer potential questions/manipulate the data itself by adding or deleting rows in the file.
#Bugs: When adding a student to the file, two blank rows are added to the file under the row with the new student.
#Specs Answered: I provided functions for requirements 1,2,3,4,5,6,7,9,9a. I also added 9b,10,and 10a to improve the program and I added challenges 12 and 14.

import os
import matplotlib.pyplot as plt
from csv import writer

def main():
    '''
    main function that executes entire program
    '''

    file_input = open("c:\\Users\hgoodner24\\Desktop\\CS2\\gcds_data2.csv") #opens the data

    file_input.readline()                                                   #skip first line of header info
    run = True

    while run is True:
        answer = input("Menu:\n 1. Find names of all Freshmen \n 2. Find total boys vs. Total girls \n \
3. Find number of seniors \n 4. Find high schoolers who live in Rye \n 5. Find number of students in a given grade \
\n 6. Find particular student \n 7. Add student to the database \n 8. Sort students by lastname alphabetically \n \
9. Find number of students in each grade of highschool \n 10. Delete a student from the data \n Q. Quit \n Enter your Choice: ")    #creates menu for user
        #runs the function corresponding to the action the user decides to take and takes the data file as the input for each function
        if answer == "1":   
            check_freshmen(file_input)
        elif answer == "2":
            find_gender(file_input)
        elif answer == "3":
            count_seniors(file_input)
        elif answer == "4":
            check_rye_high(file_input)
        elif answer == "5":
            count_students(file_input)
        elif answer == "6":
            find_student(file_input)
        elif answer == "7":
            add_student(file_input)
        elif answer == "8":
            sort_names(file_input)
        elif answer == "9":
            see_grades(file_input)
        elif answer == "10":
            delete_student(file_input)
        elif answer == "Q":
            run = False
            print("bye")
            return
        

def check_freshmen(file_in):
    '''
    defines the function check_freshmen which takes one input (the file) and outputs the names of the ninth graders in the file
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns names of the ninth grade students in the file
    '''
    file_in.seek(0)                                     #move pointer to line 1

    for row in file_in:

        student = row.split(",")
        if student[3] == "9":
            print(student[0] + " " + student[2])

def find_gender(file_in):
    '''
    defines the function find_gender which takes one input (the file) and outputs number of boys and girls in the file
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns the amount of boys and girls in the file and presents the numbers graphically
    '''
    file_in.seek(0)
    boys = 0
    girls = 0
    for row in file_in:
        student = row.split(",")
        if student[4] == "M":
            boys +=1
        elif student[4] == "F":
            girls +=1    
    genders = ["Boys","Girls"]                              #inputs for the x-axis of the graph
    amount_of_gender = [boys,girls]                         #inputs for the y-axis of the graph
    plt.bar(genders, amount_of_gender, color ='purple',     #creates a bar graph with an x-axis consisting of the genders, a y-axis consisting of the amount of each gender, makes the color of the bars purple and the width of the bars .3
        width = 0.3)
    plt.xlabel("Gender")                                    #labels the x-axis of the graph
    plt.ylabel("Number of students")                        #labels the y-axis of the graph
    plt.title("Number of Boys vs. Girls")                   #labels the title of the graph
    plt.show()                                              #renders and displays the graph

def count_seniors(file_in):
    '''
    defines the function count_seniors which takes one input (the file) and outputs number of twelfth graders in the file
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns the number of twelfth graders in the file
    '''
    file_in.seek(0)
    seniors = 0
    for row in file_in:
        student = row.split(",")
        if student[3] == "12":
            seniors +=1
    print("Senior Class Size: " + str(seniors))

def check_rye_high(file_in):
    '''
    defines the function check_rye_high which takes one input (the file) and outputs names of students who live in Rye
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns the names of the students who live in rye
    '''
    file_in.seek(0)                                     
    for row in file_in:
        student = row.split(",")
        if (student[3] == "9") or (student[3] == "10") or (student[3] == "11") or (student[3] == "12"):
            if student[7] == "Rye":
                print(student[0] + " " + student[2])

def count_students(file_in):
    '''
    defines the function count_students which takes one input (the file) and outputs number of students in a certain grade
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns the number students in a user-determined grade
    '''
    file_in.seek(0)      
    while True:
        grade = input("What class do you want to see the size of? Enter number or PK = Pre-K and K= Kindergarten ")
        if grade.isnumeric():
            if int(grade) not in range(1,12):                           #if the grade the user asks for the size of is not a grade K-12, tells the user their entry was invalid
                print("invailid entry")
                break
        
        if not grade.isnumeric() and grade not in ["PK", "K"]:
            print("invailid entry")
            break

        size = 0                                                        #creates variable size that will represent the size of the grade and sets it to zero
        for row in file_in:
            student = row.split(",")
            if str(grade) == student[3]:
                size +=1                                                #adds one to the size variable if the grade of the student matches the grade the user asked the size of
        print("Class Size: " + str(size))                               #displays the class size
        break
                                  

def find_student(file_in):
    '''
    defines the function find_student which takes one input (the file) and outputs the row of the file that the user wants to see
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns the row of the file that the user asks to see
    '''
    found = False                                                       #creates variable found and sets it to False so that the program can tell the user if the row they want to find exists
    file_in.seek(0)
    kid = input("Enter firstname and lastname of student").split(" ")
    firstname = kid[0]
    lastname = kid[1]
    for row in file_in:
        student = row.split(",")
        if (lastname == student[2]) and (firstname == student[0]):
            found = True                                               #since the row was found, the variable is equal to true
            print(row)
            break
    if found == False:                                                 #if the row is not found, the variable will stay equal to false so the program can tell the user the row doesn't exist
        print("Record not found")
        
def add_student(file_in):
    '''
    defines the function add_student which takes one input (the file) and adds a row to the file
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns nothing to the user, but adds the user-inputed row to the file
    '''
    file_in.seek(0)
    new_student = input("Enter firstname, middle name, lastname, grade, sex,\
    advisor lastname, advisor firstname, home city, home state, home zip").split(',')   #asks the user to write out the row they want to add to the file
    new_student[-1] = new_student[-1]
    new_student[0] = '\n' + new_student[0]

    with open('gcds_data2.csv', 'a') as f_object:                                       #opens the existing CSV file in append mode and create a file object for the file

        writer_object = writer(f_object)                                                #passes this file object to csv.writer() and get a writer object
 
        writer_object.writerow(new_student)                                             #writes the user's input into the file as a new row

    f_object.close()                                                                    #close the file object

def sort_names(file_in):
    '''
    defines the function sort_names which takes one input (the file) and outputs the names of the students in the file
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns first and last name of each student in the file
    '''
    file_in.seek(0)
    for row in file_in:
        student = row.split(",")
        print(student[0] + "," + student[2])

def see_grades(file_in):
    '''
    defines the function see_grades which takes one input (the file) and outputs the number of students in each grade of high school
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns the number of students in each grade of high school in the file and presents the data as a graph
    '''
    file_in.seek(0)
    freshman = 0
    sophomores = 0
    juniors = 0
    seniors = 0
    for row in file_in:
        student = row.split(",")
        if student[3] == "9":
            freshman +=1
        elif student[3] == "10":
            sophomores +=1    
        elif student[3] == "11":
            juniors +=1 
        elif student[3] == "12":
            seniors +=1       
    grades = ["Freshman","Sophomors","Juniors", "Seniors"]          #inputs for the x-axis of the graph
    number_of_students = [freshman,sophomores,juniors,seniors]      #inputs for the y-axis of the graph
    plt.bar(grades, number_of_students, color ='blue', 
        width = 0.3)                                                #creates a bar graph with an x-axis consisting of the genders, a y-axis consisting of the amount of each gender, makes the color of the bars blue and the width of the bars .3
    plt.xlabel("Grade")                                             #labels the x-axis of the graph
    plt.ylabel("Number of students")                                #labels the y-axis of the graph
    plt.title("Number of Students in each Highschool Class")        #titles the graph
    plt.show()                                                      #renders and displays the graph

def delete_student(file_in):
    '''
    defines the function delete_student which takes one input (the file) and deletes a row in the file
    takes the variable file_in which is defined by the file with all the data being manipulated
    returns nothing, but deletes the row in the file that the user wants to delete
    '''
    file_in.seek(0)
    kid = input("What is the first and last name of the student you want to delete? ").split(" ")
    fname = kid[0]
    lname = kid[1]
    new_file = open('c:\\Users\hgoodner24\\Desktop\\CS2\\new.csv', 'w')     #opens a new file in writer mode
    for row in file_in:                                                     #runs through each row in the original file
        student = row.split(",")
        if (student[0] == fname) and (student[2] == lname):                 #does nothing to the row in the orginal file that the user wants to delete
            continue
        else:
            new_file.write(row)                                             #writes all the other rows to the new file
    file_in.close()                                                         #closes the original file
    new_file.close()                                                        #closes the new file
    os.remove('gcds_data2.csv')                                             #deletes the entire original file
    os.rename('new.csv','gcds_data2.csv')                                   #renames the new file to match the name of the old, deleted file




if __name__ == '__main__':
    main()                                                                  #runs the main
