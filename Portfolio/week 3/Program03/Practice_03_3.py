"""Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long"""

password1 = input("Enter a new password: ")
password2= input("Enter a password for conformation: ")

def set_password():

    if 8<= len(password1)<= 12:
        if password1==password2:
            print("Password Set")

        else:
            print("Error, Please try again. ")

    else:
        print("Password must be between 8 and 12.")            

set_password()