#Harley Goodner
#This code was created to determine the postage cost for entered mail. By determining the postage class (found by the length, width, and thickness of the piece) and the number of postage zones the piece must travel to, the algorithm can return the cost to mail the piece.
#September 22, 2023


while True: #creates infinite loop
    def size(length,height,thick):     
        #defines the function size which takes three float inputs (length, width, height) and outputs the classtype of the package
        #length is defined by the user's measurement of the length of the piece of mail
        #height is defined by the user's measurement of the height of the piece of mail
        #thick is difined by the user's measurement of the height of the piece of mail
        #returns the classtype of the piece of mail
        
        if (3.5<=length<=4.25) and (3.5<=height<=6) and (.007<=thick<=.016):                #if the package meets these parameters, perform the function
            return "Post Card"                                                              #returns the classtype as being a post card
        elif (4.25<length<6) and (6<height<11.5) and (.007<=thick<=.015):                   #if the package doesn't meet the post card parameters but meets these parameters, perform the function
            return "Large Post Card"                                                        #returns the classtype as being a large post card
        elif (3.5<=length<=6.125) and (5<=height<=11.5) and (.016<thick<.25):               #if the package doesn't meet prior parameters but meets these parameters, perform the function
            return "Envelope"                                                               #returns the classtype as being an envelope
        elif (6.125<length<24) and (11<=height<=18) and (.25<=thick<=.5):                   #if the package doesn't meet prior parameters but meets these parameters, perform the function
            return "Large Envelope"                                                         #returns the classtype as being a large envelope
        elif ((2*length)+(2*height)+(2*thick))<=84:                                         #if the package doesn't meet prior parameters but meets these parameters, perform the function
            return "Package"                                                                #returns the classtype as being a package
        elif 84<((2*length)+(2*height)+(2*thick))<130:                                      #if the package doesn't meet prior parameters but meets these parameters, perform the function
            return "Large Package"                                                          #returns the classtype as being a large package
        else:                                                                               #if the package doesn't meet any of the previous parameters, perform the function
            return "Unmailable"                                                             #returns the classtype as unmailable
   
    def zone(z): 
        #defines the function zone which takes one input (an integer zip code) and outputs the postal zone of the zip code
        #z is an integer defined by either the starting or ending zip code the user is sending their piece of mail to or from
        #returns the postal zone the piece of mail is being sent to or from
        if (1<=z<=6999):                                                                    #if the input is an integer between 1 and 6999, perform the function
            return "1"                                                                      #returns the output "1"
        elif (7000<=z<=19999):                                                              #if the input is an integer between 7000 and 19999, perform the function
            return "2"                                                                      #returns the output "2"
        elif (20000<=z<=35999):                                                             #if the input is an integer between 20000 and 35999, perform the function
            return "3"                                                                      #returns the output "3"
        elif (36000<=z<=62999):                                                             #if the input is an integer between 36000 and 26999, perform the function
            return "4"                                                                      #returns the output "4"
        elif (63000<=z<=84999):                                                             #if the input is an integer between 63000 and 84999, perform the function
            return "5"                                                                      #returns the output "5"
        elif (85000<=z<=99999):                                                             #if the input is an integer between 85000 and 99999, perform the function
            return "6"                                                                      #returns the output "6"

    def getcost(classtype,netzone): 
        #defines the function getcost that takes two inputs, the classtype of the package and the amount of zones the package will travel through
        #classtype is defined by the classtype of the piece of mail which was returned by the size function
        #netzone is defined by the absolute value of the starting and ending postal zones of the package (determined by the zone function)
        #returns the cost of mailing the piece of mail
        if classtype=="Post Card":                                                          #if the classtype input is a Post Card, perform the function
            cost=.20+(.03*netzone)                                                          #determine cost
            return round(cost,2)                                                            #returns the cost rouded to two decimals
        elif classtype=="Large Post Card":                                                  #if the classtype input is't a post card and is a Large Post Card, perform the function
            cost=.37+(.03*netzone)                                                          #determine cost
            return round(cost,2)                                                            #returns the cost rouded to two decimals
        elif classtype=="Envelope":                                                         #if the classtype input isn't one of the previous types and is an envelope, perform the function
            cost=.37+(.04*netzone)                                                          #determine cost
            return round(cost,2)                                                            #returns the cost rouded to two decimals
        elif classtype=="Large Envelope":                                                   #if the classtype input isn't one of the previous types and is a Large Envelope, perform the function
            cost=.60+(.05*netzone)                                                          #determine cost
            return round(cost,2)                                                            #returns the cost rouded to two decimals
        elif classtype=="Package":                                                          #if the classtype input isn't one of the previous types and is a package, perform the function
            cost=2.95+(.25*netzone)                                                         #determine cost
            return round(cost,2)                                                            #returns the cost rouded to two decimals
        elif classtype=="Large Package":                                                    #if the classtype input isn't one of the previous types and is large package, perform the function
            cost=3.95+(.35*netzone)                                                         #determine cost
            return round(cost,2)                                                            #returns the cost rouded to two decimals
        elif classtype=="Unmailable":                                                       #if the classtype input isn't one of the previous types and is something unmailable, perform the function
            cost="Package is Unmailable"                                                    #there is no cost because the package is unmailable
            return cost                                                                     #returns the cost to the user

    while True:                                                                             #creates an infinite loop
        def main(): 
            try:                                                                                                                #tries to perform the following function
                data=input("Enter length, width, thickness, starting zip code, ending zip code: ").split(",")                   #tells the user to input all their data and splits the data at each comma
                length=float(data[0])                                                                                           #defines the variable length (a float) as the first item in the data input
                height=float(data[1])                                                                                           #defines the variable height (a float) as the second item in the data input
                thick=float(data[2])                                                                                            #defines the variable thick (a float) as the third item in the data input
                zip1=int(data[3])                                                                                               #defines the variable zip1 (a float) as the fourth item in the data input
                zip2=int(data[4])                                                                                               #defines the variable zip2 (a float) as the fifth item in the data input

                classtype=size(length,height,thick)                                                                             #creates the variable classtype that is defined by calling the size function and inputing the variables length, height, and thick
                zone1=int(zone(zip1))                                                                                           #creates the variable zone1 that is defined by calling the zone function inputing zip1 and converting it to an integer
                zone2=int(zone(zip2))                                                                                           #creates the variable zone2 that is defined by calling the zone function inputing zip2 and converting it to an integer
                net_zone=abs(zone1-zone2)                                                                                       #creates the variable net_zone which is defined by taking the absolute value of zone1-zone2
                cost=getcost(classtype,net_zone)                                                                                #creates the variable cost which is defined by calling the getcost function and inputing the variables classtype and net_zone
                print(f"Postage Cost: {cost}")                                                                                  #prints the cost of mailing the piece of mail
            except:                                                                                                             #the function isn't performed if the user inputs data that causes an error
                print("That data was invalid.")                                                                                 #tells the user their data is invalid
        main()                                                                                                                  #performs the main function