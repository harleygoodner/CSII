#Author: Harley Goodner
#Date: September 22, 2023
#Discription: This code was created to determine the postage cost for entered mail. By determining the postage class (found by the length, width, and thickness of the piece) and the number of postage zones the piece must travel to, the algorithm can return the cost to mail the piece.
#Bugs: None found


def size(length,height,thick):    
    """
    #defines the function size which takes three float inputs (length, width, height) and outputs the classtype of the package
    #length is defined by the user's measurement of the length of the piece of mail
    #height is defined by the user's measurement of the height of the piece of mail
    #thick is difined by the user's measurement of the height of the piece of mail
    #returns the classtype of the piece of mail
    """
    #determines the classtype of the package depending on its length, height, and thickness
    if (3.5<=length<=4.25) and (3.5<=height<=6) and (.007<=thick<=.016):          
        return "Post Card"                                                              
    elif (4.25<length<6) and (6<height<11.5) and (.007<=thick<=.015):                  
        return "Large Post Card"                                                        
    elif (3.5<=length<=6.125) and (5<=height<=11.5) and (.016<thick<.25):               
        return "Envelope"                                                              
    elif (6.125<length<24) and (11<=height<=18) and (.25<=thick<=.5):                  
        return "Large Envelope"                                                        
    elif ((2*length)+(2*height)+(2*thick))<=84:                                         
        return "Package"                                                                
    elif 84<((2*length)+(2*height)+(2*thick))<130:                                      
        return "Large Package"                                                         
    else:                                                                              
        return "Unmailable"
   
def zone(z): 
    """
    #defines the function zone which takes one input (an integer zip code) and outputs the postal zone of the zip code
    #z is an integer defined by either the starting or ending zip code the user is sending their piece of mail to or from
    #returns the postal zone the piece of mail is being sent to or from
    """
    #determines the postal zone of the zip code that was input
    if (1<=z<=6999):              
        return "1"                                                                     
    elif (7000<=z<=19999):                                                             
        return "2"                                                                      
    elif (20000<=z<=35999):                                                             
        return "3"                                                                      
    elif (36000<=z<=62999):                                                            
        return "4"                                                                      
    elif (63000<=z<=84999):                                                            
        return "5"                                                                      
    elif (85000<=z<=99999):                                                             
        return "6"                                                                      

def getcost(classtype,netzone): 
    """
    #defines the function getcost that takes two inputs, the classtype of the package and the amount of zones the package will travel through
    #classtype is defined by the classtype of the piece of mail which was returned by the size function
    #netzone is defined by the absolute value of the starting and ending postal zones of the package (determined by the zone function)
    #returns the cost of mailing the piece of mail
    """
    #determines the cost
    if classtype=="Post Card":      
        cost=.20+(.03*netzone)                                                          
    elif classtype=="Large Post Card":                                                  
        cost=.37+(.03*netzone)                                                         
    elif classtype=="Envelope":                                                      
        cost=.37+(.04*netzone)                                                          
    elif classtype=="Large Envelope":                                                 
        cost=.60+(.05*netzone)                                                         
    elif classtype=="Package":                                                          
        cost=2.95+(.25*netzone)                                                         
    elif classtype=="Large Package":                                                   
        cost=3.95+(.35*netzone)                                                         
    elif classtype=="Unmailable":                                                      
        cost="Package is Unmailable"                                                    

    if type(cost) == str:                   #if cost is 'unmailable' return cost       
        return cost
    else:
        cost = format(cost, ".2f")          #if the cost is a float, rounds it to two decimal points
        if cost[0] == "0":
            cost = cost[1:]                 #removes the zero in front of the decimal if the cost is less than one (matches specs)
            return cost
        else:
            return cost

def main(): 
    """
    #main function that executes entire program
    """
    for _ in range(0,5):
        try:                                                                                                     
            data=input("Enter length, width, thickness, starting zip code, ending zip code: ").split(",")    #tells the user to input all their data and splits the data at each comma
            length=float(data[0])                                                                                #length of the mail
            height=float(data[1])                                                                                #height of the mail
            thick=float(data[2])                                                                                 #thickness of the mail
            zip1=int(data[3])                                                                                    #starting zip code
            zip2=int(data[4])                                                                                    #ending zip code
            classtype=size(length,height,thick)                                                                  #calls the size function
            zone1=int(zone(zip1))                                                                                #calls the zone function inputting zip1
            zone2=int(zone(zip2))                                                                                #calls the zone function inputting zip2
            net_zone=abs(zone1-zone2)                                                                            #takes absolute value of zones
            mailing_cost=getcost(classtype,net_zone)                                                             #calls the getcost function
            print(f"Postage Cost: {mailing_cost}")  
        except:                                                                   #the function isn't performed if the user inputs data that causes an error
            print("That data was invalid.")
            main()                                                                #restarts program if an error had occurred
            break
main()                                                                                                                  
