"""Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
"""
args = input("Enter a list of words separated by spaces: ").split()

if args:
    shortest = min(args, key=len)
    print("The sgortest word is: ",shortest)
else:
    print("No arguments provided.")
