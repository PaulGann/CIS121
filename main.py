#Title: Correct Change 
#Name: Paul Gann
#Date: 04 April 2022
#Purpose of Program: Correctly calculate the correct denominations of coin change to be returned to the customer for the amount of change input.
#User enters in a change value between 1 and 99
#Program outputs the number of quarters, dimes, nickels, and pennies to return to the user.

#INPUT-----------------------------------------------------------------
#create a variable named change, ask the user for the change value, be sure these are number data types

print()  # A greeting to print only at the start of the program (outside of any loop).
print("Welcome to 'Correct Change'.")
change = input("Please enter the amount of change to calculate: ")  # Request change amount to be calculated from the user
# Validate input - only integers allowed
try:
    int(change) # Validating the input is an integer; if not skips to the exception at the end.
    change = int(change)  # Convert user input to an integer
    if change not in range(1,100):  # Verify user input conforms with parameters
        print()
        print("I am sorry; you entered " + str(change) + " which is more than 100 cents.")
        print("Please re-run and enter an integer between 1 and 99.")
        quit()
    else:  
        # PROCESSING------------------------------------------------------------
        #Develop assignment statements to figure the number of quarters, dimes, nickels, and pennies

        #quarters
        quarters = change // 25
        left_over_after_quarters = change % 25

        #dimes
        dimes = left_over_after_quarters // 10
        left_over_after_dimes = left_over_after_quarters % 10

        #nickels
        nickels = left_over_after_dimes // 5
        left_over_after_nickels = left_over_after_dimes % 5

        #pennies
        pennies = left_over_after_nickels

     #OUTPUT-----------------------------------------------------------------
     #The number of quarters, dimes, nickels, pennies.
        print()
        print("```")
        print("Here is your change: ") 
        if quarters > 1:
            print (str(quarters) + " x Quaters")
        else:
            print (str(quarters) + " x Quarter") 
        if dimes > 1:
            print (str(dimes) + " x Dimes")
        else:
            print (str(dimes) + " x Dime") 

        print (str(nickels) + " x Nickel")  # Skipping plural Nickels as that would be Dimes
        
        if pennies > 1:
            print (str(pennies) + " x Pennies")
        else:
            print (str(pennies) + " x Penny") 
    print()
    print("```")
    quit()

except ValueError:  # If user enters a non-integer, print an error and exit.
    print("Invalid input.  Please re-run, and try again with an integer between 1 and 99.")
    quit()