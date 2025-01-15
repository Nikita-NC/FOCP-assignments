"""Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

password1 = input("Enter a new password: ")

Bad_passwords=['password', 'letmein', 'sesame', 'hello', 'justinbieber']

if 8<= len(password1) <= 12:
    if password1.lower() in Bad_passwords:
        print("Error, Please choose a different password.")
    else:
        password2= input("Enter a password for conformation: ")

        if password1==password2:
            print("Password Set")
        else:
            print("Error, Please try again. ")    
else:
        print("Password must be between 8 and 12.")            