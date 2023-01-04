# Establish randomability 
import random
from random import randint

#Declare list of months for iteration later on. 
months_in_year = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Ask the user what their name is. 
name = input("What is your name?: ")

#Prompt the user at least 5 quesstions.
for number in range(0,5):
#The following will print to the console    
    print(name + " were you born in " + random.choice(months_in_year) + ' year ' + str(randint(1924,2014)) + '?')
#The user will input yes or no. 
    answer = input("Please answer yes or no?: ")
    if answer == 'yes':
        print("I guessed correctly, I win!")
        #break out of loop if the user answers yes
        break
    if answer == 'no':
        print("Aww man I lose")
# When the range ends the program prints the following statement. 
else:
    print("I have other things to do. Good-bye.")
    
    
        









