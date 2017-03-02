"""
Design Prolog 
Author:Karthik Nayak
Date: 24th Sept 2015
Purpose: to ask the user for some personal information and,
use it to generate a hashed version of their password (with userid "salt")

 Preconditions:  first name, last name, userid, password

 Postconditions:  prompts for inputs, then the userid,
 full name and hashed password (with salt) separated by colons on one line

"""

# Importing the hashlib library used to hashing the password 
from hashlib import *
def main():
   
    # Taking inputs from user 
    firstname = input("Enter your first name:")
    lastname = input("Enter your last name:")
    username = input("Enter a userid:")
    password = input("Enter a password:")
    
    #Concatenate the password  with the userid to form the string to hash
    hashword = password + username
    
    #Call the hashing function with the string to hash from previous step
    hashed_password = sha256(hashword.encode()).hexdigest()
    
    #Display the userid, full name and hashed string on the screen,
    #separated by colons
    print()
    print(username,":",firstname," ",lastname,":",hashed_password,sep="")
    
    # Retaking password from user 
    print()      
    verify = input("Enter your password again:")
    
    #Concatenate the re-entered password  with the userid to form the string to hash
    verify = verify + username    
    
    # Hashing the re-entered password 
    verify_password = sha256(verify.encode()).hexdigest()
    
    #Verifying the password     
    if verify_password == hashed_password:
        print("Welcome back")
    else:
        print("You are banned")
main()

