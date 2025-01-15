"""Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time."""

def set_password():
    Bad_passwords=['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    
    while True:
        password1 = input("Enter a new password: ")

        if not (8<= len(password1)<= 12):
           print("Password must be between 8 adn 12")
      
        elif password1.lower() in Bad_passwords:
            print("Error, Please choose a different password.") 

        else:
            password2= input("Enter a password for conformation: ")
            if password1==password2:
                print("Password Set")
                break
            else:
                print("Error, Please try again. ") 
            
set_password()