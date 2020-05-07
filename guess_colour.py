import random as r        #random package imported
list_of_colour=["red","green","yellow","blue","black","white","violet","orange"]    #list initialized by the program
print("Welcome to Guess the COLOUR")       #display message
i=0;          # i object is initialized
while(i==0):      #while loop begins
    g=r.randint(0,7)    #random integers initialized to g
    S=list_of_colour[g];  #the value in the list is initialized to the new object
    c=str(input("enter your guess colour(but it should be a string )"));  #input from the user
    if (S.lower()==c.lower()):  #condition to check the answer
        print("guess is correct and you have guessed the right colour in my mind \n");  #display message 
    else :        #condition if failed
        print("guess is wrong ");         #display message 
    i=int(input("do you want to play again,if yes press(0) or press (1)"))    #input from the user to continue or not 
