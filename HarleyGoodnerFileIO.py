#Author: Harley Goodner
#Date: November 28, 2023
#Discription: This code was created to 
#Bugs: None found

import os
import matplotlib.pyplot as plt
from csv import writer

def main():

    file_input = open("c:\\Users\hgoodner24\\Desktop\\CS2\\gcds_data2.csv")

    file_input.readline()                       #skip first line of header info
    run = True

    while run is True:
        answer = input("Menu:\n 1. Find names of all Freshmen \n 2. Find total boys vs. Total girls \n \
3. Find number of seniors \n 4. Find high schoolers who live in Rye \n 5. Find number of students in a given grade \
\n 6. Find particular student \n 7. Add student to the database \n 8. Sort students by lastname alphabetically \n \
9. Find number of students in each grade of highschool \n 10. Delete a student from the data \n Q. Quit \n Enter your Choice: ")
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
    """ doc """

    file_in.seek(0)                                     #move pointer to line 1

    for row in file_in:

        student = row.split(",")
        if student[3] == "9":
            print(student[0] + " " + student[2])

def find_gender(file_in):
    file_in.seek(0)
    boys = 0
    girls = 0
    for row in file_in:
        student = row.split(",")
        if student[4] == "M":
            boys +=1
        elif student[4] == "F":
            girls +=1    
    x_axis = ["Boys","Girls"]
    y_axis = [boys,girls]
    plt.bar(x_axis, y_axis, color ='purple', 
        width = 0.3)
    plt.xlabel("Gender")
    plt.ylabel("Number of students")
    plt.title("Number of Boys vs. Girls")
    plt.show()  

def count_seniors(file_in):
    file_in.seek(0)
    seniors = 0
    for row in file_in:
        student = row.split(",")
        if student[3] == "12":
            seniors +=1
    print("Senior Class Size: " + str(seniors))

def check_rye_high(file_in):
    file_in.seek(0)                                     #move pointer to line 1
    for row in file_in:
        student = row.split(",")
        if (student[3] == "9") or (student[3] == "10") or (student[3] == "11") or (student[3] == "12"):
            if student[7] == "Rye":
                print(student[0] + " " + student[2])

def count_students(file_in):
    file_in.seek(0)      #move pointer to line 1
    while True:
        grade = input("What class do you want to see the size of? Enter number or PK = Pre-K and K= Kindergarten ")
        
        if (1<=int(grade)<=12) or (grade == "PK") or (grade == "K"):                                
            size = 0
            for row in file_in:
                student = row.split(",")
                if grade == student[3]:
                    size +=1
            print("Class Size: " + str(size))
            break
        else:
            print("invalid entry")

def find_student(file_in):
    found = False
    file_in.seek(0)
    kid = input("Enter firstname and lastname of student").split(" ")
    firstname = kid[0]
    lastname = kid[1]
    for row in file_in:
        student = row.split(",")
        if (lastname == student[2]) and (firstname == student[0]):
            found = True
            print(row)
            break
    if found == False:
        print("Record not found")
        
def add_student(file_in):
    file_in.seek(0)
    new_student = input("Enter firstname, middle name, lastname, grade, sex,\
advisor lastname, advisor firstname, home city, home state, home zip").split(',') 
    new_student[-1] = new_student[-1] + '\n'
    new_student[0] = '\n' + new_student[0]

    with open('gcds_data2.csv', 'a') as f_object:    #Open the existing CSV file in append mode and create a file object for the file

        writer_object = writer(f_object)             #Pass this file object to csv.writer() and get a writer object
 
        writer_object.writerow(new_student)
    
    f_object.close()                                 # Close the file object

def sort_names(file_in):
    file_in.seek(0)
    for row in file_in:
        student = row.split(",")
        print(student[0] + "," + student[2])

def see_grades(file_in):
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
    x_axis = ["Freshman","Sophomors","Juniors", "Seniors"]
    y_axis = [freshman,sophomores,juniors,seniors]
    plt.bar(x_axis, y_axis, color ='blue', 
        width = 0.3)
    plt.xlabel("Grade")
    plt.ylabel("Number of students")
    plt.title("Number of Students in each Highschool Class")
    plt.show()  

def delete_student(file_in):
 
    file_in.seek(0)
    kid = input("What is the first and last name of the student you want to delete? ").split(" ")
    fname = kid[0]
    lname = kid[1]
    new_file = open('c:\\Users\hgoodner24\\Desktop\\CS2\\new.csv', 'w')
    for row in file_in:
        student = row.split(",")
        if (student[0] == fname) and (student[2] == lname):
            continue
        else:
            new_file.write(row)
    file_in.close()
    new_file.close()
    os.remove('gcds_data2.csv')
    os.rename('new.csv','gcds_data2.csv')




if __name__ == '__main__':
    main()